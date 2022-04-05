class Product:
    def __init__(self, title, description,price):
        self.title = title
        self.description = description
        self.price = price

    def getTotal(self):
        return int(self.price * 1.07)
        
    def display(self):
        print(f"""
        {self.title}
        Description = {self.description}
        Price = {self.getTotal()}
        """)
    
