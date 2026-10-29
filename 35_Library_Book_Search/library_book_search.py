books=[
    "Python Basics",
    "Learn Django",
    "JavaScript Guide",
    "Data Structure",
    "Aritificial Intelligence"
]
print("=== Library Book Search ===")
search=input("Enter a book name to search:").strip().lower()
found=False
for book in books:
    if search in book.lower():
        print("Book found:",book)
        found=True
if not found:
     print("Sorry, no matching book found.")