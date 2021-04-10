from detection.detect import  Retina_Detector
from alignmet_four_point import Alignment
import cv2
import glob
if __name__ == '__main__':
    X=Retina_Detector()
    A=Alignment()
    for i, path in enumerate(glob.glob("test/*")):
        image=cv2.imread(path)
        print(path)
        # for i in range(100):
        #     t1=time.time()
        #     dets=X.detect(image)
        #     print(len(dets))
        #     print(time.time()-t1)
        boxes,landms=X.detect(image)
        print("len boxes",len(boxes))
        for box,land in zip(boxes,landms):
            # print(box)
            # print(land)
            img=A.align(image,[(land[0],land[1]),(land[2],land[3]),(land[6],land[7]),(land[8],land[9])])    
            name = "test"
            # img1=image[box[0]:box[1],box[2]:box[3]]
            # cv2.imshow("image",image)
            image = cv2.line(image, (land[0], land[1]), (land[2], land[3]), color=(255, 0, 0), thickness=2)
            image = cv2.line(image, (land[2], land[3]), (land[6], land[7]), color=(255, 0, 0), thickness=2)
            image = cv2.line(image, (land[0], land[1]), (land[8], land[9]), color=(255, 0, 0), thickness=2)
            image = cv2.line(image, (land[6], land[7]), (land[8], land[9]), color=(255, 0, 0), thickness=2)
            cv2.imwrite(f"image_{i}.jpg", image)
            cv2.imwrite(f"test_{i}.jpg", img)
            # cv2.imshow(name, img)
            # cv2.imshow("box",img1)
            # cv2.waitKey(0)
            # 1/0
           

    

