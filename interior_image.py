from functions import downloadUrl
import os
import mysql.connector
##

def main():

    #db connect
    mydb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        passwd="root",
        database="toyota"
    )

    #Varibales
    color_code = "218" #default color code
    car_id = "db50c897-99e4-4035-85ad-dfc1722b4ce1" #prado
    model_id = "f16e299d-991f-6590-9860-ab4e2a45d845" #toyota model id, comfort
    o_model_id = "30" #our model id
    o_car_name="land-cruiser-prado"

    #store path
    path = './result/interior_images'

    #Make directory
    try:
        os.makedirs(path)
    except OSError:
        print ("====> DIRECTORY %s FAILED" % path)
    else:
        print ("====> CREATED %s DIRECTORY" % path)

    #db query
    get_interior = mydb.cursor()
    get_interior.execute("SELECT * FROM car_interiors WHERE car_model_id = "+o_model_id)
    result_interior = get_interior.fetchall()

    #db records
    for c_interior in result_interior:
        get_color_code = c_interior[2].split('(',1)
        car_interior_id = c_interior[0]
        #get color code
        if len(get_color_code) > 1:
            _get_color_code = get_color_code[1].split(')',1)
            get_interior_color = _get_color_code[0]; #interior color code

            #Start
            print ("====> START  -- %s" % get_interior_color)

            #Run
            for x in range(0,3):
                c = str(x)
                file_name = o_model_id + '-static-day-interior-'+ c +'_' + color_code +'_'+ get_interior_color +'.jpg';
                grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/width/2460/height/1094/scale-mode/1/padding/0/background-colour/F0F0F0/image-quality/60/static-day-interior-' + c +'_' + color_code +'_'+ get_interior_color +'.jpg'
                downloadUrl( grab_url, path+'/'+ file_name ) #Download file
                print(grab_url)
                #insert DB
                car_interiors = mydb.cursor()
                sql = "INSERT INTO car_interior_images (car_interior_id, image) VALUES (%s, %s)"
                val = (car_interior_id, "/cars/"+ o_car_name + "/interior_images/"+file_name)
                car_interiors.execute(sql, val)
                mydb.commit()

                print ("====> GRAB %s" % x)

                print ("====> DONE  -- %s" % color_code)


if __name__ == '__main__':
    main()
