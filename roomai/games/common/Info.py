#!/bin/python
#coding=utf8

import roomai
from roomai.games.common import AbstractStatePerson
from roomai.games.common import AbstractStatePublic




class Info(object):
    '''
    The class of information sent by env to a player. The Info class contains the public state history and the corresponding person state history w.r.t the target player
    '''
    def __init__(self, public_state_history_tuple, person_state_history_tuple, playerid_action_history_tuple):
        self.__public_state_history_tuple__       = public_state_history_tuple
        self.__person_state_history_tuple__       = person_state_history_tuple
        self.__playerid_action_history_tuple__    = playerid_action_history_tuple


    def __get_public_state_history__(self):
        return self.__public_state_history_tuple__
    public_state_history = property(__get_public_state_history__, doc="The public state history in the information")

    def __get_person_state_history__(self):
        return self.__person_state_history_tuple__
    person_state_history = property(__get_person_state_history__, doc="The person state history in the information")

    def __get_playerid_action_history__(self):
        return self.__playerid_action_history_tuple__
    playerid_action_history = property(__get_playerid_action_history__, doc = "The playerid and action history in the information")

    def __deepcopy__(self, memodict={}):
        newinstance = Info()
        newinstance.__public_state_history_tuple__  = self.__public_state_history_tuple__
        newinstance.__personc_state_history_tuple__ = self.__person_state_history_tuple__
        newinstance.__playerid_action_history_tuple__ = self.__playerid_action_history_tuple__
        return newinstance