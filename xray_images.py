from functions import downloadUrl
import os
##

def main():

    #Varibales
    color_code = "040" #first color code
    car_id = "368cedb3-a905-49e8-82f8-e09c20eca8a4"
    model_id = "5a2db31d-b461-471d-bc1b-e296864d310d"



    path = './result/xray/' + color_code

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
            grab_url='https://images.toyota-europe.com/az/product-token/' + car_id +'/vehicle/' + model_id + '/width/1300/height/340/scale-mode/1/padding/0,0,140,135/background-colour/F0F0F0/image-quality/75/xray-safety-exterior-' + c +'_' + color_code +'.jpg'
            downloadUrl( grab_url, path+'/xray-safety-exterior-'+ c +'_' + color_code +'.jpg' ) #Download file
            print ("====> GRAB %s" % x)

        print ("====> DONE  -- %s" % color_code)


if __name__ == '__main__':
    main()
