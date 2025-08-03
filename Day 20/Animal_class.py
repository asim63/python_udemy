class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, Exhale")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("Doing this under water")
    def swim(self):
        print("moving in water")
        

nemo = Fish()
nemo.swim()

dog = Animal()
dog.breathe()

print(nemo.num_eyes)
print(nemo.num_eyes)
nemo.breathe()