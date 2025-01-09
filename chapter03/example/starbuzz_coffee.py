from chapter03.example.beverage import Beverage
from chapter03.example.espresso import Espresso
from chapter03.example.house_blend import HouseBlend
from chapter03.example.mocha import Mocha


class StarbuzzCoffee:
    beverage: Beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")
    
    beverage3: Beverage = HouseBlend()
    beverage3 = Mocha(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")
