from functions import downloadUrl
import os
##

def main():

    #Varibales
    color_codes = ['040','4W9','209','1K3','6X1','1K0','1F7','3t3','070']
    car_id = "368cedb3-a905-49e8-82f8-e09c20eca8a4"
    model_id = "5a2db31d-b461-471d-bc1b-e296864d310d"
    accessory_id = "17224";

    for color_code in color_codes:

        path = './result/color_accessories_images/'+ accessory_id +'/' + color_code

        #Start
        print ("====> START  -- %s" % color_code)

        #Make directory
        try:
            os.makedirs(path)
        except OSError:
            print ("====> DIRECTORY %s FAILED" % path)
        else:
            print ("====> CREATED %s DIRECTORY" % path)

            #Run
            for x in range(0,36):
                c = str(x)
                grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/accessories/' + accessory_id + '/width/1300/height/340/scale-mode/1/padding/0,0,140,135/background-colour/F0F0F0/image-quality/75/exterior-' + c +'_' + color_code +'.jpg'
                downloadUrl( grab_url, path+'/ac-' + accessory_id + '-exterior-'+ c +'_' + color_code +'.jpg' ) #Download file
                print ("====> GRAB %s" % x)

            print ("====> DONE  -- %s" % color_code)
            print ("================")
            print ("================")


if __name__ == '__main__':
    main()
