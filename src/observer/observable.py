# -*- coding: utf-8 -*-
#########################
#       OBSERVABLE      #
#########################



#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# OBSERVABLE CLASS      #
#########################
class Observable():
    """
    Implementation of Observable interface, according to Observer Pattern.
    """


# CONSTRUCTOR #################################################################
    def __init__(self):
        self.observers = set()


    def register_observer(self, observer):
        """Registering observable"""
        self.observers.add(observer)


    def deregister_observer(self, observer):
        """Deregistering observable"""
        self.observers.remove(observer)


# PUBLIC METHODS ##############################################################
    def notify(self):
        """Notify observers"""
        for o in self.observers:
            o.update()




if __name__ == '__main__':
    pass

