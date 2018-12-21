class Transitions(object):
    """
    A transition describes what happens in a source state when an event occurs
    src: the current state (str)
    event: what is happening (str)
    condition: a function that must evaluate to True for the action or state transition to happen
    action: what to do in case of the event (function)
    dst: the new state after the transition (str)
    """
    def __init__(self):
        self.transitions = {}
    def append(self,src,event,condition=None,action=None,dst=None):
        eventhandler = {}
        if callable(condition): eventhandler['condition'] = condition
        if callable(action): eventhandler['action'] = action
        if dst: eventhandler['dst'] = dst
        self.transitions[(src,event)] = eventhandler
    def run(self,src,event):
        if (src,event) in self.transitions:
            eventhandler = self.transitions[(src,event)]
            if 'condition' in eventhandler:
                if not eventhandler['condition'](): return src
            if 'action' in eventhandler:
                eventhandler['action']()
            if 'dst' in eventhandler:
                return eventhandler['dst']
            else:
                return src
    def condition(self,src,event):
        try:
            return self.transitions[(src,event)].condition
        except KeyError:
            return None
    def action(self,src,event):
        try:
            return self.transitions[(src,event)].action
        except KeyError:
            return None
    def dst(self,src,event):
        try:
            return self.transitions[(src,event)].dst
        except KeyError:
            return src

if __name__== "__main__":
    door = Transitions()
    door.append('open','push',dst='closed')
    door.append('closed','pull',dst='open')
    print('Push the open door and the door is {dst}'.format(dst = door.run('open','push')))
    def locking():
        print('Krick krack')
    door.append('closed','lock',action=locking,dst='locked')
    print('Lock the closed door and the door is {dst}'.format(dst = door.run('closed','lock')))


