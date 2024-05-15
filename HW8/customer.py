
class Customer:
    
    def __init__(self, name: str,
                 date_of_birth: int,
                 education: str,
                 address: str) -> None:
        self.name = name
        self.date_of_birth = date_of_birth
        self.education = education
        self.address = address
        
    def __str__(self) -> str:
        return f'''The {self.name} who born at {self.date_of_birth}
    with {self.education} education with this {self.address} address.'''
    
    def __repr__(self) -> str:
        return f'''{type(self)}, Name: {self.name},
    Birth Date: {self.date_of_birth}
    Education: {self.education}
    Address: {self.address}'''
    