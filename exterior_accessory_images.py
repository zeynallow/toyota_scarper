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
    car_slug="rav4"

    color_codes = [
    # '040',
    # '6X3',
    '1G3',
    '8W9',
    '8X8',
    '218',
    '3T3',
    '070'
    ]

    ow_color_codes= [
    # '5',
    # '14',
    '15',
    '16',
    '17',
    '18',
    '12',
    '13'
    ]

    car_id = "fe635412-d9a4-40dd-8965-d8e09cf1751e" #rav-4

    model_ids = [
    # 'd1e5962a-77a4-4b45-a443-d70d60501b65',
    # '34a98906-f669-4921-a2d8-f402c9358a06',
    # 'b152ad23-b832-41a1-8d88-c063cb2ca46b',
    # 'd5f1f740-0308-459d-9aab-145590c4a77c',
    # '92169201-3ecd-41e8-a62f-c3c80e2e0ec0',

    # 'df99bc49-fcbf-45a8-bab5-5053a59fb03f',
    # 'ded7b7be-4ad4-4e99-97b2-946a80a652d6',
    # 'c87a3f97-31e6-4c05-8799-d0d4f2810652',
    # 'bfcb8133-b1bc-4a5e-a338-7ac69b6e9be5',
    '1953b2aa-5968-4401-b81c-3ed7956febcc',
    '08bea019-8821-4288-b15a-ca576fe70097',
    '1f7f04e7-857f-4171-ae24-904b76f6dd81'
    ]

    #START  -- 1G3
    ##FILE SAVED:  ./result/color_images//249-17068-exterior-0_1G3.jpg

    ow_model_ids=[
    # '8',
    # '9',
    # '10',
    # '11',
    # '12',

    # '13',
    # '14',
    # '15',
    # '16',
    '17',
    '18',
    '19'
    ]

    accessories_id = [
    '17065',
    '17083',
    '17068',
    '17066',
    '17067'
    ]


    ow_accessories_id = [
    '110',
    '799',
    '111',
    '112',
    '113',
    ]

    m_count = 0
    a_count = 0
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
        for accessory_id in accessories_id:
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

                    img_name = '' + car_color_id + '-'+ accessory_id +'-exterior-'+ c +'_' + color_code +'.jpg'
                    grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/accessories/' + accessory_id + '/width/1300/height/340/scale-mode/1/padding/0,0,140,135/background-colour/F0F0F0/image-quality/75/exterior-' + c +'_' + color_code +'.jpg'
                    downloadUrl( grab_url, path+'/'+ img_name ) #Download file

                    # insert DB
                    car_color_images = mydb.cursor()
                    sql = "INSERT INTO car_color_images (car_color_id,accessory_id,image) VALUES (%s, %s, %s)"
                    val = (car_color_id, ow_accessories_id[a_count], '/cars/'+ car_slug +'/color_images/'+ img_name)
                    car_color_images.execute(sql, val)
                    mydb.commit()

                    print ("====> GRAB %s" % x)
                #range end

                count+=1
                print ("====> DONE  -- %s" % color_code)
                #color_codes for end

            count=0
            a_count+=1
            print ("====> DONE ACCESSORY  -- %s" % accessory_id)
            #accessories_id for end

        m_count+=1
        count=0
        a_count=0
        print ("====> DONE MODEL  -- %s" % model_id)
        #model end


if __name__ == '__main__':
    main()
