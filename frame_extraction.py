import cv2

def FrameCapture(path):
	# Path to video file
    cam = cv2.VideoCapture(path)

    # counter
    currentframe = 0
    count = 0
  
    while(True): 
        # reading from frame
        ret,frame = cam.read()
  
        if ret:
            # if video is still left continue creating images
            name = './Images/frame' + str(count) + '.jpg'
            #print ('Creating...' + name)
            
            # writing the extracted images
            if currentframe%30 ==0:
                cv2.imwrite(name, frame)
                print('Creating...' + name)
                count+=1

            currentframe += 1
        else:
            break
  
    cam.release()
    cv2.destroyAllWindows()
    #print(currentframe, count)
    return count
