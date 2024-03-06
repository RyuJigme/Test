# Initialize empty lists, set and dictionary
books_list = []
authors_set = set()
books_dict = {}

# Add books
books_list.append("Python programming")
authors_set.add("John Smith")
books_dict["Python programming"] = "John Smith"

books_list.append("Data Structures and Alogorithms")
authors_set.add("Jane Doe")
books_dict["Data Structures and Alogorithms"] = "Jane Doe"

books_list.append("Machine learning basics")
authors_set.add("Alice Johnson")
books_dict["Machine learning basics"] = "Alice Johnson"

#search for books 
search_title = input ("Enter the title of the book to search:")
if search_title in books_list:
    print(f"Book found! Author : {books_dict[search_title]}")
else:
    print("Book not found!")

#Display all books 
print("List of books:")
for book in books_list:
    print(book)

#remove a book
remove_title = input("Enter the title of the book to remove or else enter to skip:")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
    print("Books available : ",books_list)

else:
    print("Book not found!")
