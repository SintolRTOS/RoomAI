class AbstractPlayerChance(object):
    '''
    The abstract class of a chance player. 
    '''

    def receive_info(self, info):
        '''
        Receive information 

        :param:info: the information produced by a game environments
        :raises: NotImplementedError: An error occurred when we doesn't implement this function
        '''
        raise NotImplementedError("The receiveInfo function hasn't been implemented")

    def take_action(self):
        """
        :returns: The action produced by this player
        """
        raise NotImplementedError("The takeAction function hasn't been implemented")

    def reset(self):
        '''
        reset for a new game 
        '''
        raise NotImplementedError("The reset function hasn't been implemented")


class RandomPlayerChance(AbstractPlayerChance):
    '''
    The RandomChancePlayer is a chance player, who randomly takes an action.
    '''
    def receive_info(self, info):
        self.available_actions = info.person_state_history[-1].available_actions

    def take_action(self):
        import random
        idx = int(random.random() * len(self.available_actions))
        return list(self.available_actions.values())[idx]

    def reset(self):
        pass