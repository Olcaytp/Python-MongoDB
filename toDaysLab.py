import pymongo

#Establish connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Create or select database
mydb = client["lexicondb"]

#Create or select a collection in the database
mycol = mydb["books"]

def add_book():
    print("--- Add a Book ---")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    book = {"title": title, "author": author, "price": price, "stock": stock}
    result = mycol.insert_one(book)
    print("Book added successfully with ID:", result.inserted_id)

def view_all_books():
    print("--- All Books ---")
    for book in mycol.find():
        print(book)

def search_book_by_title():
    print("--- Search Book by Title ---")
    title = input("Enter book title: ")
    result = mycol.find_one({"title": title})
    if result:
        print(result)
    else:
        print("Book not found!")

def update_book():
    print("--- Update a Book Price ---")
    title = input("Enter the title of the book you want to update: ")
    new_price = float(input("Enter the new price: "))
    result = mycol.update_one({"title": title}, {"$set": {"price": new_price}})
    if result.modified_count > 0:
        print("Book price updated successfully!")
    else:
        print("Book not found or price not updated.")
    
def delete_book():
    print("--- Delete a Book ---")
    title = input("Enter the title of the book you want to delete: ")
    result = mycol.delete_one({"title": title})
    if result.deleted_count > 0:
        print("Book deleted successfully!")
    else:
        print("Book not found or not deleted.")

def view_books_by_author():
    print("--- View Books by Author ---")
    author = input("Enter the name of the author: ")
    books = mycol.find({"author": author})
    if books:
        for book in books:
            print(book)
    else:
        print("No author found!")

def view_books_in_stock():
    print("--- View Books in Stock ---")
    books_cursor = mycol.find({"stock": {"$gt": 0}})
    books = list(books_cursor)
    book_count = len(books)
    if book_count:
        print("Total number of books:", book_count)
    else:
        print("No books are currently in stock.")


def main():
    print("--- Hello and welcome to the awesome Lexicon bookstore! ---")
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search a book by title")
        print("4. Update a book price")
        print("5. Delete a book")
        print("6. View books by author")
        print("7. View books in stock")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_book_by_title()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            view_books_by_author()
        elif choice == "7":
            view_books_in_stock()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
