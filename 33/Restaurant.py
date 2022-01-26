class Restaurant:
    def __init__(self,a,b):
        self.restaurant_name=a
        self.cuisine_type=b
        self.number_served=0
    def describe_restaurant(self):
        print(f"Restaurant \"{self.restaurant_name}\" open!")
    def set_number_served(self,numb):
        self.number_served=numb
    def increment_number_served(self,numb2):
        self.number_served+=numb2
