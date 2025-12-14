def page_schema(page):
    return {
        "page_id": page.get("page_id"),
        "name": page.get("name"),
        "url": page.get("url"),
        "description": page.get("description"),
        "website": page.get("website"),
        "industry": page.get("industry"),
        "followers": page.get("followers"),
        "headcount": page.get("headcount"),
        "specialities": page.get("specialities"),
        "profile_image": page.get("profile_image")
    }

def post_schema(post):
    return {
        "page_id": post.get("page_id"),
        "content": post.get("content"),
        "likes": post.get("likes"),
        "comments": post.get("comments")
    }

def employee_schema(employee):
    return {
        "page_id": employee.get("page_id"),
        "name": employee.get("name"),
        "designation": employee.get("designation")
    }
