from server.app import App
from server.controllers.rest_controller import RestController

app = App()

app.register_controller(RestController)

if __name__ == '__main__':
    app.run()
