# 🏨 Hotel Booking Management Web App

This is a hotel booking web application that allows users to book hotels and administrators to manage hotel data. Built using **Python (Flask)** for the backend, **MongoDB** for data storage, and **HTML/CSS** for the frontend.

---

## 🚀 Features

- 🧾 Add, view, and manage hotel details
- 👤 User interface for booking and browsing
- 💾 MongoDB for backend data management
- 📸 Hotel images rendered from static directory
- 🔐 Form handling with HTML templates

---

## 📂 Project Structure
```bash
hotel_booking-master/
│
├── app.py # Main Flask application
├── mongo.py # MongoDB configuration and operations
│
├── static/
│ └── images/ # Hotel-related image assets
│
├── templates/
│ ├── index.html # Home page
│ ├── add_hotel.html # Admin page to add hotels
│ └── user.html # User view for booking

```


## 🛠️ Technologies Used

- **Python (Flask)** – lightweight web framework
- **MongoDB** – NoSQL database
- **HTML5, CSS3** – Frontend structure and styling
- **Jinja2** – Flask templating engine
- **Bootstrap (Optional)** – For responsive UI (if used)

---

## 💻 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/hotel_booking-master.git
cd hotel_booking-master
Install dependencies


pip install flask pymongo
Start MongoDB service (locally or Atlas)

Run the app


python app.py
Open in browser
Go to http://127.0.0.1:5000/
```
# 📌 Notes
Make sure MongoDB is running or properly connected via mongo.py.

Customize hotel image paths under the /static/images/ directory.

Extend HTML templates for additional features like authentication, admin dashboard, etc.

# 📷 Screenshots
Add screenshots here from static/images to demonstrate UI.

# 🧑‍💻 Author
Vaishnavi Shatagopam
🔗 [Your LinkedIn or Portfolio link]

📄 License
This project is licensed under the MIT License.

