import sys, os
os.chdir(os.getcwd() + '/Controller/')
sys.path.insert(1, '../Controller/')
import GameController

game = GameController.GameController()
game.run_game()
