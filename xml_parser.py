import xml.etree.ElementTree as ET

xml_path = r"books.xml"

tree = ET.parse(xml_path)
root = tree.getroot()

def printBooks():
    print("Books in the XML:")
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        isbn= book.find('year').text

        print(f"Title: {title}\n Author: {author}\n Year: {year}\n ISBN:{isbn}")

def insertBook(title,author,year, isbn):
    new_book = ET.Element('book')
    ET.SubElement(new_book, 'title').text = title
    ET.SubElement(new_book, 'author').text = author
    ET.SubElement(new_book, 'year').text = year
    ET.SubElement(new_book, 'isbn').text = isbn
    root.append(new_book)
    tree.write(xml_path)
    print(f"Inserted new Book with \n Title:{title} \n Author:{author} \n Year: {year}\n ISBN: {isbn}" )


def deleteBook(title):
    del_title = title
    for book in root.findall('book'):
        if book.find('title').text == del_title:
            root.remove(book)
            print(f"Deleted book with \n Title:{del_title}")
            break
        
    print(f"Book with title {del_title} not found.")
    tree.write(xml_path)



programRunning = True
while programRunning is True:
    functionNo = input("Enter function number (1 for print, 2 for insert, 3 for delete, 4 to quit Menu): ")

    if functionNo == "1":
        printBooks()
    elif functionNo == "2":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")
        isbn = input("Enter book ISBN: ")
        insertBook(title, author, year, isbn)
    elif functionNo == "3":
        title = input("Enter book title to delete: ")
        deleteBook(title)   
    elif functionNo == "4":
        print("Exiting the program.")
        programRunning = False
    else:
        print("Invalid function number. Please enter 1, 2, or 3.")
