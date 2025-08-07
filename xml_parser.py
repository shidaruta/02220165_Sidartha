import xml.etree.ElementTree as ET

xml_path = r"first.xml"

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


# insertBook("Advanced Systems", "John Doe", "2023", "1234567890")
# printBooks()
# deleteBook("Advanced Systems")
# printBooks()