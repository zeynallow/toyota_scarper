from functions import downloadUrl
import os
##

def main():

    #Varibales
    # color_codes = ['6X3','1G3','8W9','8X8','218','3t3']#rav4 default
    color_codes = ['2RA','2QZ','2QY','2QJ'] #rav 4 style
    car_id = "575b2757-c42e-42ad-9236-7b001ad39b13"
    # model_id = "d1e5962a-77a4-4b45-a443-d70d60501b65" #rav4 default
    model_id = "3451ed15-3aec-4505-a275-b12dce5217b8" #rav 4 style


    for color_code in color_codes:

        path = './result/color_images/' + color_code

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
                grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/width/1300/height/340/scale-mode/1/padding/0,0,140,135/background-colour/F0F0F0/image-quality/75/exterior-' + c +'_' + color_code +'.jpg'
                downloadUrl( grab_url, path+'/exterior-'+ c +'_' + color_code +'.jpg' ) #Download file
                print ("====> GRAB %s" % x)

            print ("====> DONE  -- %s" % color_code)


if __name__ == '__main__':
    main()
