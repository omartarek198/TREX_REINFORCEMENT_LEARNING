import pygame
import sys
import math
import time
from Cdino import Dinosaur
from Ccactus import Cactus
from typing import List

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Pygame Full Screen")
        self.clock = pygame.time.Clock()
        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]
        self.i = 0
        self.scroll = 0
        self.dinos: List[Dinosaur] = []
        self.cacti: List[Cactus] = []
        
        self.track_level = self.screen_height * 2.8 / 4
        self.jump_cooldown = 0.50  # Cooldown duration in seconds
        self.last_jump_time = 0.0  # Time of the last jump

        self.MakeDino()
        self.MakeCactus()
        self.tick=0
        self.speed =12
    def run(self):
        self.clock.tick(60)  # Limit the frame rate to 60 FPS
        self.tick+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_time = time.time()
                    if current_time - self.last_jump_time > self.jump_cooldown:
                        self.dinos[0].jump()
                        self.last_jump_time = current_time
        if (self.tick>50):
            self.MakeCactus()
            self.tick = 0
        self.MoveDinos()
        self.MoveCacti()
        self.DrawScene()

    def DrawScene(self):
        self.screen.fill((255, 255, 255))
        self.Scroll()
        for dino in self.dinos:
            if dino.isjump:
                self.DrawObj(dino.GetCurrentJumpSprite(), dino.GetPosition())
            elif dino.isduck:
                pass
            else:
                self.DrawObj(dino.GetCurrentSpritePath(), dino.GetPosition())
        for cactus in self.cacti:
            self.DrawObj(cactus.GetCactusPath(), cactus.GetPosition())

        pygame.display.flip()

    def DrawObj(self, path_to_image, position):
        image = pygame.image.load(path_to_image)
        self.screen.blit(image, position)

    def MoveDinos(self):
        for dino in self.dinos:
            if dino.isjump:
                if dino.switch_index < dino.switch_rate / 2:
                    dino.Move((0, -15))
                else:
                    dino.Move((0, 15))
    def MoveCacti(self):
        for cactus in self.cacti:
            cactus.Move((self.speed*-1,0))

    def Scroll(self):
        bg = pygame.image.load("assets\Other\Track.png")
        tiles = math.ceil(self.screen_width / bg.get_width()) + 1
        self.i = 0

        while self.i < tiles:
            self.screen.blit(bg, (bg.get_width() * self.i + self.scroll, self.track_level))
            self.i += 1

        self.scroll -= self.speed
        if abs(self.scroll) > bg.get_width():
            self.scroll = 0

    def MakeDino(self):
        sprites = ["assets\Dino\DinoRun1.png", "assets\Dino\DinoRun2.png"]
        jumping_sprites = ["assets\Dino\DinoJump.png"]

        position = (30, self.track_level - 84)
        dino = Dinosaur(sprites, position, jumping_sprites)
        self.dinos.append(dino)
    def MakeCactus(self):
        sprites = ["assets\Cactus\LargeCactus1.png","assets\Cactus\LargeCactus2.png", "assets\Cactus\LargeCactus3.png", "assets\Cactus\SmallCactus1.png", "assets\Cactus\SmallCactus2.png","assets\Cactus\SmallCactus3.png"]
        position = (30, self.track_level - 84)
        cactu = Cactus(sprites,position)
        temp = pygame.image.load(cactu.cactus_path)
        cactu.position = (self.screen_width-100,self.track_level-temp.get_height()+10)
        self.cacti.append(cactu)