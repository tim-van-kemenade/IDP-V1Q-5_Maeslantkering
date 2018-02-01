from flask import jsonify
from server.controllers.controller_interface import ControllerInterface


class GateController(ControllerInterface):
    """Initialize flask routes for the force commands and gate status update."""
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def add_routes(self, app):
        """Add routes to flask in app.py."""
        app.add_endpoint('/open-gate', 'open-gate', self.handle_open_gate_request)
        app.add_endpoint('/close-gate', 'close-gate', self.handle_close_gate_request)
        app.add_endpoint('/gate-status', 'gate-state', self.handle_gate_status_request)
        app.add_endpoint('/reset-gate', 'reset-gate', self.handle_reset_gate_request)

    def handle_reset_gate_request(self):
        """Reset gate and send JSON back to client."""
        self.state_machine.apply_state('open')
        return jsonify({
            "success": True,
            "message": "Gate is reset and open."
        })

    def handle_gate_status_request(self):
        """Send JSON with gate status to client."""
        return jsonify({
            "status": self.state_machine.get_current_state()
        })

    def handle_close_gate_request(self):
        """Change state to force closed and send JSON back to client"""
        self.state_machine.apply_state('force-closed')
        return jsonify({
            "success": True,
            "message": "Gate is closing."
        })

    def handle_open_gate_request(self):
        """Change state to force open and send JSON back to client."""
        self.state_machine.apply_state('force-open')
        return jsonify({
            "success": True,
            "message": "Gate is opening."
        })