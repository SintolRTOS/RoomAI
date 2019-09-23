#!/bin/python
#coding=utf8

import roomai.games.common
logger = roomai.get_logger()



class AbstractStatePrivate(object):
    '''
    The Abstract class of the private state. The information in the private state is hidden from every player
    '''
    def __deepcopy__(self, memodict={}):
        return AbstractStatePrivate()
