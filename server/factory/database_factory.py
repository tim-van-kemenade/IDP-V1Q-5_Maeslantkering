import sqlite3


class DatabaseFactory:
    """Create sqlite 3 database connection instance."""
    def __init__(self):
        pass

    def create_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect('Weather.db', check_same_thread=False)
        connection.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])

        return connection
