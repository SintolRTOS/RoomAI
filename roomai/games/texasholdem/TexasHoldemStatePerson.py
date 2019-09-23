#!/bin/python
#coding:utf-8
import roomai.games.common


class TexasHoldemStatePerson(roomai.games.common.AbstractStatePerson):

    def __init__(self):
        super(TexasHoldemStatePerson, self).__init__()
        self.__hand_cards__  =    []

    def __get_hand_cards__(self):   return tuple(self.__hand_cards__)
    hand_cards = property(__get_hand_cards__, doc="The hand cards of the corresponding player. It contains two poker cards. For example, hand_cards=[roomai.coomon.Card.lookup(\"A_Spade\"),roomai.coomon.Card.lookup(\"A_Heart\")]")

    def __deepcopy__(self, memodict={}, newinstance = None):
        if newinstance is None:
            newinstance    = TexasHoldemStatePerson()
        newinstance = super(TexasHoldemStatePerson, self).__deepcopy__(newinstance=newinstance)
        newinstance.__hand_cards__ = list(self.hand_cards)
        return  newinstance



