
from Cgame_object import GameObject
class Dinosaur(GameObject):
   def __init__(self,sprites, position,jumping_sprites):
        super().__init__(sprites, position)
        self.jumping_sprites = jumping_sprites
        self.isjump = False
        self.isjumpUp = False
        self.isjumpDown = False
        self.max_jump_sprite = len(jumping_sprites)
        self.isduck = False
   def jump(self):
       "starts jump animation"
       print("SET TO TRUE")
       self.isjump = True
       self.current_sprite_index= 0
       self.switch_index = 0
       self.switch_rate = 30
       
   def GetCurrentJumpSprite(self):
         "returns current path"
         
         
         path = self.jumping_sprites[self.current_sprite_index]
         if self.switch_index+1 == self.switch_rate:
                    self.current_sprite_index = 0
                    self.isjump= False
                    self.switch_rate = 10
                    self.switch_index = 0
                    self.isjumpDown = False
      
                
                        
         self.switch_index+=1                     
            
                
      
         return path
        
    
