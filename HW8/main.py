from customer import Customer
from book import Book
from buy import Buy

import sqlite3


customer_1 = Customer(1, 'Amirali Toori', '2003-10-01', "bachelor", "Ilam")
customer_2 = Customer(2, 'Amirmahdi Abravesh', '2002-02-02', "PhD", "Karaj")
customer_3 = Customer(3, 'Mohammad Hosseini', '2002-1-1', "PhD", "Borujerd")


book_1 = Book(1522, 'Moby Dick', 1851, 'Harper and Brothers', 635, 20)
book_2 = Book(1523, 'To kill a mocking bird',1960, 'HarperCollins', 350, 13.75)
book_3 = Book(1524, 'Midnight Library', 2020, 'Canongate Books', 372, 15)
book_4 = Book(1525, 'David Copperfield', 1849, 'Bradbury & Evans', 482, 6)
book_5 = Book(1526, 'Oliver Twist', 1838, 'Richard Bentley', 608, 9)

buy_1 = Buy(1523, 1, '2023-10-02', 1)
buy_2 = Buy(1522, 1, '2023-10-02', 1)
buy_3 = Buy(1524, 3, '2022-10-10', 2)
buy_4 = Buy(1525, 2, '2023-02-02', 3)
buy_5 = Buy(1526, 3, '2021-02-02', 1)
buy_6 = Buy(1522, 1, '2022-01-02', 1)
buy_7 = Buy(1522, 2, '2020-02-01', 1)


connect = sqlite3.connect('Bookstore.db')

c = connect.cursor()


with connect:
    c.execute("PRAGMA foreign_keys = ON")

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
            FOREIGN KEY (book_id) REFERENCES Books (book_id) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (customer_id) REFERENCES Customers (customer_id) ON DELETE SET NULL ON UPDATE CASCADE)''')




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



# a
def count_of_buy_for_customer(customer: Customer,
                  date1: str,
                  date2: str) -> None:
    
    with connect:
        c.execute('''SELECT Customers.customer_id, Customers.name, COUNT(*) FROM 
                  Customers INNER JOIN Buy ON
                  Customers.customer_id == Buy.customer_id 
                  WHERE
                  :customer_id == Buy.customer_id AND 
                  buy.date BETWEEN :date1 AND :date2
                  GROUP BY Customers.customer_id, Customers.name'''
                  ,
                  {"customer_id": customer.customer_id,
                   "date1": date1,
                   "date2": date2})
        
        print(c.fetchone())

# count_of_buy_for_customer(customer_2,'2019-01-01', '2024-01-01')
# count_of_buy_for_customer(customer_1, '2022-01-01', '2022-01-05')

# b
def sell_of_every_books(date1: str, date2: str):
    with connect:
        c.execute('''SELECT Books.book_id, Books.book_title, SUM(buy.count) FROM
                  Books INNER JOIN Buy 
                  ON Books.book_id == buy.book_id
                  WHERE buy.date BETWEEN :date1 AND :date2
                  GROUP BY Books.book_id, Books.book_title''',
                  {"date1": date1, "date2": date2})
        results = c.fetchall()
        for row in results:
            print(row)
    
# sell_of_every_books('2015-01-01', '2024-01-01')

# c
def sell_of_store(date1: str, date2: str):
    with connect:
        c.execute('''SELECT SUM(buy.count) AS Purchase_count FROM
                  Buy 
                  WHERE date BETWEEN :date1 AND :date2''',
                  {"date1": date1, "date2": date2 })
        print(c.fetchone())
        
# sell_of_store('2015-01-01', '2024-01-01')

# d
def books_list():
    with connect:
        c.execute('''SELECT * FROM Books''')
    results = c.fetchall()
    for row in results:
        print(row)

# books_list()

# e
def customers_list():
    with connect:
        c.execute('''SELECT * FROM Customers''')
    results = c.fetchall()
    for row in results:
        print(row)

# customers_list()


# f
def search_customers(customer: Customer) -> None:
    with connect:
        c.execute('''SELECT * FROM Customers
                  WHERE Customers.customer_id == :value''', {"value": customer.customer_id})
        print(c.fetchone())


def search_books(book: Book) -> None:
    with connect:
        c.execute('''SELECT * FROM Books
                  WHERE Books.book_id == :value''', {"value": book.book_id})
        print(c.fetchone())

# search_customers(customer_3)
# search_books(book_2)

# g
def delete_from_customers(customer: Customer) -> None:
    with connect:
        c.execute('''DELETE FROM Customers
                  WHERE Customers.customer_id == :value ''', {"value": customer.customer_id})


def delete_from_books(book: Book) -> None:
    with connect:
        c.execute('''DELETE FROM Books
                  WHERE Books.book_id == :value ''', {"value": book.book_id})


def delete_from_buy(buy: Buy) -> None:
    with connect:
        c.execute('''DELETE FROM Buy
                  WHERE Buy.customer_id == :value''', {"value": buy.customer_id})

# Delete
# delete_from_customers(customer_1)
# delete_from_customers(customer_2)
# delete_from_books(book_3)

# h
def update_customer(customer: Customer,
                    customer_id: int,
                    name: str,
                    date_of_birth: str,
                    education: str,
                    address: str) -> None:
    if customer_id is None:
        customer_id = customer.customer_id
    if name is None:
        name = customer.name

    with connect:
        c.execute('''UPDATE Customers
                  SET customer_id = :customer_id,
                  name = :name,
                  date_of_birth = :date_of_birth,
                  education = :education,
                  address = :address
                  WHERE customer_id == :value ''', {"customer_id": customer_id,
                                                    "name": name,
                                                    "date_of_birth": date_of_birth,
                                                    "education": education,
                                                    "address": address,
                                                    "value": customer.customer_id
                                                    })


def update_book(book: Book,
                book_id: int,
                book_title: str,
                publish_year: int,
                publisher: str,
                number_of_pages: int,
                price: float) -> None:
    if book_id is None:
        book_id = book.book_id
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
                SET book_id = :book_id,
                book_title = :book_title,
                publish_year = :publish_year,
                publisher = :publisher,
                number_of_pages = :number_of_pages,
                price = :price
                WHERE book_id == :value''',{"book_id": book_id,
                                                "book_title": book_title,
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


# update_customer(customer_1, 5,'Reza Ebrahimi', None, None, None)
# update_book(book_2, 1528, 'Amirali Toori', None, None, None, None)
# update_buy(buy_3, 111111, 121212, None)

# i
def buy_per_day():
    with connect:
        c.execute('''SELECT * FROM Buy
                  GROUP BY Buy.date''')
    results = c.fetchall()
    for row in results:
        print(row)

# buy_per_day()


connect.close()


# print(str(book_1))
# print(repr(book_1))

# print(str(customer_1))
# print(repr(customer_1))
