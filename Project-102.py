import cv2
import dropbox
import time
import random

startTime=time.time()

def Take_snapshot():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videocaptureobject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        startTime=time.time
        result=False

    print("Snapshot Taken")

    videocaptureobject.release()
    cv2.destroyAllWindows()
    return img_name

def uploadFile(img_name):
    accessToken="W9J2M1sZu-MAAAAAAAAAASMUFbLdpnYWTCEReGMBKfWtY_l_Ewzl_JWRd7RI95fQ"
    file=img_name
    file_from=file
    file_to="/newFolder1/"+(img_name)
    dbx=dropbox.Dropbox(accessToken)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
 
def main():
    while(True):
        if((time.time()-startTime)>=15):
            name=Take_snapshot()
            uploadFile(name)

main()            