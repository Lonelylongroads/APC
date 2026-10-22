books = [
    {"id": "1", "title": "Python", "author": "Guido", "status": "Available"},
    {"id": "2", "title": "Java", "author": "Gosling", "status": "Available"}
]

def add_book(b_id, title, author):
    books.append({"id": b_id, "title": title, "author": author, "status": "Available"})

def search_book(title):
    for b in books:
        if b["title"].lower() == title.lower():
            return b
    return None

def issue_book(b_id):
    for b in books:
        if b["id"] == b_id and b["status"] == "Available":
            b["status"] = "Issued"
            return True
    return False

def return_book(b_id):
    for b in books:
        if b["id"] == b_id and b["status"] == "Issued":
            b["status"] = "Available"
            return True
    return False

def display_available():
    for b in books:
        if b["status"] == "Available":
            print(b)