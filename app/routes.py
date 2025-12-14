from fastapi import APIRouter
from app.database import pages, posts, employees
from app.scraper import scrape_page, scrape_posts, scrape_employees
from app.models import page_schema, post_schema, employee_schema

router = APIRouter()

@router.get("/pages/{page_id}")
def get_page(page_id: str):
    page = pages.find_one({"page_id": page_id})
    if not page:
        page_data = page_schema(scrape_page(page_id))
        pages.insert_one(page_data)

        for p in scrape_posts(page_id):
            posts.insert_one(post_schema(p))

        for e in scrape_employees(page_id):
            employees.insert_one(employee_schema(e))

        return page_data

    page["_id"] = str(page["_id"])
    return page

@router.get("/pages")
def filter_pages(min_followers: int = 0, max_followers: int = 1000000):
    result = []
    for page in pages.find({"followers": {"$gte": min_followers, "$lte": max_followers}}):
        page["_id"] = str(page["_id"])
        result.append(page)
    return result

@router.get("/pages/{page_id}/posts")
def get_posts(page_id: str):
    result = []
    for post in posts.find({"page_id": page_id}).limit(10):
        post["_id"] = str(post["_id"])
        result.append(post)
    return result

@router.get("/pages/{page_id}/employees")
def get_employees(page_id: str):
    result = []
    for emp in employees.find({"page_id": page_id}):
        emp["_id"] = str(emp["_id"])
        result.append(emp)
    return result
