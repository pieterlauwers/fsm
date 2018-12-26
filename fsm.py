class Transitions(object):
    """
    A transition describes what happens in a source state when an event occurs
    src: the current state (str)
    event: what is happening (str)
    condition: a function that must return True for the action or state transition to happen
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

class States(object):
    """
    Describe a collection of states for a finit state machine.
    A state has a
    name: The name of the state (str)
    on_entry: A function to be called when entering the state
    on_exit: A function to be called when leaving the state
    """
    def __init__(self):
        self.states = {}
    def append(self, name, on_enter=None, on_exit=None):
        callback_functions = {}
        if callable(on_enter): callback_functions['on_enter'] = on_enter
        if callable(on_exit): callback_functions['on_exit'] = on_exit
        self.states[name] = callback_functions
    def enter(self,name):
        if name in self.states:
            if 'on_enter' in self.states[name]:
                return self.states[name]['on_enter']()
    def exit(self,name):
        if name in self.states:
            if 'on_exit' in self.states[name]:
                return self.states[name]['on_exit']()


class Fsm(object):
    """
    A finit state machine described by a list of transitions.
    A transition moves the state machine from one state to another when an event happens
    Transitions can be conditional and can call an external function when they happen
    States are regular strings, but can have enter and exit functions that get called automatically
    """
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
