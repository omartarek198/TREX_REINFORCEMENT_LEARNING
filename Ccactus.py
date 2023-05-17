from Cgame_object import GameObject
import random
class Cactus(GameObject):
    def __init__(self, sprites, position) -> None:
        super().__init__(sprites, position)
        self.cactus_path = random.choice(self.sprites)
     
        
    def GetCactusPath(self):
        return self.cactus_path
    
        