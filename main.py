# Main algorithm
# Created by Oscar SIU #

# 1. Extract video frames
# 2. Calculate focal length
# 3. Import LRF dis
# 4. find image dimension
# 5. Obtain GSD

import os
from PIL import Image
from frame_extraction import FrameCapture
from distance_estimation import *
from LRF import *

VIDEO_PATH = ".\Mini2\DJI_0083.mp4"
STORE_PATH = ".\Images"

csv_file = "data.csv"

# For 1/2" sensor
#SENSOR_W = 6.4 # Camera sensor width (mm)
#SENSOR_H = 4.8 # Camera sensor height (mm)

# Focal length for M2EA visual camera
#CROP_FACTOR = 5.41 
#EFL = 24 # 35mm equivalent focal length (mm)

# For 1/2.3" sensor
SENSOR_W = 6.17 # Camera sensor width (mm)
SENSOR_H = 4.55 # Camera sensor height (mm)

# Focal length for Mini 2 visual camera
CROP_FACTOR = 5.64 
EFL = 24 # 35mm equivalent focal length (mm)

FOCAL_LEN = EFL/CROP_FACTOR # Camera true focal length (mm)


if __name__ == '__main__':
    try:  
    # creating a folder named data
        if not os.path.exists(STORE_PATH):
            os.makedirs(STORE_PATH)
  
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
    
    frame_num = FrameCapture(VIDEO_PATH)
    i=0

    load_csv(csv_file)

    while i < frame_num:
        name = r"C:\Users\Oscar SIU\Desktop\GSD estimation\Images\frame" + str(i) + ".jpg"
        print('frame'+ str(i) + '.jpg: ')
        DIM_W, DIM_H = find_dim(name)
        #FLIGHT_DIS = float(get_dis(i))
        FLIGHT_DIS = 5.16
        gsd_calculation(FLIGHT_DIS, FOCAL_LEN, SENSOR_W, SENSOR_H, DIM_W, DIM_H)
        i += 1
