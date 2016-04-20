import sys
import mysql.connector as mariadb
import logging
import json
import collections
from flask import jsonify

username = '[USER]'
password = '[PASSWORD]'
database = '[DATABASE]'

mariadb_connection = mariadb.connect(user=username, password=password, database=database)



def insertreading(Reading):
    try:
        cursor = mariadb_connection.cursor()
        cursor.execute(
            "INSERT INTO reading (Temp1,Temp2,TempSensorAvg,Pressure,SeaLevelPressure,Humidity,TimeStamp) "
            "VALUES (%s, %s, %s, %s, %s, %s, NOW())", (
            Reading.temp1, Reading.temp2, Reading.tempavg, Reading.pressure, Reading.sealevelpressure,
            Reading.humidity))

        mariadb_connection.commit()

    except mariadb.Error as error:
        logging.error("Error: {}".format(error))
        return False

    except IOError as e:
        logging.error("I/O error({0}): {1}".format(e.errno, e.strerror))
        return False

    except:
        logging.error("Unexpected error:", sys.exc_info()[0])
        return False

    # if all is good
    return True


def getreading(amount):

    cursor = mariadb_connection.cursor()

    #query = ("""
    #          SELECT readingID,Temp1,Temp2,TempSensorAvg,Humidity,Pressure,SeaLevelPressure,TimeStamp
    #          FROM weather.reading ORDER BY readingID DESC LIMIT 0, """ + str(amount))

    query = ("""
                SELECT * FROM (SELECT * FROM weather.reading
            ORDER BY readingID desc LIMIT 0, """ + str(amount) + """) as newtable order by newtable.readingID asc
    """)

    cursor.execute(query)

    rows = cursor.fetchall()

    column = [t[0] for t in cursor.description]
    result = []

    for row in rows:
        myjson = {
            column[0]: row[0],
            column[1]: str(row[1]),
            column[2]: str(row[2]),
            column[3]: str(row[3]),
            column[4]: str(row[4]),
            column[5]: str(row[5]),
            column[6]: str(row[6]),
            column[7]: str(row[7])
        }

        result.append(myjson)

    cursor.close()

    return json.dumps(result, indent=3)


def getsinglereading(id):

    cursor = mariadb_connection.cursor()

    query = ("SELECT * FROM weather.reading WHERE readingID=" + str(id))

    cursor.execute(query)

    output = []

    for (readingID, Temp1, Temp2, TempSensorAvg, Pressure, SeaLevelPressure, Humidity, TimeStamp) in cursor:

        output.append(str({
            "readingID": readingID,
            "Temp1": str(Temp1),
            "Temp2": str(Temp2),
            "TempSensorAvg": str(TempSensorAvg),
            "Pressure": str(Pressure),
            "SeaLevelPressure": str(SeaLevelPressure),
            "Humidity": str(Humidity),
            "TimeStamp": str(TimeStamp)
        }))

    cursor.close()

    return output
