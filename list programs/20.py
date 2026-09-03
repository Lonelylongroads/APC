#Create a list of books. Implement:
#Add a new book
#Search a book
#Remove a book
#Display all books
#Count total books

books = []

books.append("Python")
books.append("Data Structures")
books.append("Web Development")

print(books)
search = "Data Structures"
if search in books:
    print(f"'{search}' found.")
else:
    print(f"'{search}' not found.")

print("Removing Web Development Book from the list...")
books.remove("Web Development")

print("All books:", books)
print("Total books:", len(books))

