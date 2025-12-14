import requests
from bs4 import BeautifulSoup

def scrape_page(page_id):
    url = f"https://www.linkedin.com/company/{page_id}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text if soup.title else page_id

    return {
        "page_id": page_id,
        "name": title,
        "url": url,
        "description": "",
        "website": "",
        "industry": "",
        "followers": 0,
        "headcount": 0,
        "specialities": [],
        "profile_image": ""
    }

def scrape_posts(page_id):
    data = []
    for i in range(10):
        data.append({
            "page_id": page_id,
            "content": f"Sample post {i+1}",
            "likes": 0,
            "comments": []
        })
    return data

def scrape_employees(page_id):
    data = []
    for i in range(5):
        data.append({
            "page_id": page_id,
            "name": f"Employee {i+1}",
            "designation": "Software Engineer"
        })
    return data
