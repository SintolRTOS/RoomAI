#!/bin/python
import logging;
import sys;

project_name = "roomai";

'%(asctime)s|process:%(process)d|filename:%(filename)s|lineNum:%(lineno)d|level:%(levelno)s|log_msg:%(message)s'

logger = logging.getLogger(project_name);
handler = logging.StreamHandler(sys.stderr);
formatter = logging.Formatter("%(asctime)s - %(levelname)s - line %(lineno)d in %(filename)s - %(message)s");

logger.setLevel(logging.INFO);
handler.setLevel(logging.INFO);
handler.setFormatter(formatter);
logger.addHandler(handler);

class FrozenDict(dict):
    def __setitem__(self, key, value):
        raise NotImplementedError("The FrozenDict doesn't support the __setitem__ function")


def version():
    '''

    :return: The version of RoomAI 
    '''
    version = "0.1.16"
    print("roomai-%s" % version)
    return ("roomai-%s" % version)


def set_loglevel(level):
    '''
    set the level of log
    
    :param level: 
    :return: 
    '''
    logger.setLevel(level)
    handler.setLevel(level)

def get_logger():
    '''
    get the logger
    
    :return: 
    '''
    return logger

