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

if __name__== "__main__":
    radio = States()
    def start_playing():
        print('Good morning Vietnam.')
    def stop_playing():
        print('Hasta la vista Baby.')
    radio.append('playing', on_enter=start_playing, on_exit=stop_playing)
    radio.enter('playing')
    radio.exit('playing')
    radio.enter('upsidedown')