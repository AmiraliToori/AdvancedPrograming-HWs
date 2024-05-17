

class AverageAnnualPrecipitation:
    
    def __init__(self,
                 values: tuple) -> None:
        self.values = values # m lit 
        
    def __str__(self) -> str:
        return f'''the amount of precipitation
per month in one year is: {self.values} in ml.'''
                    
    def __repr__(self) -> str:
        return f'''{type(self).__name__}, values: {self.values} '''
    
    def add(self, new_value: int) -> None:
        temp_lst = [new_value]
        [temp_lst.append(value) for value in self.values[0:11]]
        self.values = tuple(temp_lst)
    
    def average(self) -> float:
        total = 0
        for value in self.values:
            total += value
        
        return f"The average annual precipitation is: {round(total / 12, 2)}ml"
    
    
    
if __name__ == "__main__":
    
    per_month_values = (100, 220, 230, 500, 550, 600, 300, 280, 110, 300, 200, 320)

    year_1 = AverageAnnualPrecipitation(per_month_values)


    print(str(year_1))
    print(repr(year_1))

    # print(year_1.average())


    # year_1.add(100)

    # print(str(year_1))

    # print(year_1.average())
    
        