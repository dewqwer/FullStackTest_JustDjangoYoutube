# import the necessary packages
from __future__ import print_function
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import sys
import datetime

# construct the argument parse and parse the arguments
path_vdo_input_NB5_0 = "D:/GithubProjects/INT353/oneMin.mp4"
path_vdo_input_NB5_1 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_1.mp4"
path_vdo_input_NB5_1t = "D:/GithubProjects/INT353/G_KMUTT_2561_P_1t.mp4"
path_vdo_input_NB5_2 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_2.mp4"
path_vdo_input_NB5_3 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_3.mp4"
path_vdo_input_NB5_4 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_4.mp4"
path_vdo_input_NB5_5 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_5.mp4"
path_vdo_input_NB5_6 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_6.mp4"
path_vdo_input_NB5_7 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_7.mp4"
path_vdo_input_NB5_8 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_8.mp4"
path_vdo_input_NB5_1t8 = "D:/GithubProjects/INT353/G_KMUTT_2561_P_1t8_Trim.mp4"

path_vdo_input_DT3_0 = "D:/GithubProjects/INT353_Senior-Project/oneMin.mp4"
path_vdo_input_DT3_1 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_1.mp4"
path_vdo_input_DT3_1t = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_1t.mp4"
path_vdo_input_DT3_2 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_2.mp4"
path_vdo_input_DT3_3 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_3.mp4"
path_vdo_input_DT3_4 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_4.mp4"
path_vdo_input_DT3_5 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_5.mp4"
path_vdo_input_DT3_6 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_6.mp4"
path_vdo_input_DT3_7 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_7.mp4"
path_vdo_input_DT3_8 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_8.mp4"
path_vdo_input_DT3_1t8 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_1t8_Trim.mp4"

path_log_DT3 = "C:/Users/Nuntuch  Thongyoo/Desktop/Github_Projects/INT353_Senior-Project/NUM-SHOW_BANDIT/people_counter/graduation_ceremony/output/log_program.txt"
path_log_NB5 = "C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUM-SHOW_BANDIT/people_counter/graduation_ceremony/output/log_program.txt"

path_purelog_DT3 = "C:/Users/Nuntuch  Thongyoo/Desktop/Github_Projects/INT353_Senior-Project/NUM-SHOW_BANDIT/people_counter/graduation_ceremony/output/purelog_program.txt"
path_purelog_NB5 = "C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUM-SHOW_BANDIT/people_counter/graduation_ceremony/output/purelog_program.txt"


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,default= path_vdo_input_DT3_1t8, 
	help="path to optional input video file")
ap.add_argument("-o", "--output", type=str,default="D:/output_01t.avi",
	help="path to optional output video file")
ap.add_argument("-ocw", "--outputOfcutwhite", type=str,default="D:/outputOfcutwhite.avi", #outputOfcutwhite.MJPG
	help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.4,
	help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=1,
	help="# of skip frames between detections")

args = vars(ap.parse_args())
SetFrameCount = 0#15
PeopleCount = 0
PeopleErrorCount = 0
ErrorFrameSetCount = 0
PeopleErrorCount_PeoplePass = 0
PeopleErrorCount_ShortFlash = 0
PeopleErrorCount_LongFlash = 0
detect_status = 0
rounds = 0
fgMaskCutMean_befor_minus1 = 0
fgMaskCutMean_befor_minus2 = 0
fgMaskCutMean_befor_minus3 = 0
fgMaskCutMean_befor_minus4 = 0
fgMaskCutMean_befor_minus5 = 0
fgMaskCutMean_befor_minus6 = 0
fgMaskCutMean_befor_minus7 = 0
fgMaskCutMean_befor_minus8 = 0
fgMaskCutMean_befor_minus9 = 0
fgMaskCutCheckErrMean = 0
fgMaskCutCheckErrMean_befor_minus1 = 0
fgMaskCutCheckErrMean_befor_minus2 = 0
fgMaskCutCheckErrMean_befor_minus3 = 0
fgMaskCutCheckErrMean_befor_minus4 = 0
fgMaskCutCheckErrMean_befor_minus5 = 0
fgMaskCutCheckErrMean_befor_minus6 = 0
fgMaskCutCheckErrMean_befor_minus7 = 0
fgMaskCutCheckErrMean_befor_minus8 = 0
fgMaskCutCheckErrMean_befor_minus9 = 0

detect_status = 0 #0 = ไม่สนใจ 1 = สนใจ 

fp = open(path_purelog_DT3, "a") 
f = open(path_log_DT3, "a")
f.write("\n")
f.write("\n")
f.write("\n")
f.write("_____Start Log " + str(datetime.datetime.now()) +" _____\n")
f.write(args.get("input"))
f.write("\n")

fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.write("_____Start Log " + str(datetime.datetime.now()) +" _____\n")
fp.write(args.get("input"))
fp.write("\n")


# ___________________________Start Cut White Code___________________________________
print("[INFO] loading model MOG2...")

# if args.algo == 'MOG2':
if args.get("algo") == 'MOG2':
    backSub = cv2.createBackgroundSubtractorMOG2()
else:
    backSub = cv2.createBackgroundSubtractorKNN()
# ___________________________End Cut White Code___________________________________

# if a video path was not supplied, grab a reference to the webcam
if not args.get("input", False):
	print("[INFO] starting video stream...")
	f.write("[INFO] starting video stream...\n")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

	
# otherwise, grab a reference to the video file
else:
	print("[INFO] opening video file...")
	f.write("[INFO] opening video file...\n")
	# vs = cv2.VideoCapture(args["input"])#เปิด VDO ธรรมดา
	# vs = cv2.VideoCapture(cv2.samples.findFileOrKeep(args.input)) #เปิด VDO แบบตัดสีขาว
	# vs = cv2.VideoCapture(cv2.samples.findFileOrKeep(args.get("input"))) #เปิด VDO แบบตัดสีขาว
	vs = cv2.VideoCapture(args["input"])
	if not vs.isOpened:
		print('Unable to open: ' + args.input)
		exit(0)

# initialize the video writer (we'll instantiate later if need be)
writer = None
writerOfcutwhite = None

# initialize the frame dimensions (we'll set them as soon as we read
# the first frame from the video)
W = None
H = None
WOfcutwhite = None
HOfcutwhite = None

# initialize the total number of frames processed thus far, along
# with the total number of objects that have moved either up or down
totalFrames = 0
totalFramesOfcutwhite = 0
totalDown = 0
totalUp = 0

# start the frames per second throughput estimator
fps = FPS().start()
fpsOfcutwhite = FPS().start()

# loop over frames from the video stream
while True:
	# grab the next frame and handle if we are reading from either
	# VideoCapture or VideoStream
	frame = vs.read()
	frame = frame[1] if args.get("input", False) else frame
	# fgMask = backSub.apply(frame)

	# if we are viewing a video and we did not grab a frame then we
	# have reached the end of the video
	if args["input"] is not None and frame is None:
		break

	# resize the frame to have a maximum width of 500 pixels (the
	# less data we have, the faster we can process it), then convert
	# the frame from BGR to RGB for dlib
	# frame = imutils.resize(frame, width=500)
	frame = imutils.resize(frame, width=500)
	fgMask = backSub.apply(frame)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# fgMask = imutils.resize(fgMask, width=500)
	# print(fgMask.shape)

	if totalFramesOfcutwhite % args["skip_frames"] == 0:

		rgbOfcutwhite = cv2.cvtColor(fgMask, cv2.COLOR_GRAY2RGB) #แปลงเป็นสีขาว ดำ  ไบนารี่

		cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
		cv2.putText(frame, str(vs.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
					cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))

#_____________________________________Start CutCheckPeoplePass/Long Flash_____________________________________________
		
		fgMaskCutCheckPeoplePass1 = fgMask[50:80,420:450] #120:150 170:190 , 450:420 ,240:270

		fgMaskCutCheckPeoplePass1Mean =	fgMaskCutCheckPeoplePass1.flatten().mean()

		# fgMask[0:30,0:30] = fgMaskCutCheckPeoplePass1


		fgMaskCutCheckPeoplePass2 = fgMask[120:150,420:450] #120:150 170:190 , 450:420

		fgMaskCutCheckPeoplePass2Mean =	fgMaskCutCheckPeoplePass2.flatten().mean()

		
		fgMaskCutCheckPeoplePass3 = fgMask[170:190,420:450] #120:150 170:190 , 450:420  X(232 60) _30_

		fgMaskCutCheckPeoplePass3Mean =	fgMaskCutCheckPeoplePass3.flatten().mean()


#_____________________________________End CutCheckPeoplePass/Long Flash_____________________________________________


#_____________________________________Start CutCheckPeoplePass/Long Flash_____________________________________________
		
		fgMaskCutCheckPeoplePass4 = fgMask[50:80,200:230] #120:150 170:190 , 450:420 ,240:270

		fgMaskCutCheckPeoplePass4Mean =	fgMaskCutCheckPeoplePass4.flatten().mean()

		# fgMask[0:30,0:30] = fgMaskCutCheckPeoplePass1


		fgMaskCutCheckPeoplePass5 = fgMask[120:150,200:230] #120:150 170:190 , 450:420

		fgMaskCutCheckPeoplePass5Mean =	fgMaskCutCheckPeoplePass5.flatten().mean()

		
		fgMaskCutCheckPeoplePass6 = fgMask[170:190,200:230] #120:150 170:190 , 450:420  X(232 60) _30_

		fgMaskCutCheckPeoplePass6Mean =	fgMaskCutCheckPeoplePass6.flatten().mean()

# ------------------------------------------------------------------------------------------------------------------

		fgMaskCutCheckPeoplePass7 = fgMask[50:80,60:90] #120:150 170:190 , 450:420 ,240:270

		fgMaskCutCheckPeoplePass7Mean =	fgMaskCutCheckPeoplePass7.flatten().mean()

		# fgMask[0:30,0:30] = fgMaskCutCheckPeoplePass1


		fgMaskCutCheckPeoplePass8 = fgMask[120:150,60:90] #120:150 170:190 , 450:420

		fgMaskCutCheckPeoplePass8Mean =	fgMaskCutCheckPeoplePass8.flatten().mean()

		
		fgMaskCutCheckPeoplePass9 = fgMask[170:190,60:90] #120:150 170:190 , 450:420  X(232 60) _30_

		fgMaskCutCheckPeoplePass9Mean =	fgMaskCutCheckPeoplePass9.flatten().mean()


#_____________________________________End CutCheckPeoplePass/Long Flash_____________________________________________








# 171 125
# 171 122
		fgMaskCut = fgMask[115:145,150:190] 

		fgMaskCutMean =	fgMaskCut.flatten().mean()
		
		# fgMask[0:(145-115),0:(190-150)] = fgMaskCut


		print(fgMaskCutMean)
		fp.write(str(fgMaskCutMean))
		fp.write("\n")



		fgMaskCutCheckErr = fgMask[15:45,190:230] 

		fgMaskCutCheckErrMean =	fgMaskCutCheckErr.flatten().mean()
		
		fgMask[0:(30),0:(40)] = fgMaskCutCheckErr

			
		if(detect_status == 1):
			SetFrameCount = SetFrameCount + 1

		if(fgMaskCutMean > 80 #70 #80
		and	fgMaskCutMean > fgMaskCutMean_befor_minus1 
		and fgMaskCutMean_befor_minus1 > fgMaskCutMean_befor_minus2 
		and fgMaskCutMean_befor_minus2 > fgMaskCutMean_befor_minus3 
		and detect_status == 0 ):	
			detect_status = 1 
			PeopleCount = PeopleCount + 1
			SetFrameCount = SetFrameCount + 1
			print("rounds : " ,rounds)
			f.write("rounds : " )
			f.write(str(rounds))
			f.write("\n")
			
			# eprint(fgMaskCutCheckErrMean)
			print("fgMaskCutCheckErrMean : ",fgMaskCutCheckErrMean)
			f.write("fgMaskCutCheckErrMean : ")
			f.write(str(fgMaskCutCheckErrMean))
			f.write("\n")
			
			# print(fgMaskCutCheckErrMean)
			print(fgMaskCutMean,fgMaskCutMean_befor_minus1,fgMaskCutMean_befor_minus2,fgMaskCutMean_befor_minus3)
			print("_________________________________Count!!! ",PeopleCount,"_________________________________")

			f.write(str(fgMaskCutMean))
			f.write(str(fgMaskCutMean_befor_minus1))
			f.write(str(fgMaskCutMean_befor_minus2))
			f.write(str(fgMaskCutMean_befor_minus3))
			
			f.write("\n")
			
			f.write("_________________________________Count!!! ")
			f.write(str(PeopleCount))
			f.write(" _________________________________")
		
			f.write("\n")




		# if(fgMaskCutMean - fgMaskCutMean_befor_minus1 >= 100
		if(fgMaskCutMean - fgMaskCutMean_befor_minus1 >= 100
		and fgMaskCutMean_befor_minus1 - fgMaskCutMean_befor_minus2 <= 50
		and fgMaskCutMean_befor_minus2 - fgMaskCutMean_befor_minus3 <= 50 
		and detect_status == 1): 
			detect_status = 0
			PeopleCount = PeopleCount - 1
			PeopleErrorCount = PeopleErrorCount + 1
			PeopleErrorCount = PeopleErrorCount_ShortFlash + 1
			print("_________________________________Detect Noise (Short Flash) !!! ",PeopleCount,"______________________________")
			f.write("_________________________________Detect Noise (Short Flash) !!! ")
			f.write(PeopleCount)
			f.write("______________________________")
			f.write("\n")


		if((fgMaskCutMean+fgMaskCutMean_befor_minus1+fgMaskCutMean_befor_minus2)/3 >= 253
		and detect_status == 1): 
			detect_status = 0
			PeopleCount = PeopleCount - 1
			PeopleErrorCount = PeopleErrorCount + 1
			PeopleErrorCount_PeoplePass = PeopleErrorCount_PeoplePass + 1
			print("_________________________________Detect Noise (Other People Pass) !!! ",PeopleCount,"______________________________")
			f.write("_________________________________Detect Noise (Other People Pass) !!! ")
			f.write(str(PeopleCount))
			f.write("______________________________")
			f.write("\n")

		if((fgMaskCutCheckErrMean
		+fgMaskCutCheckErrMean_befor_minus1
		+fgMaskCutCheckErrMean_befor_minus2
		+fgMaskCutCheckErrMean_befor_minus3
		+fgMaskCutCheckErrMean_befor_minus4
		# +fgMaskCutCheckErrMean_befor_minus5
		# +fgMaskCutCheckErrMean_befor_minus6
		# +fgMaskCutCheckErrMean_befor_minus7
		# +fgMaskCutCheckErrMean_befor_minus8
		# +fgMaskCutCheckErrMean_befor_minus9
		# )/10 >= fgMaskCutCheckErrMean-2
		)/5 >= fgMaskCutCheckErrMean-2 

		and
		(fgMaskCutCheckErrMean
		+fgMaskCutCheckErrMean_befor_minus1
		+fgMaskCutCheckErrMean_befor_minus2
		+fgMaskCutCheckErrMean_befor_minus3
		+fgMaskCutCheckErrMean_befor_minus4
		# +fgMaskCutCheckErrMean_befor_minus5
		# +fgMaskCutCheckErrMean_befor_minus6
		# +fgMaskCutCheckErrMean_befor_minus7
		# +fgMaskCutCheckErrMean_befor_minus8
		# +fgMaskCutCheckErrMean_befor_minus9
		)/5 <= fgMaskCutCheckErrMean+2
		and detect_status == 1 and fgMaskCutCheckErrMean > 80
		): 
			detect_status = 0
			PeopleCount = PeopleCount - 1
			PeopleErrorCount = PeopleErrorCount + 1
			PeopleErrorCount_LongFlash = PeopleErrorCount_LongFlash + 1
			print("_________________________________Detect Noise (Long Flash) !!! ",PeopleCount,"______________________________")
			f.write("_________________________________Detect Noise (Long Flash) !!! ")
			f.write(str(PeopleCount))
			f.write("______________________________")
			f.write("\n")


		if(fgMaskCutMean < 80 #80
		and	fgMaskCutMean < fgMaskCutMean_befor_minus1 
		and fgMaskCutMean_befor_minus1 < fgMaskCutMean_befor_minus2 
		and fgMaskCutMean_befor_minus2 < fgMaskCutMean_befor_minus3 
		and detect_status == 1 
		and SetFrameCount >= 15
		):	
			SetFrameCount = 0
			detect_status = 0
			print("_________________________________clear!!!_______________________________________________________")
			f.write("_________________________________clear!!!_______________________________________________________")
			f.write("\n")
		
		# else if(SetFrameCount >):

		if(fgMaskCutMean < 80 #80
		and	fgMaskCutMean < fgMaskCutMean_befor_minus1 
		and fgMaskCutMean_befor_minus1 < fgMaskCutMean_befor_minus2 
		and fgMaskCutMean_befor_minus2 < fgMaskCutMean_befor_minus3 
		and detect_status == 1 
		and SetFrameCount <= 7 # #9 #12
		):	
			SetFrameCount = 0
			detect_status = 0
			ErrorFrameSetCount = ErrorFrameSetCount + 1
			PeopleErrorCount = PeopleErrorCount + 1
			PeopleCount = PeopleCount - 1
			print("________________________detect error frame set___clear!!!_______________________________________________________")
			f.write("________________________detect error frame set___clear!!!_______________________________________________________")
			f.write("\n")

		rounds = rounds + 1
		if(rounds != 0 ):
			# fgMaskCutMean_befor_minus10 = fgMaskCutMean_befor_minus9
			# fgMaskCutMean_befor_minus9 = fgMaskCutMean_befor_minus8
			# fgMaskCutMean_befor_minus8 = fgMaskCutMean_befor_minus7
			# fgMaskCutMean_befor_minus7 = fgMaskCutMean_befor_minus6
			# fgMaskCutMean_befor_minus6 = fgMaskCutMean_befor_minus5
			# fgMaskCutMean_befor_minus5 = fgMaskCutMean_befor_minus4
			# fgMaskCutMean_befor_minus4 = fgMaskCutMean_befor_minus3
			fgMaskCutMean_befor_minus3 = fgMaskCutMean_befor_minus2
			fgMaskCutMean_befor_minus2 = fgMaskCutMean_befor_minus1
			fgMaskCutMean_befor_minus1 = fgMaskCutMean

			fgMaskCutCheckErrMean_befor_minus9 = fgMaskCutCheckErrMean_befor_minus8
			fgMaskCutCheckErrMean_befor_minus8 = fgMaskCutCheckErrMean_befor_minus7
			fgMaskCutCheckErrMean_befor_minus7 = fgMaskCutCheckErrMean_befor_minus6
			fgMaskCutCheckErrMean_befor_minus6 = fgMaskCutCheckErrMean_befor_minus5
			fgMaskCutCheckErrMean_befor_minus5 = fgMaskCutCheckErrMean_befor_minus4
			fgMaskCutCheckErrMean_befor_minus4 = fgMaskCutCheckErrMean_befor_minus3
			fgMaskCutCheckErrMean_befor_minus3 = fgMaskCutCheckErrMean_befor_minus2
			fgMaskCutCheckErrMean_befor_minus2 = fgMaskCutCheckErrMean_befor_minus1
			fgMaskCutCheckErrMean_befor_minus1 = fgMaskCutCheckErrMean

	cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
	# cv2.waitKey(0)
	cv2.namedWindow("FG Mask", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
	# cv2.waitKey(0)

	# if the frame dimensions are empty, set them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	if WOfcutwhite is None or HOfcutwhite is None:
		(HOfcutwhite, WOfcutwhite) = fgMask.shape[:2]

	# if we are supposed to be writing a video to disk, initialize
	# the writer
	if args["output"] is not None and writer is None:
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args["output"], fourcc, 30,
			(W, H), True)

	if args["outputOfcutwhite"] is not None and writerOfcutwhite is None:
		# fourccOfcutwhite = cv2.VideoWriter_fourcc(*"MJPG")
		fourccOfcutwhite = cv2.VideoWriter_fourcc(*'XVID')
		writerOfcutwhite = cv2.VideoWriter(args["outputOfcutwhite"], fourccOfcutwhite, 30,
			(WOfcutwhite, HOfcutwhite), True)




	# construct a tuple of information we will be displaying on the
	# frame
	info = [
		("People Counts", PeopleCount),
		# ("CWM_0", fgMaskCutMean,"CWM_-1", fgMaskCutMean_befor_minus1,"CWM_-2", fgMaskCutMean_befor_minus2,"CWM_-3", fgMaskCutMean_befor_minus3,),
		# ("CWM_0", fgMaskCutMean),
		# ("Status", detect_status),
	]

	info_cut_white = [
		("People Counts", PeopleCount),
		("Total Detect Error Counts", PeopleErrorCount),
		("Detect Error Counts (People Pass)", PeopleErrorCount_PeoplePass),
		("Detect Error Counts (Short Flash)", PeopleErrorCount_ShortFlash),
		("Detect Error Counts (Long Flash)", PeopleErrorCount_LongFlash),
		("Detect Error Counts (ErrorFrameSetCount)", ErrorFrameSetCount),

		("CWM_0", fgMaskCutMean),
		# ("CWM_-1", fgMaskCutMean_befor_minus1),
		# ("CWM_-2", fgMaskCutMean_befor_minus2),
		# ("CWM_-3", fgMaskCutMean_befor_minus3),
		("Status", detect_status),
	]
	


	# loop over the info tuples and draw them on our frame
	for (i, (k, v)) in enumerate(info):
		text = "{}: {}".format(k, v)
		cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
	
	for (i, (k, v)) in enumerate(info_cut_white):
		text = "{}: {}".format(k, v)
		cv2.putText(fgMask, text, (10, H - ((i * 20) + 20)),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


	# check to see if we should write the frame to disk
	if writer is not None:
		writer.write(frame)

	# show the output frame
	cv2.imshow("Frame", frame)
	cv2.imshow('FG Mask', fgMask)

	# f.write("People Count : ",PeopleCount," Status : ",detect_status ," CWM_0", fgMaskCutMean,"\n")
	f.write("People Count : ")
	f.write(str(PeopleCount))
	f.write(" Status : ")
	f.write(str(detect_status))
	f.write(" CWM_0 : ")
	f.write( str(fgMaskCutMean))
	f.write("\n")
	


	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# increment the total number of frames processed thus far and
	# then update the FPS counter
	totalFrames += 1
	totalFramesOfcutwhite += 1
	fps.update()
	fpsOfcutwhite.update()

# stop the timer and display FPS information
fps.stop()
fpsOfcutwhite.stop()
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("P1EP:293 P2EP:535 P3EP529")
print("[INFO] elapsed time Ofcutwhite: {:.2f}".format(fpsOfcutwhite.elapsed()))
print("[INFO] approx. FPS Ofcutwhite: {:.2f}".format(fpsOfcutwhite.fps()))
print("[INFO] Total People Count: " , PeopleCount)
print("[INFO] Total People Error Count: " , PeopleErrorCount)
print("[INFO] Detect Error Counts (People Pass)", PeopleErrorCount_PeoplePass)
print("[INFO] Detect Error Counts (Short Flash)", PeopleErrorCount_ShortFlash)
print("[INFO] Detect Error Counts (Long Flash)", PeopleErrorCount_LongFlash)
print("[INFO] Detect Error Counts (ErrorFrameSetCount)", ErrorFrameSetCount)

f.write("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
f.write("\n")
f.write("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
f.write("\n")
f.write("P1EP:293 P2EP:535 P3EP529")
f.write("\n")
f.write("[INFO] elapsed time Ofcutwhite: {:.2f}".format(fpsOfcutwhite.elapsed()))
f.write("\n")
f.write("[INFO] approx. FPS Ofcutwhite: {:.2f}".format(fpsOfcutwhite.fps()))
f.write("\n")
f.write("[INFO] Total People Count: " + str(PeopleCount))
f.write("\n")
f.write("[INFO] Total People Error Count: " + str(PeopleErrorCount))
f.write("\n")
f.write("[INFO] Detect Error Counts (People Pass)"+ str(PeopleErrorCount_PeoplePass))
f.write("\n")
f.write("[INFO] Detect Error Counts (Short Flash)"+ str(PeopleErrorCount_ShortFlash))
f.write("\n")
f.write("[INFO] Detect Error Counts (Long Flash)"+ str(PeopleErrorCount_LongFlash))
f.write("\n")
f.write("[INFO] Detect Error Counts (ErrorFrameSetCount)"+ str(ErrorFrameSetCount))
f.write("\n")

f.write("_____End Log " + str(datetime.datetime.now())  + " _____\n")
f.write("\n")
f.write("\n")
f.write("\n")
f.close()




fp.write("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
fp.write("\n")
fp.write("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
fp.write("\n")
fp.write("P1EP:293 P2EP:535 P3EP529")
fp.write("\n")
fp.write("[INFO] elapsed time Ofcutwhite: {:.2f}".format(fpsOfcutwhite.elapsed()))
fp.write("\n")
fp.write("[INFO] approx. FPS Ofcutwhite: {:.2f}".format(fpsOfcutwhite.fps()))
fp.write("\n")
fp.write("[INFO] Total People Count: " + str(PeopleCount))
fp.write("\n")
fp.write("[INFO] Total People Error Count: " + str(PeopleErrorCount))
fp.write("\n")
fp.write("[INFO] Detect Error Counts (People Pass)"+ str(PeopleErrorCount_PeoplePass))
fp.write("\n")
fp.write("[INFO] Detect Error Counts (Short Flash)"+ str(PeopleErrorCount_ShortFlash))
fp.write("\n")
fp.write("[INFO] Detect Error Counts (Long Flash)"+ str(PeopleErrorCount_LongFlash))
fp.write("\n")
fp.write("[INFO] Detect Error Counts (ErrorFrameSetCount)"+ str(ErrorFrameSetCount))
fp.write("\n")

fp.write("_____End Log " + str(datetime.datetime.now())  + " _____\n")
fp.write("\n")
fp.write("\n")
fp.write("\n")
fp.close()




# check to see if we need to release the video writer pointer
if writer is not None:
	writer.release()

# if we are not using a video file, stop the camera video stream
if not args.get("input", False):
	vs.stop()

# otherwise, release the video file pointer
else:
	vs.release()

# close any open windows
cv2.destroyAllWindows()
