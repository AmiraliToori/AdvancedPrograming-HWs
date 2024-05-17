

class Buy:
    
    def __init__(self,
                 book_id: int,
                 customer_id: int,
                 date: str,
                 count: int) -> None:
        self.book_id = book_id
        self.customer_id = customer_id
        self.date = date
        self.count = count
        
        
    def __str__(self) -> str:
        return f'''Customer {self.customer_id} bought {self.count} this {self.book_id} book, at {self.date}.'''
    
    def __repr__(self) -> str:
        return f'''{type(self).__name__},
Book ID: {self.book_id},
Customer ID: {self.customer_id},
Date: {self.date}
Count: {self.count}'''
        