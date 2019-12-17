from functions import downloadUrl
import os
from pyquery import PyQuery
import mysql.connector
import json
import urllib.request, json
import ssl
import random
import string
##

def main():

    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="root",
        database="toyota"
    )

    #Varibales
    car_slug="new-c-hr"

    color_codes = [
    '2NK',
    '2NH',
    '2TJ',
    '2NB',
    '2TH',
    '2TB',
    '2TA',
    '2NA'
    ]

    ow_color_codes= [
    '46',
    '44',
    '54',
    '43',
    '51',
    '55',
    '52',
    '48'
    ]

    car_id = "a3fc91d5-2942-4653-92e9-9f530b396e41" #c-hr

    model_ids = [
    '23d2bfcf-fd96-4a48-ac2a-b87ae7fb6c4e',
    ]

    ow_model_ids=[
    '71',
    ]

    m_count = 0
    count = 0


    path = './result/color_images/'


    #Make directory
    try:
        os.makedirs(path)
    except OSError:
        print ("====> DIRECTORY %s FAILED" % path)
    else:
        print ("====> CREATED %s DIRECTORY" % path)

    for model_id in model_ids:
        print ("====> START MODEL  -- %s" % model_id)
        for color_code in color_codes:

            ow_color_code = ow_color_codes[count]
            ow_model_id = ow_model_ids[m_count]

            #db query
            get_car_color_id = mydb.cursor()
            get_car_color_id.execute("SELECT id FROM car_colors WHERE color_id = "+ow_color_code+" and model_id="+ ow_model_id)
            _car_color_id = get_car_color_id.fetchone()
            car_color_id = str(_car_color_id[0])


            #Start
            print ("====> START  -- %s" % color_code)


            #Run
            for x in range(0,36):
                c = str(x)
                img_name = '' + car_color_id + '-exterior-'+ c +'_' + color_code +'.jpg'
                grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/width/1300/height/340/scale-mode/1/padding/0,0,140,135/background-colour/F0F0F0/image-quality/75/exterior-' + c +'_' + color_code +'.jpg'
                downloadUrl( grab_url, path+'/'+ img_name ) #Download file

                # insert DB
                car_color_images = mydb.cursor()
                sql = "INSERT INTO car_color_images (car_color_id,accessory_id,image) VALUES (%s, %s, %s)"
                val = (car_color_id, 0, '/cars/'+ car_slug +'/color_images/'+ img_name)
                car_color_images.execute(sql, val)
                mydb.commit()

                print ("====> GRAB %s" % x)

            count+=1
            print ("====> DONE  -- %s" % color_code)

        m_count+=1
        count=0
        print ("====> DONE MODEL  -- %s" % model_id)


if __name__ == '__main__':
    main()
