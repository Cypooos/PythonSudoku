import pygame
import sys


class GraphicalInterface():

  def __init__(self,game,**kwargs):
    self.windows = None
    self.game = game
    self.conf = kwargs
    self.h,self.w = self.conf.get("height",880),self.conf.get("width",800)
    self.ph,self.pw = self.h/(len(self.game.grid)+1),self.w/len(self.game.grid[0])
    print("Size: ",self.w,self.h,", Pad: ",self.pw,self.ph)
  
  def drawGrid(self):
    self.windows.fill(self.conf.get('line-color',(255,255,255)))
    x,y = 0,0
    for y,list_ in enumerate(self.game.grid):
      for x,ele in enumerate(list_):
        if ele.canBeWrite:pygame.draw.rect(self.windows, self.conf.get("back-color",(0,0,0)), (y*self.ph,x*self.pw,self.ph-2,self.pw-2))
        else:pygame.draw.rect(self.windows, self.conf.get("good-color",(0,0,50)), (y*self.ph,x*self.pw,self.ph-2,self.pw-2))
        if ele.number != self.game.default:
          txt = self.textFont.render(str(ele.number), True, self.conf.get("num-color",(255,200,255)))
          self.windows.blit(txt, (y*self.ph,x*self.pw))
  
  def drawNumbers(self):
    for x,num in enumerate(self.game.possibleNumbers):
      pygame.draw.rect(self.windows, self.conf.get("back-color",(0,0,0)), (len(self.game.grid)*self.pw,x*self.pw,self.ph,self.pw-2))
      txt = self.textFont.render(str(num), 1, self.conf.get("text-color",(100,200,200)))
      self.windows.blit(txt, (len(self.game.grid)*self.pw,x*self.pw))
  
  def click(self,pos,type_):
    if pos[0] >= (len(self.game.grid))*self.pw:
      self.select = int(pos[1] // self.pw)+1
      print(self.select)
    else:
      print(type_)
      select = None
      if type_ == 2: self.game.showAt(int(pos[0] // self.ph),int(pos[1] // self.pw))
      elif type_ == 1:select = self.select
      elif type_ == 3:select = self.game.default
      if select != None:
        self.game.play(int(pos[0] // self.ph),int(pos[1] // self.pw),select)
    if self.game.checkWin():
      print("WINNNNN")
      pygame.quit();sys.exit()

  def start(self):
    pygame.init()
    pygame.font.init()
    self.textFont = pygame.font.SysFont("monospace", int(self.ph))
    self.windows = pygame.display.set_mode((self.h,self.w))
    self.clock = pygame.time.Clock()
    self.select = self.game.default
    while True:
      self.drawGrid()
      self.drawNumbers()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          print("Ah le looser :D la réponse était",self.game.printWorking())
          pygame.quit();sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        self.click(pos,event.button)
      pygame.display.update()