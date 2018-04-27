import mysql.connector
import env

class Weather(object):
    def __init__(self, temperature, humidity, rain):
        self.table = 'weather'
        self.has_error = False
        self.error = ''

        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.rain = int(rain)

    def conn(self):
        try:
            self.connection = mysql.connector.connect(
                user=env.DB_USER,
                password=env.DB_PASS,
                host=env.DB_HOST,
                database=env.DB_NAME
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        finally:
            return self

    def set_error(self, message):
        self.has_error = True

    def store(self):
        self.conn()
        cursor = self.connection.cursor()
        cursor.execute(
            'INSERT INTO %s (temperature, humidity, rain) VALUES (%.2f, %.2f, %d)' % (self.table, self.temperature, self.humidity, self.rain)
        )
        self.connection.commit()
        self.connection.close()

    def update(self):
        self.conn()
        cursor = self.connection.cursor()
        cursor.execute(
            'UPDATE %s SET temperature = %.2f, humidity = %.2f, rain = %d' % (self.table, self.temperature, self.humidity, self.rain)
        )
        self.connection.commit()
        self.connection.close()

