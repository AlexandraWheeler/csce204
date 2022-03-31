FILE_NAME = "examples/march31/books.txt" #constant = all upper case because it wont be changed

# writing the file
def writeBooks(books):
    try:
        with open(FILE_NAME, "w") as file:
            for book in books:
                file.write(book + "\n")

    except FileNotFoundError:
        print("Book file not found.")

def readBooks():
    books = []
    try:
        with open(FILE_NAME) as file:
            for line in file:
                books.append(line.strip())
    except FileNotFoundError:
        print("Book file not found")

    return books

def displayBooks(books):
    print("Book List: ")
    num = 1
    for book in books:
        print(f"{num}. {book}")
        num += 1

def addBook(books):
    # get a book from user and add to the list
    book = input("Enter a book: ")
    books.append(book)
    print(f"{book} was successfully added")
    return books #return list with book added to it

def removeBook(books):
    # display book list
    displayBooks(books)

    #get book number to remove
    try:
        bookNum = int(input("Enter Book Number: ")) - 1
    except ValueError:
        print("Invalid Number")
        return books

    # error check
    if bookNum < 0 or bookNum >= len(books):
        print("Sorry, that number is not in the range of books")
        return books

    # delete book
    book = books.pop(bookNum)
    print(f"{book} was removed from the list.")
    return books

books = readBooks()

while True:
    command = input("(V)iew, (A)dd, (D)elete, or (Q)uit: ").strip().lower()
    if command == "q":
        break
    elif command == "a":
        addBook(books)
    elif command == "d":
        removeBook(books)
    elif command == "v":
        displayBooks(books)
    else:
        print("Invalid Command")

print("Goodbye")
writeBooks(books)




