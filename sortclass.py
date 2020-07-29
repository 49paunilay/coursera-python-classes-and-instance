class Fruit():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def sort_priority(self):
        return self.price
    
FruitList=[Fruit('Cherry',10),Fruit('Apple',5),Fruit('Blueberry',20)]
for fruit in sorted(FruitList,key=Fruit.sort_priority):
    print(fruit.name)

