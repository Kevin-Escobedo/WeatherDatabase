import sqlite3
import datetime

class WeatherDatabase:
    def __init__(self, name: str = "weather.db"):
        self.db = sqlite3.connect(name, detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cursor = self.db.cursor()

    def createTable(self, tableName: str) -> None:
        '''Creates a new table in the database'''
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS {}(TIME TIMESTAMP PRIMARY KEY, TEMPERATURE REAL, 
        PRESSURE INT, HUMIDITY INT, DESCRIPTION TEXT)
        '''.format(tableName))
        self.db.commit()

    def insertData(self, city: str, data: tuple) -> None:
        '''Inserts weather data into appropriate table'''
        try:
            currentTime = datetime.datetime.now()
            self.cursor.execute('''
            INSERT INTO {}(TIME, TEMPERATURE, PRESSURE, HUMIDITY, DESCRIPTION)
            VALUES(?, ?, ?, ?, ?)
            '''.format(city), (currentTime, data[0], data[1], data[2], data[3]))

        except sqlite3.IntegrityError:
            print("Invalid Entry")

    def close(self) -> None:
        '''Closes the connection to the database'''
        self.db.commit()
        self.db.close()