from transition import Transition
from fsm import Fsm

class Wekker(Fsm):
    """
    A wekker with a time display and radio as a finite state machine
    """
    def __init__(self):
        transitions = [
            Transition(src='idle',  event='inc',   condition=None,             action=self.bright_inc,    dst=None),
            Transition(src='idle',  event='on',    condition=None,             action=self.radio_on,      dst='playing'),
            Transition(src='idle',  event='alarm', condition=self.switchstate, action=self.radio_on,      dst='playing'),
            Transition(src='playing', event='inc', condition=None,             action=self.vol_up,        dst=None),
            Transition(src='playing', event='off', condition=None,             action=self.radio_off,     dst='idle'),
        ]
        self.vol=0
        self.brightness=0
        self.switch = True
        Fsm.__init__(self,'idle')
        self.transition_push(transitions)
    def switchstate(self):
        return self.switch
    def switchon(self):
        self.switch = True
    def switchoff(self):
        self.switch = False
    def radio_on(self):
        print("Start radio")
    def radio_off(self):
        print("Stop radio")
    def vol_up(self):
        self.vol += 1
    def vol_down(self):
        self.vol -= 1
    def bright_inc(self):
        self.brightness += 1
    def bright_dec(self):
        self.brightness -= 1

if __name__== "__main__":
    clock=Wekker()
    clock.on_event('on')
    clock.on_event('off')
    clock.on_event('inc')
    clock.on_event('on')
    clock.on_event('inc')
