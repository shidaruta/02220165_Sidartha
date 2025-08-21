import json 
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None
    
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            
            return data
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return None
        
def print_books(data):
    if not data:
        print("No data to display.")
        return
    
    print("Books in the JSON:")
    for book in data:
        title = book.get('title', 'Unknown Title')
        author = book.get('author', 'Unknown Author')
        year = book.get('year', 'Unknown Year')
        isbn = book.get('isbn', 'Unknown ISBN')

        print(f"Title: {title}\nAuthor: {author}\nYear: {year}\nISBN: {isbn}\n")


def insert_book(file_path, title, author, year, isbn):
    data = read_json_file(file_path)
    if data is None:
        print("No data to insert into.")
        return
    
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn" : isbn 
        }
    data.append(new_book)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def delete_book(file_path, title):
    data = read_json_file(file_path)
    if data is None:
        print("No data to delete from.")
        return
    
    for book in data:
        if book.get('title') == title:
            data.remove(book)
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Deleted book with title: {title}")
            return
    
    print(f"Book with title {title} not found.")

def edit_book(file_path, old_title, new_title, author, year, isbn):
    data = read_json_file(file_path)
    if data is None:
        print("No data to edit on")
    
    for book in data:
        if book.get('title') == old_title:
            book['title'] = new_title or old_title
            book['author'] = author or book['author']
            book['year'] = year or book['year']
            book['isbn'] = isbn or book['isbn']
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Edited book with title: {old_title} to {new_title}")




file_path = "lab_2/book.json"
play = True

while play is True:
    data = read_json_file(file_path)
    funcNo = input(f"Enter function number (\n 1 for print,\n 2 for insert,\n 3 for delete,\n 4 to edit,\n 5 to quit Menu):\n ")
    
    match funcNo:
        case "1":
            print_books(data)
        case "2":
            title = input("Enter  book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            isbn = input("Enter book ISBN: ")
            insert_book(file_path, title, author, year, isbn)
        case "3":
            title = input("Enter book title to delete: ")
            delete_book(file_path, title)
        case "4":
            old_title = input("Enter book title to edit: ")
            new_title = input("Enter new book title (leave blank to keep current): ")
            author = input("Enter new book author (leave blank to keep current): ")
            year = input("Enter new book year (leave blank to keep current): ")
            isbn = input("Enter new book ISBN (leave blank to keep current): ")
            edit_book(file_path, old_title, new_title, author, year, isbn)
        case "5":
            print("Exiting the program.")
            play = False