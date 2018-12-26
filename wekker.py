from fsm import Fsm

class Wekker(Fsm):
    """
    A wekker with a time display and radio as a finite state machine
    """
    def __init__(self):
        Fsm.__init__(self,'idle')
        self.append_state(name='idle',       on_enter=self.showtime)
        self.append_state(name='playing',    on_enter=self.radio_on,    on_exit=self.radio_off)
        self.append_transition(src='idle',  event='inc',   condition=None,             action=self.bright_inc,    dst=None),
        self.append_transition(src='idle',  event='on',    condition=None,             action=None,               dst='playing'),
        self.append_transition(src='idle',  event='alarm', condition=self.switchstate, action=None,               dst='playing'),
        self.append_transition(src='playing', event='inc', condition=None,             action=self.vol_up,        dst=None),
        self.append_transition(src='playing', event='off', condition=None,             action=None,               dst='idle'),
        self.vol=0
        self.brightness=0
        self.switch = True
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
    def showtime(self):
        print('17:12')

if __name__== "__main__":
    clock=Wekker()
    clock.event('on')
    clock.event('off')
    clock.event('inc')
    clock.event('on')
    clock.event('inc')
