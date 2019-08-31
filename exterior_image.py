from functions import downloadUrl
import os
##

def main():

    #Varibales
    color_codes = ['040','202','218','4V8','3R3','1G3','1F7','070','4X4','221']
    car_id = "db50c897-99e4-4035-85ad-dfc1722b4ce1" #prado
    model_id = "09c451a6-40c4-6590-8676-6e3034c722b1" #1
    # model_id = "48e765ee-b959-6590-b707-676c03f5e921" #2


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
                downloadUrl( grab_url, path+'/a-exterior-'+ c +'_' + color_code +'.jpg' ) #Download file
                print ("====> GRAB %s" % x)

            print ("====> DONE  -- %s" % color_code)


if __name__ == '__main__':
    main()
