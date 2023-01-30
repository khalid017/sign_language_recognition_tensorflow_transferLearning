import os
import uuid #for naming image files
import cv2
import time

IMAGES_PATH = "F:/test/RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages"

labels=['hello','thanks','yes','no']
number_images=10

for label in labels:
    parent_dir="F:/test/RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages/"+label
    os.mkdir(parent_dir)
    
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    print('collecting images for {}' .format(label))
    time.sleep(5)
    for imgnum in range(number_images):
        ret,frame = cap.read()
        imagename=os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(imgnum).format(str(uuid.uuid1())))
        print(imagename)
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(4)

        if cv2.waitKey(1) and 0xFF ==  ord('q'):
            break 
    cap.release()
    cv2.destroyAllWindows()


