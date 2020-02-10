# uses class inheritance from the Chef Class. 

from Chef import Chef

class FrenchChef(Chef): 

  def make_special_dish(self): 
      print('the chef makes a souffle')

  def make_duck_confit(self):
    print('the chef makes duck confit.')