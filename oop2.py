class Cars:
    def __init__(self,make,year,model,color):
        self.make=make
        self.year=year
        self.model=model
        self.color=color
    def display(self):
        print(f"my dream car is:{self.make}, manufactured in {self.year}the model is {self.model},its color is {self.color}")
myobj=Cars("Toyota","2022","Corrola LE","super white")
myobj.display()
myobj2=Cars("Audi","2021","Q5 Premium Plus","Navara blue mettalic")
myobj2.display()
myobj3=Cars("Tesla","2022","Model 3 Long Range","Midnight Silver Metalic")
myobj3.display()
myobj4=Cars("BMW","2023","330I sedan","alpine white")
myobj4.display()
myobj5=Cars("Chevrolet","2023","Silverado 1500 LTZ","black")
myobj5.display()