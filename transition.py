class Transition(object):
    """
    A transition describes what happens in a source state when an event occurs
    src: the current state (str)
    event: what is happening (str)
    condition: must evaluate to True for the action or state transition to happen
    action: what to do in case of the event (function)
    dst: the new state after the transition (str)
    """
    def __init__(self,src,event,condition=None,action=None,dst=None):
        self.src = src
        self.event = event
        self.condition = condition if callable(condition) else lambda: True
        self.action = action if callable(action) else lambda: None
        self.dst = dst if dst else src

if __name__== "__main__":
    t1 = Transition(src='idle',event='on',dst='playing')
    def fly():
        print("Flying")
    t2 = Transition(src='playing',event='inc',action=fly)
    t2.action()
    def test():
        return 3 < 6
    t3 = Transition(src='playing', event='off',condition=test, dst='idle')
    print(t3.condition())