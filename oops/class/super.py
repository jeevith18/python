class Car:
    def __init__(self, company: str, model_year: int, color: str):
        self.company = company
        self.model_year = model_year
        self.color = color

'''
by setting None it becomes the default value for the variable
'''
class CarWithOptions(Car):
    def __init__(self, company: str, model_year: int, color: str, change_color_to: str = None):
        super().__init__(company, model_year, color)
        self.change_color_to = change_color_to
        if change_color_to:
            self.color = change_color_to

    def return_car_details_after_changing_color(self):
        return f'i own a car which belongs to {self.company} and it is of model {self.model_year} with color {self.color}'

car1 = CarWithOptions('Tata', 2025, 'Blue', "yellow")
print(car1.return_car_details_after_changing_color())
