from customer import Customer
from book import Book
import sqlite3


customer_1 = Customer("Amirali Toori", 2003-10-1, "bachelor", "Ilam")
customer_2 = Customer("Amirmahdi Abravesh", 2002-2-2, "PhD", "Karaj" )
customer_3 = Customer("Mohammad Hosseini", 2002-1-1, "PhD", "Borujerd")


book_1 = Book("Moby Dick", 1851, "Harper and Brothers", 635, 20)
book_2 = Book("To kill a mocking bird", 1960, "HarperCollins",350, 13.75)
book_3 = Book("Midnight Library", 2020, "Canongate Books", 372, 15)
book_4 = Book("David Copperfield", 1849, "Bradbury & Evans", 482, 6)
book_5 = Book("Oliver Twist", 1838, "Richard Bentley", 608, 9)


customer_table = [customer_1, customer_2, customer_3]
book_table = [book_1, book_2, book_3, book_4, book_5]
