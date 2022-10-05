"""class Learning"""   
class Dog:
    
    tricks = []
    
    # kind = 'canine'
    
    def __init__(self,name):
        self.name = name
     
    def add_tricks(self,trick):
        self.tricks.append(trick)    
d = Dog('Fido') 
e = Dog('Buddy')        
d.add_tricks('roll over') 
e.add_tricks('play dead') 
# print(d.kind)
print(d.name)
# print(e.kind)
print(e.name)
print(d.tricks)
print(e.tricks)