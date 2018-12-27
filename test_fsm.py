from fsm import Fsm
"""
Testcases for the fsm class (finit state machine).
Run the pytest command in this folder to execute the tests.
"""
def test_fsm_initialize_default():
    state_machine = Fsm()
    assert state_machine.state is None
def test_fsm_initialize_initial_state():
    state_machine = Fsm('idle')
    assert state_machine.state == 'idle'
def test_fsm_set_state():
    state_machine = Fsm()
    state_machine.state = 'idle'
    assert state_machine.state == 'idle'
def test_fsm_basic_transition():
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on', dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'playing'
def test_fsm_unknown_transition():
    state_machine = Fsm('idle')
    state_machine.event('on')
    assert state_machine.state == 'idle'
def test_fsm_transition_condition_false():
    def test():
        return False
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on',condition=test, dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'idle'
def test_fsm_transition_condition_true():
    def test():
        return True
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on',condition=test, dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'playing'
def test_fsm_transition_action_only():
    a = 0
    def inc():
        nonlocal a
        a = a + 1
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on', action=inc,)
    state_machine.event('on')
    assert state_machine.state == 'idle'
    assert a == 1
def test_fsm_transition_action_condition_false():
    a = 0
    def inc():
        nonlocal a
        a = a + 1
    def test():
        return False
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on', condition=test, action=inc, dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'idle'
    assert a == 0
def test_fsm_transition_action_condition_true():
    a = 0
    def inc():
        nonlocal a
        a = a + 1
    def test():
        return True
    state_machine = Fsm('idle')
    state_machine.append_transition(src='idle', event='on', condition=test, action=inc, dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'playing'
    assert a == 1
def test_fsm_state_enter():
    a = 0
    def start():
        nonlocal a
        a = a + 1
    state_machine = Fsm('idle')
    state_machine.append_state(name='playing', on_enter=start)
    state_machine.append_transition(src='idle', event='on', dst='playing')
    state_machine.event('on')
    assert state_machine.state == 'playing'
    assert a == 1
def test_fsm_state_exit():
    a = 0
    def stop():
        nonlocal a
        a = a - 1
    state_machine = Fsm('playing')
    state_machine.append_state(name='playing', on_exit=stop)
    state_machine.append_transition(src='playing', event='off', dst='idle')
    state_machine.event('off')
    assert state_machine.state == 'idle'
    assert a == -1
