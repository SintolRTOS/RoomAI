#!/bin/python
#coding=utf8

import roomai.games.common
from roomai import FrozenDict
logger = roomai.get_logger()



class AbstractStatePerson(object):
    '''
    The abstract class of the person state. The information in the person state is public to the corresponding player and hidden from other players
    '''
    def __init__(self):
        self.__id__ = 0
        self.__available_actions__ = dict()

    def __get_id__(self):   return self.__id__
    id = property(__get_id__, doc="The id of player w.r.t this person state")

    def __get_available_actions__(self):  return FrozenDict(self.__available_actions__)
    available_actions = property(__get_available_actions__, doc="All valid actions for the player expected to take an action. The person state w.r.t no-current player contains empty available_actions")


    def __deepcopy__(self, memodict={}, newinstance = None):
        if newinstance is  None:
            newinstance = AbstractStatePerson()
        newinstance.__id__ = self.__id__
        newinstance.__available_actions__ = dict(self.available_actions)
        return newinstance