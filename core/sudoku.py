import random

def checkDup(list_):
  for ele in list_:
    if list_.count(ele) > 1:return True
  return False

class Number():
  def __init__(self,canBeWrite,number):
    self.canBeWrite = canBeWrite
    self.number = number
  def __str__(self):
    return str(self.number)
  def __repr__(self):
    return self.__str__()

class Sudoku():

  ENSEMBLES = None

  def resetGrid(self):
    self.grid = []
    for x in range(9):
      temp = []
      for y in range(9):
        temp.append(Number(True,self.default))
      self.grid.append(temp)
  
  def resetWorkingGrid(self):
    self.workingGrid = []
    for x in range(9):
      temp = []
      for y in range(9):
        temp.append(Number(False,self.default))
      self.workingGrid.append(temp)

  def generate(self):
    self.resetGrid()
    self.resetWorkingGrid()
    nums = [1,2,3,4,5,6,7,8,9]
    random.shuffle(nums)
    start_of = [0,1,2,3,4,5,6,7,8]
    random.shuffle(start_of)
    ofx_x = random.choice([1,2])
    ofx_y = random.choice([1,2])
    ofy_y = random.choice([1,2])
    ofy_x = random.choice([1,2])
    for n in range(9):
      anum = nums[n];asofx = start_of[n]//3;asofy = start_of[n]%3
      for y in range(0,3):
        for x in range(0,3):
          self.workingGrid[ y*3 + (asofx+(ofx_y*y + ofx_x*x)%3)%3][ x*3 + (asofy+(ofy_y*y + ofy_x*x)%3)%3].number = anum
    posX,posY = [0,1,2,3,4,5,6,7,8].copy(),[0,1,2,3,4,5,6,7,8].copy()
    random.shuffle(posX);random.shuffle(posY)
    for n in range(len(posX)):self.grid[posX[n]][posY[n]] = Number(False,self.workingGrid[posX[n]][posY[n]].number)
    return self.workingGrid

  

  def __init__(self,player):
    self.player = player
    self.possibleNumbers = [1,2,3,4,5,6,7,8,9]
    self.default = -1
    self.grid = []
    self.workingGrid = []
    self.generate()
    if self.ENSEMBLES == None:
      self.ENSEMBLES = []
      for x in range(9):
        temp1 = [].copy()
        temp2 = [].copy()
        for y in range(9):
          temp1.append([x,y])
          temp2.append([y,x])
        self.ENSEMBLES.append(temp1)
        self.ENSEMBLES.append(temp2)
      for Bx in range(3):
        temp3 = [].copy()
        for By in range(3):
          self.ENSEMBLES.append([
            [By*3,Bx*3],[By*3,Bx*3+1],[By*3,Bx*3+2],
            [By*3+1,Bx*3],[By*3+1,Bx*3+1],[By*3+1,Bx*3+2],
            [By*3+2,Bx*3],[By*3+2,Bx*3+1],[By*3+2,Bx*3+2],
          ])
    print("data = \n",self)
    print("\n\nEnsembles = \n",self.ENSEMBLES)

  def checkWin(self):
    for x_ in range(9):
      if self.default in [x.number for x in self.grid[x_]]:
        print("Not all cases filled.");return False
    for group in self.ENSEMBLES:
      eles = [str(self.grid[ele[1]][ele[0]]) for ele in group]
      if checkDup(eles):
        print("countain duplicate:",eles);return False
    return True
  
  def __str__(self):
    ret = '['
    for x in self.grid:
      ret += "  ["
      for y in x:
        ret +=str(y)+", "
      ret +="],\n"
    return ret + "]"

  def printWorking(self):
    ret = '\n['
    for x in self.workingGrid:
      ret += "  ["
      for y in x:
        ret +=str(y)+", "
      ret +="],\n"
    return ret + "]"

  def play(self,x,y,num):
    d = self.possibleNumbers.copy()
    d.append(self.default)
    if not num in d: return False
    get = self.grid[x][y]
    if get.canBeWrite: self.grid[x][y] = Number(True,num)
    else: return False
    print(self)
    return True

  def showAt(self,x,y):
    self.grid[x][y] = Number(False,self.workingGrid[x][y].number)