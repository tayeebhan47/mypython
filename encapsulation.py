#encapsulation
class man:
    def __init__(self):
        self.name = 'name'   
        self.__age = 'age'
    def function(self):
      print(self.__age)
      print(self.name)
obj=man()
obj.name
obj.function() 
