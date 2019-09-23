#!/bin/python
import unittest

import roomai.games.common
from roomai.games.texasholdem import TexasHoldemAction
from roomai.games.texasholdem import TexasHoldemEnv


class TexasUtilsTester(unittest.TestCase):
    """
    """

    def test_pattern(self):
        """

        """

        handcards1 =[roomai.games.texasholdem.PokerCard(0, 0), roomai.games.texasholdem.PokerCard(1, 1)]
        keepcards  =[roomai.games.texasholdem.PokerCard(2, 2), roomai.games.texasholdem.PokerCard(3, 3), roomai.games.texasholdem.PokerCard(4, 0), roomai.games.texasholdem.PokerCard(5, 1), roomai.games.texasholdem.PokerCard(6, 2)]
        pattern    = TexasHoldemEnv.__cards2pattern_cards__(handcards1, keepcards)

    
    def test_cards1(self):
        """

        """
        handcards1 = [roomai.games.texasholdem.PokerCard(0, 0), roomai.games.texasholdem.PokerCard(0, 1)]
        handcards2 = [roomai.games.texasholdem.PokerCard(3, 1), roomai.games.texasholdem.PokerCard(3, 2)]
        keepcards  = [roomai.games.texasholdem.PokerCard(0, 2), roomai.games.texasholdem.PokerCard(0, 3), roomai.games.texasholdem.PokerCard(2, 0), roomai.games.texasholdem.PokerCard(2, 1), roomai.games.texasholdem.PokerCard(3, 3)]
        pattern = TexasHoldemEnv.__cards2pattern_cards__(handcards2, keepcards)[0]
        cards   = TexasHoldemEnv.__cards2pattern_cards__(handcards2, keepcards)[1]

        self.assertEqual(pattern[0],'3_2')
        self.assertEqual(pattern[1],False)
        self.assertEqual(pattern[2],True)
        self.assertEqual(pattern[3],False)
        self.assertEqual(pattern[4][0], 3)
        self.assertEqual(pattern[4][1], 2)
        self.assertEqual(cards[0].point_rank, 3)
        self.assertEqual(cards[1].point_rank, 3)
        self.assertEqual(cards[2].point_rank, 3)
        self.assertEqual(cards[3].point_rank, 2)
        self.assertEqual(cards[4].point_rank, 2)

        self.assertEqual(cards[0].suit_rank, 1)
        self.assertEqual(cards[1].suit_rank, 2)
        self.assertEqual(cards[2].suit_rank, 3)
        self.assertEqual(cards[3].suit_rank, 0)
        self.assertEqual(cards[4].suit_rank, 1)

    def test_cards2(self):
        """

        """

        h1     = [roomai.games.texasholdem.PokerCard(7, 0), roomai.games.texasholdem.PokerCard(7, 1)]
        keep   = [roomai.games.texasholdem.PokerCard(3, 1), roomai.games.texasholdem.PokerCard(4, 2), roomai.games.texasholdem.PokerCard(5, 3), roomai.games.texasholdem.PokerCard(6, 0), roomai.games.texasholdem.PokerCard(7, 2)]
        pattern = TexasHoldemEnv.__cards2pattern_cards__(h1, keep)[0]
        self.assertEqual(pattern[0],"3_1_1")


    def test_cards(self):
        """

        """
        handcards1 = [roomai.games.texasholdem.PokerCard(0, 0), roomai.games.texasholdem.PokerCard(0, 1)]
        handcards2 = [roomai.games.texasholdem.PokerCard(3, 1), roomai.games.texasholdem.PokerCard(3, 2)]
        keepcards  = [roomai.games.texasholdem.PokerCard(0, 2), roomai.games.texasholdem.PokerCard(0, 3), roomai.games.texasholdem.PokerCard(2, 0), roomai.games.texasholdem.PokerCard(2, 1), roomai.games.texasholdem.PokerCard(3, 3)]
        pattern = TexasHoldemEnv.__cards2pattern_cards__(handcards1, keepcards)[0]
        cards   = TexasHoldemEnv.__cards2pattern_cards__(handcards1, keepcards)[1]
        self.assertEqual(pattern[0],'4_1')
        self.assertEqual(pattern[1],False)
        self.assertEqual(pattern[2],True)
        self.assertEqual(pattern[3],False)
        self.assertEqual(pattern[4][0], 4)
        self.assertEqual(pattern[4][1], 1)
        self.assertEqual(cards[0].point_rank, 0)
        self.assertEqual(cards[1].point_rank, 0)
        self.assertEqual(cards[2].point_rank, 0)
        self.assertEqual(cards[3].point_rank, 0)
        self.assertEqual(cards[4].point_rank, 3)

        self.assertEqual(cards[0].suit_rank, 0)
        self.assertEqual(cards[1].suit_rank, 1)
        self.assertEqual(cards[2].suit_rank, 2)
        self.assertEqual(cards[3].suit_rank, 3)
        self.assertEqual(cards[4].suit_rank, 3)


        pattern1 = TexasHoldemEnv.__cards2pattern_cards__(handcards1, keepcards)
        pattern2 = TexasHoldemEnv.__cards2pattern_cards__(handcards2, keepcards)

        diff = TexasHoldemEnv.__compare_handcards__(handcards1, handcards2, keepcards)
        self.assertTrue(diff > 0)


    def test_available_actions(self):
        """

        """
        env = TexasHoldemEnv()
        infos, public_history, persons_history, private_history, action_history = env.init()


        pu  = public_history[-1]
        pr  = private_history[-1]
        pe  = persons_history[pu.turn][-1]


        while len(pr.all_used_cards) < (len(persons_history)-1) * 2 + 5:
            action = list(pe.available_actions.values())[-1]

            if len(pr.all_used_cards) == (len(persons_history) -1)*2 + 4:
                xx = 0
                pass


            env.forward(action)

            pu = public_history[-1]
            pr = private_history[-1]
            pe = persons_history[pu.turn][-1]



        actions = env.available_actions()
        self.assertTrue("Allin_1000" in actions)

        env.__public_state_history__[-1].__raise_account__ = 200
        actions = env.available_actions()
        self.assertTrue("Call_10" in actions)
        self.assertTrue("Raise_210" in actions)
        self.assertTrue("Raise_410" in actions)
        self.assertTrue("Raise_410" in actions)
        self.assertTrue("Raise_810" in actions)
        self.assertTrue("Allin_1000" in actions)
        for key in actions:
            act = actions[key]




    def test_is_action_valid(self):
        """

        """
        env = TexasHoldemEnv()
        env.init()


        print (TexasHoldemAction.AllIn)
        action = TexasHoldemAction("Allin_1000")
        print (action.key)



    def test_compare(self):
        """

        """
        h1 = [roomai.games.texasholdem.PokerCard(7, 0), roomai.games.texasholdem.PokerCard(7, 1)]
        h2 = [roomai.games.texasholdem.PokerCard(2, 0), roomai.games.texasholdem.PokerCard(2, 1)]
        h3 = [roomai.games.texasholdem.PokerCard(2, 2), roomai.games.texasholdem.PokerCard(2, 3)]
        k  = [roomai.games.texasholdem.PokerCard(3, 1), roomai.games.texasholdem.PokerCard(4, 2), roomai.games.texasholdem.PokerCard(5, 3), roomai.games.texasholdem.PokerCard(6, 0), roomai.games.texasholdem.PokerCard(7, 2)]

        p1 = TexasHoldemEnv.__cards2pattern_cards__(h1, k)
        p2 = TexasHoldemEnv.__cards2pattern_cards__(h2, k)
        p3 = TexasHoldemEnv.__cards2pattern_cards__(h3, k)
