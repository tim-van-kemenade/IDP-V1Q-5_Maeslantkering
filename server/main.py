from server.app import App
from server.controllers.rest_controller import RestController
from server.repository.water_repository import WaterRepository
from server.repository.storm_repository import StormRepository
from server.factory.database_factory import  DatabaseFactory

app = App()

connection = DatabaseFactory().create_connection()

water_repository = WaterRepository(connection)
storm_repository = StormRepository(connection)

app.register_controller(RestController(water_repository, storm_repository))

if __name__ == '__main__':
    app.run()
