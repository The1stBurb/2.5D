from time import sleep
from random import randint,choice
import pygame
pygame.init()
X = 1000
Y = 1000
scrn = pygame.display.set_mode((X, Y))#,pygame.FULLSCREEN)
clk=pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont(None, 20)
class pygameBases:
    def __init__(self):
        pass
    def colorize(self,image, new_color):
        tinted = pygame.Surface(image.get_size(), pygame.SRCALPHA)
        tinted.fill(new_color)
        tinted.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted
    def resize(self,img,w,h):
        return pygame.transform.scale(img,(w,h))
    def rot90(self,img,r=-1):
        if r==-1:
            r=randint(0,3)*90
        return pygame.transform.rotate(img,r)
    def rect(self,x,y,w,h,col=(255,255,255)):
        # print(col)
        pygame.draw.rect(scrn, col, pygame.Rect(x, y, w, h))
    def text(self,txt,x,y,col=(0,0,0)):
        scrn.blit(font.render(txt, True, col),(x,y))
    def quad(self,x1,y1,x2,y2,x3,y3,x4,y4,col=(255,255,255)):
        pygame.draw.polygon(scrn, col, [(x1,y1),(x2,y2),(x3,y3),(x4,y4),])
    def image(self,img,x,y):
        scrn.blit(img,(x,y))
    def gitImg(self,path):
        return pygame.image.load(path).convert_alpha()
    def imgGit(self,path,w,h):
        return self.resize(self.gitImg(path),(w,h))

while True:
    scrn.fill((200,200,200))
    # mbt=1
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            # print(clickclack)
            quit()