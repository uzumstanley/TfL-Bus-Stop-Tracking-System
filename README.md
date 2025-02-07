# TfL-Bus-Stop-Tracking-System
Bus stop live update

# 🚌 TfL Bus Stop Tracking System

## **Overview**
The **TfL Bus Stop Tracking System** is a web application that allows users to **search for bus stops, view live arrival times, and explore routes** within London's **Transport for London (TfL)** network. The application consists of a **Flask API backend** and a **React-based frontend** with an interactive map.

## **Features**
✅ **Search for Bus Stops** by name or postcode.
✅ **Live Bus Arrivals** fetched from TfL’s API.
✅ **Interactive Map** using **Leaflet.js** to display bus stops.
✅ **Smart Search System** with an improved UI.
✅ **Route Optimization** (Future Feature: Suggest the best routes).
✅ **Fully Responsive UI** for mobile and desktop.

---

## **Tech Stack**
### **Backend** (Flask API)
- Python
- Flask
- Pandas
- Geopy
- Gunicorn (for deployment)

### **Frontend** (React)
- React.js
- Leaflet.js (for maps)
- Axios (for API calls)
- Bootstrap (for styling)

### **Hosting & Deployment**
- **Backend:** [Render](https://render.com/)
- **Frontend:** [Render](https://render.com/)
- **Version Control:** GitHub

---

## **Setup Instructions**

### **1️⃣ Clone the Repository**
```bash
# Clone the backend repo
git clone https://github.com/uzumstanley/TfL-Bus-Stop-Tracking-System.git
cd TfL-Bus-Stop-Tracking-System
```
```bash
# Clone the frontend repo
git clone https://github.com/uzumstanley/TfL-Frontend.git
cd TfL-Frontend
```

### **2️⃣ Backend Setup (Flask API)**
```bash
cd TfL-Bus-Stop-Tracking-System
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### **Run the Flask API locally**
```bash
python app.py
```
✅ The API will be live at **http://127.0.0.1:5000**

---

### **3️⃣ Frontend Setup (React)**
```bash
cd TfL-Frontend
npm install
```

#### **Run the React App locally**
```bash
npm start
```
✅ The frontend will be live at **http://localhost:3000**

---

## **API Endpoints**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home Route |
| `/stops` | GET | Get all bus stops |
| `/stops/search?name=Hyde` | GET | Search bus stops by name |

---

## **Deployment Guide**

### **1️⃣ Deploy Flask Backend on Render**
1. Push the project to GitHub.
2. Go to **[Render](https://render.com/)** and create a new **Web Service**.
3. Connect your **GitHub repository**.
4. Set the **Build Command**: `pip install -r requirements.txt`
5. Set the **Start Command**: `gunicorn app:app`
6. Click **Deploy**.

✅ **Render will provide a live URL for your API.**

### **2️⃣ Deploy React Frontend on Render**
1. Push the frontend code to GitHub.
2. Go to **[Render](https://render.com/)** and create a **Static Site**.
3. Connect the **GitHub repository**.
4. Set the **Build Command**: `npm install && npm run build`
5. Set the **Publish Directory**: `build`
6. Click **Deploy**.

✅ **Render will provide a live URL for your frontend.**

---

## **Future Improvements** 🚀
- **Integrate TfL’s API** for real-time bus arrival updates.
- **Route optimization** using Dijkstra’s Algorithm.
- **User alerts & notifications** for bus arrivals.
- **Heatmaps** showing bus stop congestion.

---

## **Contributing**
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-name`)
5. Submit a Pull Request (PR)


🚀 Built by [Stanley Ekene](https://github.com/uzumstanley)


