#!/bin/python
#coding:utf-8
import roomai.games.common


class TexasHoldemStatePrivate(roomai.games.common.AbstractStatePrivate):

    '''
    The private state of TexasHoldem
    '''
    def __init__(self):
        super(TexasHoldemStatePrivate, self).__init__()
        self.__keep_cards__ = []
        self.__all_used_cards__ = []


    def __get_keep_cards__(self):   return tuple(self.__keep_cards__)
    keep_cards = property(__get_keep_cards__, doc="the keep cards.")

    def __get_all_used_cards__(self):   return tuple(self.__all_used_cards__)
    all_used_cards = property(__get_all_used_cards__, doc="all used cards.")


    def __deepcopy__(self, memodict={}, newinstance = None):
        if newinstance is None:
            newinstance = TexasHoldemStatePrivate()

        newinstance.__keep_cards__ = [self.keep_cards[i] for i in range(len(self.keep_cards))]
        newinstance.__all_used_cards__ = [self.all_used_cards[i] for i in range(len(self.all_used_cards))]
        return newinstance