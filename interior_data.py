from functions import downloadUrl
import os
from pyquery import PyQuery
import mysql.connector

##

def main():

    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="root",
        database="toyota"
    )


    html = """<div class="slick-track  slick-animated" style="width: 704px; left: 0px; right: auto; margin-left: 0px; margin-right: auto;">
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current selected"><a class="or-swatch-link" href="Qara parça (FA20)"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/43c66fc4-eb54-450e-a15d-d85f9843a5df.JPG');"><span class="or-swatch-active"><i class="icon icon-ok " aria-hidden="true"></i></span></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Mavi tikişli qara Alkantara dərisi, HV Style Grade"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/2a4aa0ac-9985-45a5-bf02-630648873e0c.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Premium dəri – MONO - Hibrid - Boz haşiyə və tikişli QARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/321c821b-4c03-4927-89cf-246b9ebf955e.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Premium dəri – MONO - Hibrid - Boz haşiyə və tikişli QARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/30004f64-39b4-443c-9982-abf5cc996217.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Standart dəri – İki rəng çalarlı - Hibrid - BOZ + QARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/b7dcd11c-41c4-4b8f-b76f-9f8606d3a1ba.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Standart dəri – İki rəng çalarlı - Hibrid - Tünd-qəhvəyi tikişli QARA ALKANTARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/84e8e6a6-54a7-4490-8ef4-c57ba372e052.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Standart dəri – İki rəng çalarlı- Hibrid - TÜND-QƏHVƏYİ + QARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/ee0bf6c3-2c07-402b-af33-f96f80ecc63b.PNG');"></span></a></div>
                </div>
                <div class="or-swatches-upholstery slick-slide " style="width: 88px;">
                    <div class="or-swatch slick-current "><a class="or-swatch-link" href="Dəri dəst – Standart dəri – MONO - Hibrid - Boz haşiyə və tikişli QARA"><span class="or-swatch-item" style="background-image: url('//t1-carassets.toyota-europe.com/660861bf-12a2-4d05-9bc8-5da4e6492fc5.PNG');"></span></a></div>
                </div>
            </div>"""

    car_model_id="19"
    car_name="rav4"
    path = './result/'+car_name+'/interior/'

    #Make directory
    try:
        os.makedirs(path)
    except OSError:
        print ("====> DIRECTORY %s FAILED" % path)
    else:
        print ("====> CREATED %s DIRECTORY" % path)



    pq = PyQuery(html)

    for tag in pq('span.or-swatch-item'):
        _cl_image = pq(tag).attr('style')
        cl_name = pq(tag).closest('a.or-swatch-link').attr('href')

        cl_image= _cl_image.split("'",2) #split style code
        cl_file_name = cl_image[1].split('/',3); #file name

        downloadUrl( "https:"+ cl_image[1], path+'/' + cl_file_name[3]) #Download file

        #insert DB
        car_interiors = mydb.cursor()
        sql = "INSERT INTO car_interiors (car_model_id, name, icon) VALUES (%s, %s, %s)"
        val = (car_model_id, cl_name, "/cars/rav4/interior/"+cl_file_name[3])
        car_interiors.execute(sql, val)
        mydb.commit()

        print ("====> GRAB %s" % cl_name)



if __name__ == '__main__':
    main()
