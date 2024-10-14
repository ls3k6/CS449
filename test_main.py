import unittest
import constant
from main import SosGameGUI

class TestSosGameGUI(unittest.TestCase):
    def setUp(self):
        self.gameGUI = SosGameGUI()
        self.gameGUI.BOARD_SIZE = 5
        self.gameGUI.get_game_info()
        self.gameGUI.create_GUI_gameboard()

    def tearDown(self):
        return None

    def test_start_simple_game(self):
        self.gameGUI.set_simple_game()
        return self.assertEqual(self.gameGUI.game.type, constant.SIMPLE_GAME)

    def test_set_general_game(self):
        self.gameGUI.set_general_game()
        return self.assertEqual(self.gameGUI.game.type, constant.GENERAL_GAME)

    def test_set_red_human(self):
        self.gameGUI.game.set_red_human()
        return self.assertEqual(self.gameGUI.game.red_player.type, constant.HUMAN)

    def test_set_blue_human(self):
        self.gameGUI.game.set_blue_human()
        return self.assertEqual(self.gameGUI.game.blue_player.type, constant.HUMAN)

if __name__ == '__main__':
    unittest.main()
