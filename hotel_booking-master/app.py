from flask import Flask, request, render_template, redirect, url_for, Response
from pymongo import MongoClient
import gridfs
from bson import ObjectId 

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client['hotel_booking']
fs = gridfs.GridFS(db)
hotels = db['hotels']
bookings = db['bookings']

# Home route
@app.route('/')
def home():
    all_hotels = list(hotels.find({"image_id": {"$exists": True}}))
    return render_template('index.html', hotels=all_hotels)

# Serve image route
@app.route('/image/<image_id>')
def get_image(image_id):
    try:
        file = fs.get(ObjectId(image_id))
        return Response(file.read(), mimetype='image/jpeg')
    except:
        return "Image not found", 404

# Booking route
@app.route('/book/<hotel_id>', methods=['GET', 'POST'])
def book(hotel_id):
    hotel = hotels.find_one({"_id": ObjectId(hotel_id)})
    if request.method == 'POST':
        bookings.insert_one({
            "hotel_id": hotel_id,
            "name": request.form["name"],
            "Check-in": request.form["checkin"],
            "Check-out": request.form["checkout"]
        })
        return redirect(url_for('home'))
    return render_template('user.html', hotel=hotel)

# Add hotel route
@app.route('/add-hotel', methods=['GET', 'POST'])
def add_hotel():
    if request.method == 'POST':
        images = request.files.get('images')
        
        if not images:
            return "No file uploaded. Please go back and upload an image.", 400

        image_id = fs.put(images, filename=images.filename)
        hotels.insert_one({ 
            "name": request.form['name'],
            "location": request.form['location'],
            "price": request.form['price'],
            "image_id": image_id
        })
        return redirect(url_for('home'))
    
    return render_template('add_hotel.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
