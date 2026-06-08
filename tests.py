"""Unit tests to test functionality of project.
"""

import unittest
import random
from unittest.mock import patch, MagicMock

from modules import strings, animate, prof, route, pythodex

class TestAttack(unittest.TestCase):
    
    def setUp(self):
        self.pythomon = route.Opponent("PYPY", 20, strings.pypy_sprite)

    def test_dmg_goes_down(self):
        route.attack(self.pythomon, "Nickname")
        self.assertIn(self.pythomon.current_hp, (range(16, 19)))
        
    def test_hp_does_not_fall_below_zero(self):
        self.pythomon.current_hp = 1
        route.attack(self.pythomon, "Nickname")
        self.assertEqual(self.pythomon.current_hp, 0)


class TestCatch(unittest.TestCase):
    
    def setUp(self):
        self.pythomon = route.Opponent("PYPY", 20, strings.pypy_sprite)
        self.player_dex = []
        
    def test_continue_encounter_if_fail(self):
        self.pythomon.throw_ball = MagicMock(return_value=False)
        self.assertTrue(route.catch(self.pythomon, self.player_dex))

    def test_end_encounter_if_success(self):
        self.pythomon.throw_ball = MagicMock(return_value=True)
        self.assertFalse(route.catch(self.pythomon, self.player_dex))

class TestFind(unittest.TestCase):

    def setUp(self):
        self.test_pythomon = {
            "name" : "PYPY",
            "hp" : 20,
            "sprite" : strings.pypy_sprite
        }

    @patch('random.choices')
    def test_correct_pythomon_called(self, mock_choices):
        mock_choices.return_value = [self.test_pythomon]
        result = route.find()
        self.assertEqual(result.name, "PYPY")
        






                 
    