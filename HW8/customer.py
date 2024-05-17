
class Customer:
    
    def __init__(self,
                 customer_id: int,
                 name: str,
                 date_of_birth: str,
                 education: str,
                 address: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.education = education
        self.address = address
        
    def __str__(self) -> str:
        return f'''The {self.name} with {self.customer_id} ID, who born at {self.date_of_birth}
with {self.education} education with this {self.address} address.'''
    
    def __repr__(self) -> str:
        return f'''{type(self).__name__}, 
Customer ID: {self.customer_id}
Name: {self.name},
Birth Date: {self.date_of_birth}
Education: {self.education}
Address: {self.address}'''
    