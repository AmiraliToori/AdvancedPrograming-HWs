

class Book:
    
    def __init__(self,
                 book_id: int,
                 book_title: str,
                 publish_year: int,
                 publisher: str,
                 number_pages: str,
                 price: float) -> None:
        self.book_id = book_id
        self.book_title = book_title
        self.publish_year = publish_year
        self.publisher = publisher
        self.number_of_pages = number_pages
        self.price = price
        
    def __str__(self) -> str:
        return f'''{self.book_title} with {self.book_id} ID, which published in {self.publish_year},
by {self.publisher} have {self.number_of_pages}; you can buy it just only {self.price} dollars'''
     
     
    def __repr__(self) -> str:
        return f'''{type(self).__name__},
Book ID: {self.book_id}
Title: {self.book_title},
Publish year: {self.publish_year},
Publisher: {self.publisher},
Number of pages: {self.number_of_pages},
Price: {self.price}'''