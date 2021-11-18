from objects import Ingredient
from num_translate import num_translate

# 1
print(num_translate('Six'), end='\n\n')

# 2
carrot = Ingredient('Carrot', 100, 12)
print(f'Ingredient\n===========================================\nName: '
      f'{carrot.get_name()}\nWeight: {carrot.get_weight()}\nCost: {carrot.get_cost()}')
