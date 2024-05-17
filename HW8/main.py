from customer import Customer
from book import Book
from buy import Buy

import sqlite3


customer_1 = Customer(1, 'Amirali Toori', "2003-10-01", "bachelor", "Ilam")
customer_2 = Customer(2, 'Amirmahdi Abravesh', "2002-02-02", "PhD", "Karaj")
customer_3 = Customer(3, 'Mohammad Hosseini', "2002-1-1", "PhD", "Borujerd")


book_1 = Book(1522, 'Moby Dick', 1851, 'Harper and Brothers', 635, 20)
book_2 = Book(1523, 'To kill a mocking bird',1960, 'HarperCollins', 350, 13.75)
book_3 = Book(1524, 'Midnight Library', 2020, 'Canongate Books', 372, 15)
book_4 = Book(1525, 'David Copperfield', 1849, 'Bradbury & Evans', 482, 6)
book_5 = Book(1526, 'Oliver Twist', 1838, 'Richard Bentley', 608, 9)

buy_1 = Buy(1523, 1, "2023-10-2", 1)
buy_2 = Buy(1522, 1, "2023-10-2", 1)
buy_3 = Buy(1524, 3, "2022-10-10", 2)
buy_4 = Buy(1525, 2, "2023-2-2", 3)
buy_5 = Buy(1526, 3, "2021-02-01", 1)
buy_6 = Buy(1522, 1, "2022-01-02", 1)
buy_7 = Buy(1522, 2, "2020-02-01", 1)


connect = sqlite3.connect('Bookstore.db')

c = connect.cursor()


def create_customer_table() -> None:
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Customers( 
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                date_of_birth INTEGER,
                education TEXT, 
                address TEXT)''')


def create_book_table() -> None:
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY,
            book_title TEXT NOT NULL,
            publish_year INT NOT NULL,
            publisher TEXT NOT NULL,
            number_of_pages INTEGER NOT NULL,
            PRICE REAL NOT NULL) ''')


def create_buy_table() -> None:
    with connect:
        c.execute('''CREATE TABLE IF NOT EXISTS Buy (
            book_id INTEGER,
            customer_id INTEGER,
            date INTEGER,
            count INTEGER,
            FOREIGN KEY(book_id) REFERENCES Books(book_id),
            FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)) ''')




# Create
create_book_table()
create_customer_table()
create_buy_table()


def drop_books() -> None:
    with connect:
        c.execute('''DROP TABLE Books''')


def drop_customers() -> None:
    with connect:
        c.execute('''DROP TABLE Customers''')


def drop_buy() -> None:
    with connect:
        c.execute('''DROP TABLE Buy''')


# Drop
# drop_customers()
# drop_books()
# drop_buy()


def insert_customers(customer: Customer) -> None:
    with connect:
        c.execute('''INSERT INTO Customers VALUES
                (:customer_id,
                :customer_name,
                :date_of_birth,
                :education,
                :address) ''',
                  {'customer_id': customer.customer_id,
                   'customer_name': customer.name,
                   'date_of_birth': customer.date_of_birth,
                   'education': customer.education,
                   'address': customer.address})


def insert_books(book: Book) -> None:
    with connect:
        c.execute('''INSERT INTO Books VALUES
                  (:book_id,
                  :book_title,
                  :publish_year,
                  :publisher,
                  :number_of_pages,
                  :price)''', {'book_id': book.book_id,
                               'book_title': book.book_title,
                               'publish_year': book.publish_year,
                               'publisher': book.publisher,
                               'number_of_pages': book.number_of_pages,
                               'price': book.price})


def insert_buy(buy: Buy) -> None:
    with connect:
        c.execute('''INSERT INTO Buy VALUES(
                  :book_id,
                  :customer_id,
                  :date,
                  :count)''',
                  {'book_id': buy.book_id,
                   'customer_id': buy.customer_id,
                   'date': buy.date,
                   'count': buy.count})


# Insertion
insert_customers(customer_1)
insert_customers(customer_2)
insert_customers(customer_3)

insert_books(book_1)
insert_books(book_2)
insert_books(book_3)
insert_books(book_4)
insert_books(book_5)

insert_buy(buy_1)
insert_buy(buy_2)
insert_buy(buy_3)
insert_buy(buy_4)
insert_buy(buy_5)
insert_buy(buy_6)
insert_buy(buy_7)


def read_customers(customer: Customer) -> None:
    with connect:
        c.execute('''SELECT * FROM Customers
                  WHERE Customers.customer_id == :value''', {"value": customer.customer_id})
        print(c.fetchone())


def read_books(book: Book) -> None:
    with connect:
        c.execute('''SELECT * FROM Books
                  WHERE Books.book_id == :value''', {"value": book.book_id})
        print(c.fetchone())


def read_buy(customer: Customer) -> None:
    with connect:
        c.execute('''SELECT * FROM Buy
                  WHERE Buy.customer_id == :value''', {"value": customer.customer_id})
        print(c.fetchall())

# Read
# read_customers(customer_3)
# read_books(book_2)
# read_buy(customer_1)


def delete_from_customers(customer: Customer) -> None:
    with connect:
        c.execute('''DELETE FROM Customers
                  WHERE Customer.customer_id == :value ''', {"value": customer.customer_id})


def delete_from_books(book: Book) -> None:
    with connect:
        c.execute('''DELETE FROM Books
                  WHERE Books.book_id == :value ''', {"value": book.book_id})


def delete_from_buy(buy: Buy) -> None:
    with connect:
        c.execute('''DELETE FROM Buy
                  WHERE Buy.customer_id == :value''', {"value": buy.customer_id})

# Delete
# delete_customers(customer_1)
# delete_books(book_3)

def update_customer(customer: Customer,
                    name: str,
                    date_of_birth: str,
                    education: str,
                    address: str) -> None:
    if name is None:
        name = customer.name
    if date_of_birth is None:
        date_of_birth = customer.date_of_birth
    if education is None:
        education = customer.education
    if address is None:
        address = customer.address

    with connect:
        c.execute('''UPDATE Customers
                  SET name = :name,
                  date_of_birth = :date_of_birth,
                  education = :education,
                  address = :address
                  WHERE customer_id == :value ''', {"name": name,
                                                    "date_of_birth": date_of_birth,
                                                    "education": education,
                                                    "address": address,
                                                    "value": customer.customer_id
                                                    })


def update_book(book: Book,
                 book_title: str,
                 publish_year: int,
                 publisher: str,
                 number_of_pages: int,
                 price: float) -> None:
    if book_title is None:
        book_title = book.book_title
    if publish_year is None:
        publish_year = book.publish_year
    if publisher is None:
        publisher = book.publish_year
    if number_of_pages is None:
        number_of_pages = book.number_of_pages
    if price is None:
        price = book.price
        
    with connect:
        c.execute('''UPDATE Books
                SET book_title = :book_title,
                publish_year = :publish_year,
                publisher = :publisher,
                number_of_pages = :number_of_pages,
                price = :price
                WHERE book_id == :value''',{"book_title": book_title,
                                                "publish_year": publish_year,
                                                "publisher": publisher,
                                                "number_of_pages": number_of_pages,
                                                "price": price,
                                                "value": book.book_id})

def update_buy(buy: Buy,
               customer_id: int,
               book_id: int,
               date: str) -> None:
    if book_id is None:
        book_id = buy.book_id
    if customer_id is None:
        customer_id = buy.customer_id
    if date is None:
        date = buy.date
        
    with connect:
        c.execute('''UPDATE Buy
                  SET customer_id = :customer_id,
                  book_id = :book_id,
                  date = :date
                  WHERE Buy.customer_id == :value''', {"customer_id": customer_id,
                                    "book_id": book_id,
                                    "date": date,
                                    "value": buy.customer_id})

# Update
# update_customer(customer_1,'Reza Ebrahimi', None, None, None)
# update_book(book_2, 'Amirali Toori', None, None, None, None)
# update_buy(buy_3, 111111, 121212, None)




connect.close()


# print(str(book_1))
# print(repr(book_1))

# print(str(customer_1))
# print(repr(customer_1))
