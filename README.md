# LinkedIn Insights Microservice

This project is a backend microservice built using FastAPI and MongoDB.  
It fetches insights for a given LinkedIn Page ID, stores the data in a database, and exposes APIs to retrieve the stored information.

The system is designed to be simple, modular, and easy to demonstrate.

---

## Features

- Fetch LinkedIn Page details using Page ID
- Store page data, posts, and employees in MongoDB
- Retrieve data from database using REST APIs
- Automatically scrape data if page is not found in DB
- Pagination-ready endpoints
- Clean project structure

---

## Tech Stack

- Python
- FastAPI
- MongoDB
- PyMongo
- BeautifulSoup
- Uvicorn

---

## Project Structure

linkedin_insights/
├── app/
│ ├── main.py
│ ├── routes.py
│ ├── database.py
│ ├── scraper.py
│ ├── models.py
│ └── init.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## How to Run the Project

### 1. Start MongoDB
Make sure MongoDB is running locally.
You can start it using MongoDB Compass or by running `mongod.exe`.

---

### 2. Create virtual environment
python -m venv venv

java
Copy code

Activate it (Windows):
venv\Scripts\activate

yaml
Copy code

---

### 3. Install dependencies
pip install -r requirements.txt

yaml
Copy code

---

### 4. Run the server
uvicorn app.main:app --reload

arduino
Copy code

Server will run at:
http://127.0.0.1:8000

yaml
Copy code

---

## API Endpoints

### Get Page Details
GET /pages/{page_id}

pgsql
Copy code

### Get Pages by Followers Range
GET /pages?min_followers=1000&max_followers=50000

shell
Copy code

### Get Page Posts
GET /pages/{page_id}/posts

shell
Copy code

### Get Page Employees
GET /pages/{page_id}/employees

yaml
Copy code

---

## Notes

- No AI or LLM APIs are used
- Data scraping is minimal and safe
- Designed for backend-focused evaluation
