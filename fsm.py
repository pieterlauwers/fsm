from transition import Transition

class Fsm(object):
    def __init__(self,initialstate):
        self.state = initialstate
        self.transitions=[]

    def transition_push(self,trans):
        if type(trans) is not list:
            trans = [trans]
        self.transitions.extend(trans)

    def on_event(self,event):
        state_event_transitions = [ t for t in self.transitions if t.src == self.state and t.event == event]
        if len(state_event_transitions) > 0:
            transition = state_event_transitions[0]
            if transition.condition():
                if transition.action:
                    print("Calling",transition.action)
                    transition.action()
                if self.state != transition.dst:
                    self.state = transition.dst
                    print("New state is",self.state)


if __name__== "__main__":
    def volumeup():
        print("playing louDER")
    def brightnessup():
        print("Scherm blinkt harder")
    wekker = Fsm('idle')
    t1 = Transition(src='idle',event='on',dst='playing')
    wekker.transition_push(t1)
    t2 = Transition(src='playing',event='inc',action=volumeup)
    t3 = Transition(src='idle',event='inc',action=brightnessup)
    t4 = Transition(src='playing',event='off',dst='idle')
    wekker.transition_push([t2,t3,t4])
    def test():
        return 3>6
    t5 = Transition(src='idle',event='alarm',condition=test,dst='playing')
    wekker.transition_push(t5)

    wekker.on_event('inc')
    print("Wekker is now in",wekker.state)
    wekker.on_event('on')
    print("Wekker is now in",wekker.state)
    wekker.on_event('inc')
    print("Wekker is now in",wekker.state)
    wekker.on_event('off')
    print("Wekker is now in",wekker.state)
    wekker.on_event('alarm')
    print("Wekker is now in",wekker.state)

    def ouch():
        print("Auw, that hurts.")
    ts = [
        Transition(src='closed',  event='push', condition=None, action=ouch,   dst=None),
        Transition(src='closed',  event='pull', condition=None, action=None,   dst='open'),
        Transition(src='open',    event='push', condition=None, action=None,   dst='close'),
        Transition(src='open',    event='pull', condition=None, action=ouch,   dst=None),
    ]
    box = Fsm('closed')
    box.transition_push(ts)
    box.on_event('push')
    box.on_event('pull')
    box.on_event('pull')
    box.on_event('push')