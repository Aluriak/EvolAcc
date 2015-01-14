# -*- coding: utf-8 -*-
#########################
#       OBSERVER        #
#########################



#########################
# IMPORTS               #
#########################




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# OBSERVER CLASS        #
#########################
class Observer():
    """
    Implementation of Observer interface, according to Observer Pattern.
    """


# CONSTRUCTOR #################################################################
    def __init__(self, observable):
        """
        observable must define register_observer and 
            deregister_observer methods.
        """
        self.observable = observable
        if self.observable is not None:
            self.observable.register_observer(self)


    def __del__(self):
        """
        unregistering at observable if necessary.
        """
        if self.observable is not None:
            self.observable.deregister_observer(self)


# PUBLIC METHODS ##############################################################
    def update(self):
        """
        Be notified about observable changes
        """
        if self.observable is not None:
            raise NotImplementedError




if __name__ == '__main__':
    from observable import Observable

    class Animal(Observable):
        def register_observer(self, obs):
            super().register_observer(obs)
            print('someone looked at me !')
        def deregister_observer(self, obs):
            super().deregister_observer(obs)
            print('alert finished !')

    class Zoologist(Observer):
        def update(self):
            print('*', self.__class__.__name__, 
                  'take some notes about', 
                  self.observable.__class__.__name__, '*')

    baby_bird = Animal()
    print('baby_bird defined')
    darwin = Zoologist(baby_bird)
    print('darwin defined')
    baby_bird.notify()
    baby_bird.notify()
    del darwin
    print('darwin deleted')
    


