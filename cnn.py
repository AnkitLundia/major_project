import cv2
import numpy as np 
from keras.preprocessing import image
#from tensorflow.keras.model import load_model
import tensorflow as tf

classifier = tf.keras.models.load_model('C:/Users/Ankit/Desktop/reference/project/Source Code/Trained_model.h5',compile=False)
#img1 = cv2.imread('C:Users/Ankit/Desktop/reference/project/Source Code/SampleGestures/lol.png')
def test(img1):
	#img = image.load_img(img2, target_size=(64,64))
	img2 = cv2.resize(img1, (64,64))
	img = image.img_to_array(img2)
	img = np.expand_dims(img, axis = 0)
	#img = cv2.resize(img, (64,64))
	result = classifier.predict(img)
	if result[0][0] == 1:
	    return 'A'
	elif result[0][1] == 1:
	    return 'B'
	elif result[0][2] == 1:
	    return 'C'
	elif result[0][3] == 1:
	    return 'D'
	elif result[0][4] == 1:
	    return "del"
	elif result[0][5] == 1:
	    return 'E'
	elif result[0][6] == 1:
	    return 'F'
	elif result[0][7] == 1:
	    return 'G'
	elif result[0][8] == 1:
	    return 'H'
	elif result[0][9] == 1:
	    return 'I'
	elif result[0][10] == 1:
	    return 'J'
	elif result[0][11] == 1:
	    return 'K'
	elif result[0][12] == 1:
	    return 'L'
	elif result[0][13] == 1:
	    return 'M'
	elif result[0][14] == 1:
	    return 'N'
	elif result[0][15] == 1:
	    return ' '
	elif result[0][16] == 1:
	    return 'O'
	elif result[0][17] == 1:
	    return 'P'
	elif result[0][18] == 1:
	    return 'Q'
	elif result[0][19] == 1:
	    return 'R'
	elif result[0][20] == 1:
	    return 'S'
	elif result[0][21] == 1:
	    return "space"
	elif result[0][22] == 1:
	    return 'T'
	elif result[0][23] == 1:
	    return 'U'
	elif result[0][24] == 1:
	    return 'V'
	elif result[0][25] == 1:
	    return 'W'
	elif result[0][26] == 1:
		return 'X'
	elif result[0][27] == 1:
		return 'Y'
	elif result[0][28] == 1:
		return 'Z'



cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    height, width = frame.shape[:2]

    top_left_x = int (width / 3)
    top_left_y = int ((height / 2) + (height / 4))
    bottom_right_x = int ((width / 3) * 2)
    bottom_right_y = int ((height / 2) - (height / 4))

    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), 255, 3)

    cropped = frame[bottom_right_y:top_left_y , top_left_x:bottom_right_x]

    frame = cv2.flip(frame,1)

    char= test(cropped)
   # cv2.putText(frame,str(matches),(450,450), cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),1)

    threshold = 10

    #char = 'a'
    cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
    cv2.putText(frame,char,(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
    cv2.imshow('Sign detection ', frame)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()
