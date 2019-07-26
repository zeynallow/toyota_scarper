import os
import shutil

def main():
    path = './result/'

    shutil.rmtree(path)
    
    print ("====> DELETED %s" % path)



if __name__ == '__main__':
    main()