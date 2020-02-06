Opencv version: 3.4.2, if the version is higher than this the program will not work as the SIFT algorithm functions are not included in them.

To check the opencv version follow the steps below:
1) Open your Python command line
2) Type : >>> import cv2
          >>> cv2.__version__
3) The next line will show the current version of opencv installed on your system
>>> import cv2
>>> cv2.__version__
>>> '3.4.2'

After checking if you have the right version of opencv, download the database from the given link and follow the steps to run the program.

DATABASE link: https://www.kaggle.com/grassknoted/asl-alphabet


after downloading the database, extract the folders "asl_alphabet_test" and "asl_alphabet_test" to any location.

change the path in line 36 to the path of the images in asl_alphabet_test, replace the backward slashes in the path with forward slashes in the code to avoid any errors.

After making the necessary changes, run the program from command line using the command "python sift.py".
