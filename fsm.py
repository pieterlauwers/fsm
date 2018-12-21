from transitions import Transitions


class Fsm(object):
    def __init__(self, initialstate):
        self.state = initialstate
        self.transitions = Transitions()

    def append_transition(self, src, event, condition=None, action=None, dst=None):
        self.transitions.append(src,event,condition,action,dst)

    def on_event(self, event):
        self.state = self.transitions.run(self.state,event)

if __name__ == "__main__":
    def volumeup():
        print("playing louDER")


    def brightnessup():
        print("Scherm blinkt harder")


    wekker = Fsm('idle')
    wekker.append_transition(src='idle', event='on', dst='playing')
    wekker.append_transition(src='playing', event='inc', action=volumeup)
    wekker.append_transition(src='idle', event='inc', action=brightnessup)
    wekker.append_transition(src='playing', event='off', dst='idle')
    def test():
        return True
    wekker.append_transition(src='idle', event='alarm', condition=test, dst='playing')
    wekker.on_event('inc')
    print("Wekker is now in", wekker.state)
    wekker.on_event('on')
    print("Wekker is now in", wekker.state)
    wekker.on_event('inc')
    print("Wekker is now in", wekker.state)
    wekker.on_event('off')
    print("Wekker is now in", wekker.state)
    wekker.on_event('alarm')
    print("Wekker is now in", wekker.state)

    def ouch():
        print("Auw, that hurts.")

    box = Fsm('closed')
    box.append_transition(src='closed', event='push', condition=None, action=ouch, dst=None),
    box.append_transition(src='closed', event='pull', condition=None, action=None, dst='open'),
    box.append_transition(src='open', event='push', condition=None, action=None, dst='close'),
    box.append_transition(src='open', event='pull', condition=None, action=ouch, dst=None),
    box.on_event('push')
    box.on_event('pull')
    box.on_event('pull')
    box.on_event('push')
