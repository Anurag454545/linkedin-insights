from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["linkedin_insights"]

pages = db.pages
posts = db.posts
employees = db.employees
