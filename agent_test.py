"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import tournament

from copy import copy
import timeit

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

    # def test_minimax_agent(self):
    #     self.player1 = game_agent.MinimaxPlayer()
    #     self.player2 = game_agent.MinimaxPlayer()
    #     self.game = isolation.Board(self.player1, self.player2)
    #
    #     #  assert current active player is player-1
    #     assert (self.player1 == self.game.active_player)
    #     time_limit = 150
    #     time_millis = lambda: 1000 * timeit.default_timer()
    #     game_copy = self.game.copy()
    #
    #     move_start = time_millis()
    #     time_left = lambda: time_limit - (time_millis() - move_start)
    #     best_move = self.game._active_player.get_move(game_copy, time_left)
    #     move_end = time_left()

    # def test_alphabeta_agent(self):
    #     self.player1 = game_agent.AlphaBetaPlayer()
    #     self.player2 = game_agent.AlphaBetaPlayer()
    #     self.game = isolation.Board(self.player1, self.player2)
    #
    #     #  assert current active player is player-1
    #     assert (self.player1 == self.game.active_player)
    #     time_limit = 150
    #     time_millis = lambda: 1000 * timeit.default_timer()
    #     game_copy = self.game.copy()
    #
    #     move_start = time_millis()
    #     time_left = lambda: time_limit - (time_millis() - move_start)
    #     best_move = self.game._active_player.get_move(game_copy, time_left)
    #     move_end = time_left()


    def test_main(self):
        tournament.main()



if __name__ == '__main__':
    unittest.main()

