from pymongo import MongoClient
import gridfs #stores largers data image,videos etc
#connect to mongodb 
#pymongo is used to connect python to mongoDB
Client = MongoClient("mongodb://localhost:27017")
db = Client['hotel_booking']
fs=gridfs.GridFS(db)

#Hotels
hotels_data=[
    {"name":"Taj","location":"Mumbai","price":5000,"image":"hot1.jpeg"},
    {"name":"kihinoor","location":"Delhi","price":4,"image":"hpt2.jpeg"},
    {"name":"manipuram","location":"Chennai","price":10000,"image":"hot3.jpeg"}
]

#insert hotel with images
for hotel in hotels_data:
    with open (f"static/images/{hotel['image']}","rb") as img_file:
        image_id = fs.put(img_file,filename=hotel['image'])
        db.hotels.insert_one({
            "name":hotel['name'],
            "location":hotel['location'],
            "price":hotel['price'],
            "image_id":image_id
        })
print("all data inserted done")
       