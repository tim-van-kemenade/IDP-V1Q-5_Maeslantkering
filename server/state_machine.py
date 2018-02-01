class StateMachine:
    """Class to change the state and execute the corresponding functions."""
    current_state = 'closed'
    states = {}

    def __init__(self, states):
        self.states = states

    def apply_state(self, state_name):
        """Apply state and use it's handle if state exists."""
        if state_name not in self.states:
            raise Exception('The state' + state_name + ' does not exists!')

        self.states[state_name].handle()
        self.current_state = state_name

    def get_current_state(self) -> str:
        return self.current_state
