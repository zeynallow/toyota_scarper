from functions import downloadUrl
import os
##

def main():

    #Varibales
    color_codes = ['040','218','3T6','1G3','8X2','4R8','1D6']
    car_id = "071f3137-e5a6-4e3c-824d-57a19f89a7d7" #helix
    model_id = "456758c3-fe68-446e-8801-c25d76035543" #1

    accessories_id = ['11617','11620']

    for color_code in color_codes:
        for accessory_id in accessories_id:

            path = './result/color_accessories_images/'+ accessory_id +'/' + color_code

            #Start
            print ("====> START  -- %s" % color_code)
            print ("====> START  -- %s" % accessory_id)

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
                    # print (grab_url)

        print ("====> DONE  -- %s" % color_code)
        print ("================")
        print ("================")


if __name__ == '__main__':
    main()
