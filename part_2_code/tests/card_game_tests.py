import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("Diamonds", 10)
        self.card2 = Card("Spades", 5)
        self.card3 = Card("Hearts", 1)
        self.cards = [self.card1, self.card2, self.card3]
    
    def test_check_for_ace_true(self):
        game1 = self.game.check_for_ace(self.card3)
        self.assertEqual(True, game1)

    def test_check_for_ace_false(self):
        game2 = self.game.check_for_ace(self.card2)
        self.assertEqual(False, game2)

    def test_highest_card_card1_highest(self):
        game3 = self.game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, game3)

    def test_highest_card_card2_highest(self):
        game4 = self.game.highest_card(self.card2, self.card1)
        self.assertEqual(self.card1, game4)

    def test_cards_total(self):
        game5 = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 16", game5)