from appliances import DishWasher
from appliances import Dryer
from appliances import Washer
from appliances import CoffeeMaker
from appliances import CanOpener
from appliances import Stove
from appliances import Refrigerator

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_washer.wash_clothes()

samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes()

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

mr_can_opener = CanOpener("blue")
mr_can_opener.open_can()

new_stove = Stove("black")
new_stove.make_coffee()