class AppleBasket():
    def __init__(self,apple_color,apple_quantity):
        self.apple_color=apple_color
        self.apple_quantity=apple_quantity
    def increase(self):
        self.apple_quantity=self.apple_quantity+1
    def __str__(self):
        return 'A basket of {quantity} {color} apples.'.format(quantity=self.apple_quantity,color=self.apple_color)

#apple1=AppleBasket('red',1)
#apple1.increase()
#print(apple1)