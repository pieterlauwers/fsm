from transitions import Transitions
from states import States

class Fsm(object):
    def __init__(self, initialstate=None):
        self.state = initialstate
        self.states = States()
        self.transitions = Transitions()

    def append_state(self, name, on_enter=None, on_exit=None):
        self.states.append(name,on_enter,on_exit)

    def append_transition(self, src, event, condition=None, action=None, dst=None):
        self.transitions.append(src,event,condition,action,dst)

    def event(self, event):
        newstate = self.transitions.run(self.state,event)
        if self.state != newstate:
            self.states.exit(self.state)
            self.states.enter(newstate)
            self.state = newstate
        return self.state

if __name__ == "__main__":
    def volumeup():
        print("playing LOUDER")


    def brightnessup():
        print("Scherm blinkt harder")


    wekker = Fsm('idle')
    wekker.append_transition(src='idle', event='on', dst='playing')
    wekker.append_transition(src='playing', event='inc', action=volumeup)
    wekker.append_transition(src='idle', event='inc', action=brightnessup)
    wekker.append_transition(src='playing', event='off', dst='idle')
    def test():
        return False
    wekker.append_transition(src='idle', event='alarm', condition=test, dst='playing')
    wekker.event('inc')
    print("Wekker is now in", wekker.state)
    wekker.event('on')
    print("Wekker is now in", wekker.state)
    wekker.event('inc')
    print("Wekker is now in", wekker.state)
    wekker.event('off')
    print("Wekker is now in", wekker.state)
    wekker.event('alarm')
    print("Wekker is now in", wekker.state)

    def ouch():
        print("Auw, that hurts.")

    box = Fsm('closed')
    def opening():
        print('Puppet jumps out of the box.')
    def closing():
        print('Puppet forced in the box')
    def lid_closes():
        print('Bang!')
    box.append_state('open',on_enter=opening,on_exit=closing)
    box.append_state('closed',on_enter=lid_closes)
    box.append_transition(src='closed', event='push', condition=None, action=ouch, dst=None),
    box.append_transition(src='closed', event='pull', condition=None, action=None, dst='open'),
    box.append_transition(src='open', event='push', condition=None, action=None, dst='closed'),
    box.append_transition(src='open', event='pull', condition=None, action=ouch, dst=None),
    def do_box(e):
        print('{event} the {state} box and now the box is {newstate}'.format(event=e, state=box.state, newstate=box.event(e)))
    do_box('push')
    do_box('pull')
    do_box('pull')
    do_box('push')
