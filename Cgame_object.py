
class GameObject:
    def __init__(self,sprites, position ) -> None:
        self.sprites = sprites
        self.position =position
        self.current_sprite_index = 0
        self.max_sprite_index = len(self.sprites)
        self.switch_rate = 10
        self.switch_index = 0
    def IsCollid(self,obj):
        pass
    def Move(self,vector2d):
        "receive the amount of change to be added to the current X and Y"
        self.position = tuple(a + b for a, b in zip(self.position, vector2d))
    def GetCurrentSpritePath(self):
         "returns current path"
         
         
         path = self.sprites[self.current_sprite_index]
         if self.switch_index == self.switch_rate:
                if self.current_sprite_index+1 == self.max_sprite_index:
                    self.current_sprite_index = 0
                else:
                     self.current_sprite_index+=1
                self.switch_index = 0
         else:
                self.switch_index+=1
                
      
         return path
     
    def GetPosition(self):
         "returns current position"
         return self.position
        
 