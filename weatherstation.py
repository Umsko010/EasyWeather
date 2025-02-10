#!/usr/bin/python3

import os
import sys
import time
import mysql.connector

path = 'data.txt'


def write_database():  # Database Code
    with open(path, "r") as fileobject:
        text = fileobject.read()
        data = text.split(';')
        id = data[0]
        location = data[1]
        uv = data[2]
        date1 = data[3]
        temp = data[4]
        date2 = data[5]
        pressure = data[6]
        date3 = data[7]
        db = mysql.connector.connect(user='Jonas',
                                     password='Seelisches1',
                                     host='192.168.10.165',
                                     database='easyweather')
        
        db2 = mysql.connector.connect(user='easyweather',
                                     password='Seelisches1',
                                     host='192.168.10.223',
                                     database='db_se')

        print("Writing to Database.........")
        cursor = db.cursor()
        cursor2 = db2.cursor() 
        add_UV = ("INSERT INTO sensor_data "
                  "(sensor_type, value, value_timestamp, satellite_id) "
                  "VALUES (%s, %s, %s, %s)")
        data_UV = ('UV', uv, date1, id)
        
        add_TEMP = ("INSERT INTO sensor_data "
                  "(sensor_type, value, value_timestamp, satellite_id) "
                  "VALUES (%s, %s, %s, %s)")
        data_TEMP = ('Temperatur', temp, date2, id)
        
        add_PRESSURE = ("INSERT INTO sensor_data "
                  "(sensor_type, value, value_timestamp, satellite_id) "
                  "VALUES (%s, %s, %s, %s)")
        data_PRESSURE = ('Luftdruck', pressure, date3, id)
        cursor.execute(add_UV, data_UV)
        cursor.execute(add_TEMP, data_TEMP)
        cursor.execute(add_PRESSURE, data_PRESSURE)
        cursor2.execute(add_UV, data_UV)
        cursor2.execute(add_TEMP, data_TEMP)
        cursor2.execute(add_PRESSURE, data_PRESSURE)
        db.commit()
        db2.commit()
        print("Closing Database.........")
        cursor.close()
        db.close()
        cursor2.close()
        db2.close()
        print("DONE!")


def main():
    try:
        modification_time = os.path.getmtime(path)
        while 1:
            modification_time2 = os.path.getmtime(path)
            print(modification_time)
            print("\n"+str(modification_time2))
            if modification_time == modification_time2:
                time.sleep(30)
            else:
                print("Connecting to Database.........")
                write_database()
                modification_time = os.path.getmtime(path)
                time.sleep(30)

    except OSError:
        print("Path: " + path + " does not exists or is inaccessible")
        sys.exit()


if __name__ == '__main__':
    main()

