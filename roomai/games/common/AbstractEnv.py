#!/bin/python
# coding=utf8

import roomai.games.common
from roomai.games.common import AbstractStatePerson
from roomai.games.common import AbstractStatePrivate
from roomai.games.common import AbstractStatePublic
from roomai.games.common import Info




class AbstractEnv(object):
    '''
    The abstract class of game environment
    '''


    def __init__(self):
        self.__public_state_history__ = []
        self.__person_states_history__ = []
        self.__private_state_history__ = []
        self.__playerid_action_history__ = []

    def __gen_infos__(self):
        logger = roomai.get_logger()
        if len(self.__person_states_history__) == 0 or len(self.__public_state_history__) == 0 or len(self.__private_state_history__) == 0:
            logger.fatal("call env.__gen_infos__ before call the env.init function")
            raise Exception("call env.__gen_infos__ before call the env.init function")

        num_players = len(self.__person_states_history__)
        __infos__ = [Info(tuple(self.__public_state_history__), tuple(self.__person_states_history__[i]), tuple(self.__playerid_action_history__)) for i in range(num_players)]


        return tuple(__infos__)


    def init(self, params=dict()):
        '''
        Initialize the game environment. 

        :param params
        :return: infos, public_state, person_states, private_state
        '''

        raise ("The init function hasn't been implemented")

    def forward_able(self):
        '''
        The function returns a boolean variable, which denotes whether we can call the forward function. At the end of the game, we can't call the forward function any more.
        
        :return: A boolean variable denotes whether we can call the forward function.
        '''
        logger = roomai.get_logger()
        if len(self.__person_states_history__) == 0 or len(self.__public_state_history__) == 0 or len(self.__private_state_history__) == 0:
            logger.fatal("call env.forward_able before call the env.init function")
            raise Exception("call env.forward_able before call the env.init function")

        if self.public_state.is_terminal == True:
            return False
        else:
            return True

    def forward(self, action):
        """
        The game environment steps with the action taken by the current player

        :param action, chance_action
        :returns:infos, public_state, person_states, private_state
        """
        raise NotImplementedError("The forward hasn't been implemented")

    def backward_able(self):
        '''
        The function returns a boolean variable denotes whether we can call the backward function. If the game environment goes back to the initialization, we can't call the backward function any more.
        
        :return: A boolean variable denotes whether we can call the backward function.
        '''
        logger = roomai.get_logger()
        if len(self.__person_states_history__) == 0 or len(self.__public_state_history__) == 0 or len(self.__private_state_history__) == 0:
            logger.fatal("call env.backward_able before call the env.init function")
            raise Exception("call env.backward_able before call the env.init function")

        if len(self.__public_state_history__) <= 1:
            return False
        else:
            return True

    def backward(self):
        '''
        The game goes back to the previous states

        :returns:infos, public_state, person_states, private_state
        :raise: The game environment has reached the initialization state and can't go back further.
        '''
        logger = roomai.get_logger()
        if len(self.__person_states_history__) == 0 or len(self.__public_state_history__) == 0 or len(self.__private_state_history__) == 0:
            logger.fatal("call env.backward before call the env.init function")
            raise Exception("call env.backward before call the env.init function")


        if len(self.__public_state_history__) == 1:
            raise ValueError("Env has reached the initialization state and can't go back further. ")


        self.__public_state_history__.pop()
        self.__private_state_history__.pop()
        self.__person_states_history__.pop()
        self.__playerid_action_history__.pop()

        infos = self.__gen_infos__()
        return infos, self.__public_state_history__, self.__person_states_history__, self.__private_state_history__, self.__playerid_action_history__

    def available_actions(self):
        '''
        Generate all valid actions given the public state and the person state

        :param public_state: 
        :param person_state: 
        :return: A dict(action_key, action) contains all valid actions
        '''
        raise NotImplementedError("The available_actions function hasn't been implemented")

    def __deepcopy__(self, memodict={}, newinstance=None):
        if newinstance is None:
            newinstance = AbstractEnv()

        newinstance.__private_state_history__ = [pr.__deepcopy__() for pr in self.__private_state_history__]
        newinstance.__public_state_history__  = [pu.__deepcopy__() for pu in self.__public_state_history__]
        newinstance.__person_states_history__ = []
        if len(self.__person_states_history__) > 0:
            for i in range(len(self.__person_states_history__)):
                newinstance.__person_states_history__.append([pe.__deepcopy__() for pe in self.__person_states_history__[i]])

        newinstance.__playerid_action_history__ = list(tuple(self.__playerid_action_history__))

        return newinstance

    ### provide some util functions
    @classmethod
    def compete_silent(cls, env, players):
        '''
        Use the game environment to hold a compete for the players silently

        :param env: The game environment
        :param players: The players
        :return: scores for the players
        '''
        raise NotImplementedError("The compete_silent function hasn't been implemented")

    @classmethod
    def compete_interaction(cls, env, players):
        '''
        Use the game environment to hold a compete for the players interactively
        
        :param env: 
        :param players: 
        :return: 
        '''
        raise NotImplementedError("The compete_interaction function hasn't been implemented")

