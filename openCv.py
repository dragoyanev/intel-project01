import argparse
import cv2
import numpy as np
from datetime import datetime
import time

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args

def capture_stream(args):
    ### Handle image, video or webcam
    # Create a flag for single images
    image_flag = False
    # Check if the input is a webcam
    #if args.i == 'CAM':
     #   args.i = 0
    #el
    if args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        image_flag = True

    ### Get and open video capture
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)

    # Create a video writer for the output video
    if not image_flag:
        # The second argument should be `cv2.VideoWriter_fourcc('M','J','P','G')`
        # on Mac, and `0x00000021` on Linux
        # 100x100 to match desired resizing
        fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
        out = cv2.VideoWriter('out.mp4', fourcc, 30, (640,480))
    else:
        out = None
    oldTime = time.time()
    
    
    
    print(oldTime)

    # Process frames until the video ends, or process is exited
    while cap.isOpened():
        # Read the next frame
        flag, frame = cap.read()
        if not flag:
            print("Frame not read")
            break
        else:
            print("Frame read")

        key_pressed = cv2.waitKey(60)

        ### TODO: Re-size the frame to 100x100
        print(type(frame))
        print(frame.size)
        print(frame.shape)
        currTime = time.time()
        dt = currTime - oldTime

        oldTime = currTime
        print(dt*1000)
        #frame = cv2.resize(frame, (100,100))

        ###       Add Canny Edge Detection to the frame, 
        ###       with min & max values of 100 and 200
        ###       Make sure to use np.dstack after to make a 3-channel image
        '''
        frame = cv2.Canny(frame, 100, 200)
        frame = np.dstack((frame, frame, frame))
        '''
        ### Write out the frame, depending on image or video
        if image_flag:
            cv2.imwrite('output_image.jpg', frame)
        else:
            out.write(frame)
        # Break if escape key pressed
        if key_pressed == 27:
            break

    ### Close the stream and any windows at the end of the application
    if not image_flag:
        out.release()
    cap.release()

    cv2.destroyAllWindows()



def main():
    args = get_args()
    print(args.i)
    capture_stream(args)


if __name__ == "__main__":
    main()