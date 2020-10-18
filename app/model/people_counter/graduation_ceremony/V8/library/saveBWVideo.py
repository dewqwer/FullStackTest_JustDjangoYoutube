import cv2
import numpy as np
import cv2 as cv
import argparse

# path_vdo_input_DT3_DTDew = "C:/Users/Dew2018/Desktop/60130500120/Project/code/oneMin.mp4"
path_vdo_input_DT3_DTDew = "C:/Users/Dew2018/Downloads/G_KMUTT_2561_P_1_Trim.mp4"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default=path_vdo_input_DT3_DTDew,
                help="path to optional input video file")
ap.add_argument("-o", "--output", type=str, default="C:/Users/Dew2018/Desktop/60130500120/Project/Output_BW/output_01t.avi",
                help="path to optional output video file")
ap.add_argument("-ocw", "--outputOfcutwhite", type=str, default="C:/Users/Dew2018/Desktop/60130500120/Project/Output_BW/outputOfcutwhite.avi",  # outputOfcutwhite.MJPG
                help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.4,
                help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=1,
                help="# of skip frames between detections")

args = vars(ap.parse_args())

cap = cv.VideoCapture(args["input"])
ret, frame = cap.read()
if ret is False:
    print("Cannot read video stream")
    exit()

W = None
H = None


if W is None or H is None:
    (H, W) = frame.shape[:2]

fourcc = cv.VideoWriter_fourcc(*"DIVX")
# fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')

# fourcc = cv.VideoWriter_fourcc(*"MJPG")
myvideo = cv.VideoWriter(args["output"], fourcc, 30,
                         (W, H), True)

# ใช้ lib createBackgroundSubtractorMOG2()

# fgbg = cv.createBackgroundSubtractorMOG2()

# while(True):
#     ret, frame = cap.read()
#     if ret:
#         fgmask = fgbg.apply(frame)
#         frame = cv.cvtColor(fgmask, cv.COLOR_GRAY2RGB)
#         myvideo.write(frame)  # Save it
#         cv.imshow('Background Subtraction', fgmask)
#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break  # q to quit
#     else:
#         break  # EOF

# cap.release()
# myvideo.release()
# cv.destroyAllWindows()


# ใช้ lib BackgroundSubtractorGMG()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# initializing subtractor
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()

    # applying on each frame
    fgmask = fgbg.apply(frame)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
