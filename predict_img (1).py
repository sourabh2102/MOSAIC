import cv2
import numpy as np
import pickle

model = pickle.load(open('new_emnist_model.sav', 'rb'))
finalans=[]

def predict_(image):
    y=x+r
    g=ol+eorl


def extract_segments(img, pad=10, area=100, threshold=150, ker=1):
    # thresholding the image
    ret, thresh1 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('thres',thresh1)
    #cv2.waitKey(0)
    # Negative tranform gray levels (background becomes black)
    thresh1 = 255 - thresh1
    img = 255 - img
    #cv2.imshow('thres', thresh1)
    #cv2.waitKey(0)
    # connected component labelling
    output = cv2.connectedComponentsWithStats(thresh1, 4)
    #print(output)
    final = []
    temp2 = output[2]
    temp2 = temp2[temp2[:, 4] > area]
    temp1 = np.sort(temp2[:, 0])
    kernel = np.ones([ker, ker])

    for i in range(1, temp2.shape[0]):
        cord = np.squeeze(temp2[temp2[:, 0] == temp1[i]])

        num = np.pad(thresh1[cord[1]:cord[1] + cord[3], cord[0]:cord[0] + cord[2]],pad)
        #num=cv2.erode(num,(2 ,2),iterations=2)
        #num = 255 - num
        #cv2.imshow('image', num)
        #cv2.waitKey(0)
        #num = rescale_segment(num, (40,40))
        num=cv2.resize(num,(28,28))
        #cv2.imshow('num',num)
        #cv2.waitKey(0)
        num = num.astype('float32')
        num=num/255
        final.append(num)
        predict_(num)
    return final

def predict_image_(img,strides=False,small_width=False):
    print("working")
    finalans.clear()
    img= cv2.resize(img,(500,300))
    #cv2.imshow('frame',img)
    #cv2.waitKey(100)
    if(small_width):
        img = cv2.erode(img, (3, 3), iterations=3)
        #cv2.imshow('frame3', img)
        #cv2.waitKey(0)
    if(strides):
        img=cv2.dilate(img,(3,3),iterations=3)
        #cv2.imshow('frame2',img)
        #cv2.waitKey(0)
        img=cv2.erode(img,(3,3),iterations=2)
        #cv2.imshow('frame3',img)
        #cv2.waitKey(0)

    img = cv2.dilate(img, (3, 3), iterations=3)
    #cv2.imshow('frame2', img)
    #cv2.waitKey(0)
    img = cv2.erode(img, (3, 3), iterations=3)
    #cv2.imshow('frame3', img)
    #cv2.waitKey(0)

    segments = extract_segments(img, 10, threshold=150, area=200, ker=1)
    #print(finalans)
    sc = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r', 't']

    st=""
    s=[]
    for x in finalans:
        if (x <= 9):
            c = 48 + x
            st=st+chr(c)
            s.append(chr(c))
        elif (x <= 35):
            c = 65 + x - 10
            st = st + chr(c)
            s.append(chr(c))
        else:
            ind = int(x) - 36
            st = st + chr(c)
            s.append(sc[ind])


    cv2.destroyAllWindows()
    #print(s)
    return st
