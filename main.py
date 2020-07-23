from core.sudoku import Sudoku
from core.IG import GraphicalInterface

from core.players.human import Human

player = Human()
sudo = Sudoku(player)

gi = GraphicalInterface(sudo)
gi.start()