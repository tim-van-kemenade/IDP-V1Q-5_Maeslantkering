from flask import jsonify
from server.controllers.controller_interface import ControllerInterface


class GateController(ControllerInterface):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def add_routes(self, app):
        app.add_endpoint('/open-gate', 'open-gate', self.handle_open_gate_request)
        app.add_endpoint('/close-gate', 'close-gate', self.handle_close_gate_request)
        app.add_endpoint('/gate-status', 'gate-state', self.handle_gate_status_request)

    def handle_gate_status_request(self):
        return jsonify({
            "status": self.state_machine.get_current_state()
        })

    def handle_close_gate_request(self):
        self.state_machine.apply_state('closed')
        return jsonify({
            "success": True,
            "message": "Gate is closing."
        })

    def handle_open_gate_request(self):
        self.state_machine.apply_state('open')
        return jsonify({
            "success": True,
            "message": "Gate is opening."
        })