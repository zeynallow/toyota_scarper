from functions import downloadUrl
import os
from pyquery import PyQuery
import mysql.connector
import json
import urllib.request, json
import ssl
import random
import string


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def get_cat_id(name):
    if name == "Eksteryer":
       return "2"

    if name == "İnteryer":
       return "1"

    if name == "Aksesuarlar":
       return "3";


def main():

    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="root",
        database="toyota"
    )

    car_id="2"
    car_name="rav4"
    path = './result/'+car_name+'/gallery'
    api_url = 'https://www.toyota.az/api/data/section/gallery/path/new-cars/'+car_name+'/index.json'

    #Make directory
    # try:
    #     os.makedirs(path)
    # except OSError:
    #     print ("====> DIRECTORY %s FAILED" % path)
    # else:
    #     print ("====> CREATED %s DIRECTORY" % path)

    with urllib.request.urlopen(api_url, context=ssl._create_unverified_context()) as url:
        data = json.loads(url.read().decode())

        for section in data['sections']:
            category_id = get_cat_id(section['name'])

            for slide in section['slides']:
                is_video = 0
                srcLg = 'https:'+ slide['srcLg']
                srcThumbnail = 'https:' + slide['srcThumbnail']
                srcSm = 'https:' + slide['srcSm']

                lg_file_name = 'lg_' + randomString(12) + '.jpg'
                thumb_file_name = 'thumb_' + randomString(12) + '.jpg'
                sm_file_name = 'sm_' + randomString(12) + '.jpg'

                downloadUrl( srcLg, path+'/' + lg_file_name) #Download file
                downloadUrl( srcThumbnail, path+'/' + thumb_file_name) #Download file
                downloadUrl( srcSm, path+'/' + sm_file_name) #Download file

                lg_ac_name = '/cars/'+car_name+'/gallery/'+ lg_file_name
                thumb_ac_name = '/cars/'+car_name+'/gallery/'+ thumb_file_name
                sm_ac_name = '/cars/'+car_name+'/gallery/'+ sm_file_name

                #insert DB
                car_galleries = mydb.cursor()
                sql = "INSERT INTO car_galleries (car_id,gallery_category_id,srcLg,srcThumbnail,srcSm,isVideo) VALUES (%s, %s, %s,%s, %s, %s)"
                val = (car_id, category_id, lg_ac_name,thumb_ac_name,sm_ac_name,is_video)
                car_galleries.execute(sql, val)
                mydb.commit()

                print ("DONE!!!")


if __name__ == '__main__':
    main()
