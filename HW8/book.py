

class Book:
    
    def __init__(self, book_title: str,
                 publish_year: int,
                 publisher: str,
                 number_pages: str,
                 price: int) -> None:
        self.book_title = book_title
        self.publish_year = publish_year
        self.publisher = publisher
        self.number_pages = number_pages
        self.price = price
        
    def __str__(self) -> str:
        return f'''The {self.book_title} which published in {self.publish_year},
     by {self.publisher} have {self.number_pages}; you can buy it just only {self.price} dollars'''
     
     
    def __repr__(self) -> str:
        return f'''{type(self)} Title: {self.book_title}, Publish year: {self.publish_year}
    Publisher: {self.publisher}, Number of pages: {self.number_pages}, Price: {self.price}'''