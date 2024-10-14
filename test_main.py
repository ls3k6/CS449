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

    def test_set_red_computer(self):
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        return self.assertEqual(self.gameGUI.game.red_player.type, constant.COMPUTER)

    def test_set_blue_computer(self):
        self.gameGUI.game.set_blue_computer(self.gameGUI.gameboard)
        return self.assertEqual(self.gameGUI.game.blue_player.type, constant.COMPUTER)

    def test_computer_choose_option(self):
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        option = self.gameGUI.game.red_player.choose_option()
        return self.assertEqual(option, self.gameGUI.game.red_player.get_option())

    def test_computer_make_move(self):
        self.gameGUI.game.set_red_computer(self.gameGUI.gameboard)
        row, col = self.gameGUI.game.red_player.select_row_col(self.gameGUI.gameboard)
        self.gameGUI.game.red_player.make_move(self.gameGUI.gameboard, row, col)
        return self.assertEqual(self.gameGUI.gameboard.get_tile_symbol(row, col), self.gameGUI.game.red_player.get_option())

    def test_red_make_move(self):
        self.gameGUI.set_simple_game()
        self.gameGUI.game.set_red_turn()
        self.gameGUI.game.red_player.set_option('S')
        self.gameGUI.game.check_game_status(self.gameGUI.gameboard, 2, 2)
        return self.assertEqual(self.gameGUI.gameboard.get_tile_symbol(2, 2), self.gameGUI.game.red_player.get_option())

    def test_blue_make_move(self):
        self.gameGUI.set_simple_game()
        self.gameGUI.game.set_blue_turn()
        self.gameGUI.game.blue_player.set_option('S')
        self.gameGUI.game.check_game_status(self.gameGUI.gameboard, 2, 2)
        return self.assertEqual(self.gameGUI.gameboard.get_tile_symbol(2, 2), self.gameGUI.game.blue_player.get_option())

    def test_simple_game_over(self):
        self.gameGUI.set_simple_game()
        self.gameGUI.game.set_red_turn()
        self.gameGUI.game.red_player.set_option('S')
        self.gameGUI.gameboard.set_tile_symbol(0, 1, 'S')
        self.gameGUI.gameboard.set_tile_symbol(1, 1, 'O')
        self.gameGUI.game.check_game_status(self.gameGUI.gameboard, 2, 1)
        return self.assertEqual(self.gameGUI.game.red_wins, 1)

    def test_general_game_over(self):
        self.gameGUI.set_general_game()
        self.gameGUI.game.set_red_turn()
        self.gameGUI.game.red_player.set_option('S')
        self.gameGUI.gameboard.set_tile_symbol(0, 1, 'S')
        self.gameGUI.gameboard.set_tile_symbol(1, 1, 'O')
        self.gameGUI.game.check_game_status(self.gameGUI.gameboard, 2, 1)
        for row in range(self.gameGUI.gameboard.board_size):
            for col in range(self.gameGUI.gameboard.board_size):
                if row != 3 or col != 3:
                    if self.gameGUI.gameboard.get_tile_symbol(row, col) == constant.EMPTY:
                        self.gameGUI.gameboard.set_tile_symbol(row, col, 'O')
        self.gameGUI.game.check_game_status(self.gameGUI.gameboard, 3, 3)
        return self.assertEqual(self.gameGUI.game.red_wins, 1)


if __name__ == '__main__':
    unittest.main()
