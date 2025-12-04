class Animatronic: 
    def __init__(self, name):
        self.name = name
        
    def perform(self):
        print(f"It's Showtime! {self.name} is performing")
        
    def wander(self):
        print(f"{self.name} is wandering")
        
    def attack(self):
        print(f"{self.name} has attacked you!")
        
class Office:
    def __init__(self, tool):
        self.tool = tool
        def use_tool(self):
            print(f"Using {self.tool} to defend yourself")
            
class SecurityGuard:
    def __init__(self, guard):
        self.guard = guard
        
        
        

class Game:
    freddy = Animatronic("Freddy Fazbear")
    bonnie = Animatronic("Bonnie")
    chica = Animatronic("Chica")
    foxy = Animatronic("Foxy")


