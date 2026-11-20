# Library management system using OOP
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append({"title": title, "available": True})
        print("Book added.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        for number, book in enumerate(self.books, start=1):
            status = "Available" if book["available"] else "Issued"
            print(f"{number}. {book['title']} - {status}")

    def issue_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and book["available"]:
                book["available"] = False
                print("Book issued.")
                return
        print("Book not found or already issued.")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["available"]:
                book["available"] = True
                print("Book returned.")
                return
        print("No matching issued book found.")

library = Library()

while True:
    print("\\n1. Add book  2. View books  3. Issue book  4. Return book  5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        library.add_book(input("Book title: ").strip())
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.issue_book(input("Title to issue: ").strip())
    elif choice == "4":
        library.return_book(input("Title to return: ").strip())
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
