# import the necessary packages
from library.counter import m_frame_management as mfm
from library.counter import m_frame_set_management as mfsm
from library.counter import crop_management as cm
from library.counter import filter_and_check_error_management as fem
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
# import cv



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
path_vdo_input_DT3_1t = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_1_Trim.mp4"
path_vdo_input_DT3_2 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_2.mp4"
path_vdo_input_DT3_3 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_3.mp4"
path_vdo_input_DT3_4 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_4_Trim.mp4"
path_vdo_input_DT3_5 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_5_Trim.mp4"
path_vdo_input_DT3_6 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_6.mp4"
path_vdo_input_DT3_7 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_7.mp4"
path_vdo_input_DT3_8 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_8_Trim.mp4"
path_vdo_input_DT3_1t8 = "D:/GithubProjects/INT353_Senior-Project/G_KMUTT_2561_P_1t8_Trim.mp4"

path_log_DT3 = "D:/m_frame_crop_arm_mean_lpft_current.txt"#"C:/GithubProjects/Work_Of_SIT.KMUTT/INT353/INT353_Senior-Project/NUMSHOW_BANDIT/model/people_counter/graduation_ceremony/output/log_program.txt"
path_log_NB5 = "D:/log_program.txt"#"C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUMSHOW_BANDIT/model/people_counter/graduation_ceremony/output/log_program.txt"

path_purelog_DT3 = "D:/m_frame_crop_peoplepass_flashcheck_mean_current.txt"#"C:/GithubProjects/Work_Of_SIT.KMUTT/INT353/INT353_Senior-Project/NUMSHOW_BANDIT/model/people_counter/graduation_ceremony/output/purelog_program.txt"
path_purelog_NB5 = "D:/purelog_program.txt"#"C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUMSHOW_BANDIT/model/people_counter/graduation_ceremony/output/purelog_program.txt"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default=path_vdo_input_DT3_1t8,
                help="path to optional input video file")

#sum log
# ap.add_argument("-sum_l", "--sumlog", type=str, default=path_sum_log_DT3,
                # help="path_sumlog")
#info log
# ap.add_argument("-m_fa_l", "--m_fa_log", type=str, default=path_mfa_log_DT3,
                # help="path_m_fa_log")
# ap.add_argument("-m_fa_lpft_l", "--m_fa_lpft_log", type=str, default=path_m_fa_lpft_og_DT3,
                # help="path_m_fa_lpft_log")
# ap.add_argument("-m_ferr", "--m_ferr", type=str, default=path_m_ferr_log_DT3,
                # help="path_log")
#status log
# ap.add_argument("-peo", "--m_fa_log", type=str, default=path_mfa_log_DT3,
                # help="path_m_fa_log")
# ap.add_argument("-m_fa_lpft_l", "--m_fa_lpft_log", type=str, default=path_m_fa_lpft_og_DT3,
                # help="path_m_fa_lpft_log")
# ap.add_argument("-m_ferr", "--m_ferr", type=str, default=path_m_ferr_log_DT3,
                # help="path_log")





ap.add_argument("-o", "--output", type=str, default="E:/output_1t8.avi",
                help="path to optional output video file")
ap.add_argument("-ocw", "--outputOfcropwhite", type=str, default="D:/outputOfcropwhite.avi",  # outputOfcropwhite.MJPG
                help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.4,
                help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=1,
                help="# of skip frames between detections")


args = vars(ap.parse_args())

# var_________Start_______________________________________________________________
mfsm_arm = mfsm.MFrameSetManagement()
m_frame_crop_arm_mean_set = mfsm_arm._initial_frame_crop_mean_set(15)
m_frame_crop_arm_mean_lpft_set = mfsm_arm._initial_frame_crop_mean_lpft_set(3)
status_up_down_slope_set = mfsm_arm._initial_status_up_down_slope_set(2)

m_frame_crop_arm_mean_lpft_current = 0
people_count = 0
fem_obj = fem.FilterAndCheckErrorManagement()
mfm_arm = mfm.MFrameManagement()




# var_________End_______________________________________________________________




i_mf_a = open("D:/info_log_mframe_arm_avg.txt", "a")
i_mf_a_lpft = open("D:/info_log_mframe_arm_avg_lpft.txt", "a")
i_mf_err = open("D:/info_log_mframe_err_avg.txt", "a")
i_suw = open("D:/info_slope_up_wave_count.txt", "a")
i_tf = open("D:/info_total_frame.txt", "a")




s_mf_err = open("D:/status_log_mframe_err_avg.txt", "a")
s_fl = open("D:/status_log_filter_low_value.txt", "a")
s_s = open("D:/status_slope.txt", "a")
s_cl = open("D:/status_counter_lock.txt", "a")




# f = open(str(args.get("log")), "a")


print("[INFO] loading model MOG2...")

if args.get("algo") == 'MOG2':
    backSub = cv2.createBackgroundSubtractorMOG2()
else:
    backSub = cv2.createBackgroundSubtractorKNN()

# if a video path was not supplied, grab a reference to the webcam
if not args.get("input", False):
    print("[INFO] starting video stream...")
    # # f.write("[INFO] starting video stream...\n")
    vs = VideoStream(src=0).start()
    time.sleep(2.0)




    i_mf_a.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_mf_a_lpft.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_mf_err.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_suw.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_tf.write("Start : "+str(datetime.datetime.now())+"___________________________________________")

    s_mf_err.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_fl.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_s.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_cl.write("Start : "+str(datetime.datetime.now())+"___________________________________________")



    i_mf_a.write("\n")
    i_mf_a_lpft.write("\n")
    i_mf_err.write("\n")
    i_suw.write("\n")
    i_tf.write("\n")

    s_mf_err.write("\n")
    s_fl.write("\n")
    s_s.write("\n")
    s_cl.write("\n")



    i_mf_a.write("[INFO] starting video stream...")
    i_mf_a_lpft.write("[INFO] starting video stream...")
    i_mf_err.write("[INFO] starting video stream...")
    i_suw.write("[INFO] starting video stream...")
    i_tf.write("[INFO] starting video stream...")

    s_mf_err.write("[INFO] starting video stream...")
    s_fl.write("[INFO] starting video stream...")
    s_s.write("[INFO] starting video stream...")
    s_cl.write("[INFO] starting video stream...")



    i_mf_a.write("\n")
    i_mf_a_lpft.write("\n")
    i_mf_err.write("\n")
    i_suw.write("\n")
    i_tf.write("\n")

    s_mf_err.write("\n")
    s_fl.write("\n")
    s_s.write("\n")
    s_cl.write("\n")










# otherwise, grab a reference to the video file
else:
    print("[INFO] opening video file...")
    # # f.write("[INFO] opening video file...\n")

    vs = cv2.VideoCapture(args["input"])
    if not vs.isOpened:
        print('Unable to open: ' + args.input)
        exit(0)
    

    i_mf_a.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_mf_a_lpft.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_mf_err.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_suw.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    i_tf.write("Start : "+str(datetime.datetime.now())+"___________________________________________")

    s_mf_err.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_fl.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_s.write("Start : "+str(datetime.datetime.now())+"___________________________________________")
    s_cl.write("Start : "+str(datetime.datetime.now())+"___________________________________________")



    i_mf_a.write("\n")
    i_mf_a_lpft.write("\n")
    i_mf_err.write("\n")
    i_suw.write("\n")
    i_tf.write("\n")

    s_mf_err.write("\n")
    s_fl.write("\n")
    s_s.write("\n")
    s_cl.write("\n")



    i_mf_a.write("[INFO] opening video file...  ")
    i_mf_a_lpft.write("[INFO] opening video file...  ")
    i_mf_err.write("[INFO] opening video file...  ")
    i_suw.write("[INFO] opening video file...  ")
    i_tf.write("[INFO] opening video file...  ")

    s_mf_err.write("[INFO] opening video file...  ")
    s_fl.write("[INFO] opening video file...  ")
    s_s.write("[INFO] opening video file...  ")
    s_cl.write("[INFO] opening video file...  ")

    i_mf_a.write(str(args["input"]))
    i_mf_a_lpft.write(str(args["input"]))
    i_mf_err.write(str(args["input"]))
    i_suw.write(str(args["input"]))
    i_tf.write(str(args["input"]))

    s_mf_err.write(str(args["input"]))
    s_fl.write(str(args["input"]))
    s_s.write(str(args["input"]))
    s_cl.write(str(args["input"]))



    i_mf_a.write("\n")
    i_mf_a_lpft.write("\n")
    i_mf_err.write("\n")
    i_suw.write("\n")
    i_tf.write("\n")

    s_mf_err.write("\n")
    s_fl.write("\n")
    s_s.write("\n")
    s_cl.write("\n")

# initialize the video writer (we'll instantiate later if need be)
writer = None
# writerOfcropwhite = None

# initialize the frame dimensions (we'll set them as soon as we read
# the first frame from the video)
W = None
H = None
# WOfcropwhite = None
# HOfcropwhite = None

# initialize the total number of frames processed thus far, along
# with the total number of objects that have moved either up or down
totalFrames = 0
# totalFramesOfcropwhite = 0
totalDown = 0
totalUp = 0

# start the frames per second throughput estimator
fps = FPS().start()
# fpsOfcropwhite = FPS().start()

# loop over frames from the video stream
while True:
    # grab the next c_frame and handle if we are reading from either
    # VideoCapture or VideoStream
    c_frame = vs.read()
    c_frame = c_frame[1] if args.get("input", False) else c_frame


    # if we are viewing a video and we did not grab a frame then we
    # have reached the end of the video
    if args["input"] is not None and c_frame is None:
        break

    # resize the frame to have a maximum width of 500 pixels (the
    # less data we have, the faster we can process it), then convert
    # the c_frame from BGR to RGB for dlib
    c_frame = imutils.resize(c_frame, width=500)
    rgb = cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)

    m_frame = backSub.apply(c_frame)
    
    cm_arm = cm.CropManagement()
    cm_arm._set_width_hight_x1_y1(15, 35, 155, 110,"MFrameCropArm")
    
    # m_frame_crop_arm = cm_arm._crop_form_m_frame(m_frame, 155, 110, 155+15, 110+35)
    m_frame_crop_arm = cm_arm._crop_form_m_frame_by_cm_obj(m_frame.copy())

    # c_frame = cm_arm._create_m_frame_line(c_frame, 155, 110, 155+15, 110+35,"MFrameCropArm")
    cl_frame = cm_arm._create_m_frame_line_by_cm_obj(c_frame.copy())


    cm_peoplepass_flashcheck = cm.CropManagement()
    cm_peoplepass_flashcheck._set_width_hight_x1_y1(90, 230, 170-45, 30,"PeoplePassCheckAndFlashCheck")

    # m_frame_crop_peoplepass_flashcheck = cm_peoplepass_flashcheck._crop_form_m_frame(m_frame, 170, 10, 170+45, 10+260 )
    m_frame_crop_peoplepass_flashcheck = cm_peoplepass_flashcheck._crop_form_m_frame_by_cm_obj(m_frame.copy())


    # c_frame = cm_peoplepass_flashcheck._create_m_frame_line(c_frame, 170, 10, 170+45, 10+260,"PeoplePassCheckAndFlashCheck")
    cl_frame = cm_peoplepass_flashcheck._create_m_frame_line_by_cm_obj(cl_frame)
    

    # mfm_arm = mfm.MFrameManagement()
    m_frame_crop_arm_mean_current = mfm_arm._find_avg_value_of_m_frame(m_frame_crop_arm)
    mfm_peoplepass_flashcheck = mfm.MFrameManagement()
    m_frame_crop_peoplepass_flashcheck_mean_current = mfm_peoplepass_flashcheck._find_avg_value_of_m_frame(m_frame_crop_peoplepass_flashcheck)


    
    
    # i_mf_a.write(str(m_frame_crop_arm_mean_current))
    # i_mf_a.write("\n")

    # i_mf_err.write(str(m_frame_crop_peoplepass_flashcheck_mean_current))
    # i_mf_err.write("\n")


# Create frame to shown on moniter 9*9_________Start____________________________________________________________________
    mc_frame = cl_frame.copy()
    mc_frame_crop_arm = cv2.cvtColor(m_frame_crop_arm,cv2.COLOR_BGR2RGB)
    # mc_frame[110 : 110+35,155 : 155+15 ] = mc_frame_crop_arm
    mc_frame[cm_arm.y1_crop_arm_frame : cm_arm.y2_crop_arm_frame,cm_arm.x1_crop_arm_frame : cm_arm.x2_crop_arm_frame ] = mc_frame_crop_arm

    mc_frame_crop_peoplepass_flashcheck = cv2.cvtColor(m_frame_crop_peoplepass_flashcheck,cv2.COLOR_BGR2RGB)
    # mc_frame[10 : 10+260,170 : 170+45 ] = mc_frame_crop_peoplepass_flashcheck
    mc_frame[cm_peoplepass_flashcheck.y1_crop_peoplepass_flashcheck_frame : cm_peoplepass_flashcheck.y2_crop_peoplepass_flashcheck_frame,cm_peoplepass_flashcheck.x1_crop_peoplepass_flashcheck_frame : cm_peoplepass_flashcheck.x2_crop_peoplepass_flashcheck_frame ] = mc_frame_crop_peoplepass_flashcheck
    
   
    mc_frame = cm_arm._create_m_frame_line(mc_frame,cm_arm.x1_crop_arm_frame,cm_arm.y1_crop_arm_frame,cm_arm.x2_crop_arm_frame,cm_arm.y2_crop_arm_frame,"MFrameCropArm")
  


    mc_a_frame = c_frame.copy()
    # mc_a_frame[110 : 110+35,155 : 155+15 ] = mc_frame_crop_arm
    mc_a_frame[cm_arm.y1_crop_arm_frame : cm_arm.y2_crop_arm_frame,cm_arm.x1_crop_arm_frame : cm_arm.x2_crop_arm_frame] = mc_frame_crop_arm
    

    mc_pf_frame = c_frame.copy()
    # mc_pf_frame[10 : 10+260,170 : 170+45 ] = mc_frame_crop_peoplepass_flashcheck
    mc_pf_frame[cm_peoplepass_flashcheck.y1_crop_peoplepass_flashcheck_frame : cm_peoplepass_flashcheck.y2_crop_peoplepass_flashcheck_frame,cm_peoplepass_flashcheck.x1_crop_peoplepass_flashcheck_frame : cm_peoplepass_flashcheck.x2_crop_peoplepass_flashcheck_frame] = mc_frame_crop_peoplepass_flashcheck



    # mc_sum_frame[x1,x2:y1,y2]
    mc_sum_frame = vs.read()
    mc_sum_frame = imutils.resize(c_frame, width=1500)
    rgb_sum = cv2.cvtColor(c_frame, cv2.COLOR_BGR2RGB)
    
    mc_sum_frame[0:281,0:500] = cl_frame.copy() #11
    mc_sum_frame[281:281+281,0:500] = cv2.cvtColor(m_frame.copy(),cv2.COLOR_BGR2RGB) #12
    mc_sum_frame[0:281,500:500+500] = mc_a_frame.copy() #21 
    mc_sum_frame[281:281+281,500:500+500] = mc_pf_frame.copy() #22
    mc_sum_frame[281+281:281+281+281,500:500+500] = 0 #23
    mc_sum_frame[281+281:281+281+281,0:500] = c_frame.copy() #13
    mc_sum_frame[281+281:281+281+281,500+500:500+500+500] = 0 #33
    mc_sum_frame[281:281+281,500+500:500+500+500] = 0 #32
    mc_sum_frame[0:281,500+500:500+500+500] = mc_frame.copy() #31

# Create frame to shown on moniter 9*9_________End____________________________________________________________________

    # f.write(str(m_frame_crop_arm_mean_current))
    # f.write(str(m_frame_crop_arm_mean_lpft_current))
    # f.write("\n")
    # fp.write(str(m_frame_crop_peoplepass_flashcheck_mean_current))
    # fp.write(str(m_frame_crop_arm_mean_current))
    # fp.write("\n")
    # print("B: "+str(m_frame_crop_arm_mean_current)+" E: "+str(m_frame_crop_peoplepass_flashcheck_mean_current))

    # fem_obj = fem.FilterAndCheckErrorManagement()
    people_pass_flash_check_status =  fem_obj._people_pass_flash_check(m_frame_crop_peoplepass_flashcheck_mean_current)



    if(people_pass_flash_check_status):
        print("people_pass_flash_check_status" + str(people_pass_flash_check_status))
        people_pass_flash_check_status = False
        # m_frame_crop_arm_mean_lpft_current = -1
    else : 
        #update value in avg arm set
        m_frame_crop_arm_mean_set = mfsm_arm._update_m_frame_crop_mean_set(m_frame_crop_arm_mean_current)
        #low pass filter 15 frame
        m_frame_crop_arm_mean_lpft_current = fem_obj._lowpassfilter_m_frame(m_frame_crop_arm_mean_set,15)
        #filter low value
        m_frame_crop_arm_mean_lpft_current = fem_obj._filter_low_value(m_frame_crop_arm_mean_lpft_current,30)
        #update value in lpft avg arm set
        m_frame_crop_arm_mean_lpft_set = mfsm_arm._update_m_frame_crop_mean_lpft_set(m_frame_crop_arm_mean_lpft_current)
        # CheckStatusUpDownSlope
        status_up_down_slope_current = mfsm_arm._check_status_up_down_slope()
        # print(str(status_up_down_slope_current))
        print("A: "+str(m_frame_crop_arm_mean_current)+" A_LPFT: "+str(m_frame_crop_arm_mean_lpft_current)+" E: "+str(m_frame_crop_peoplepass_flashcheck_mean_current))
        print("status_up_down_slope_current : "+str(status_up_down_slope_current))
        # update value in status_up_down_slope_set
        status_up_down_slope_set = mfsm_arm._update_status_up_down_slope(status_up_down_slope_current)
        #counter people
        people_count = mfsm_arm._counter()
        print("People Count : "+ str(people_count))
        print("_______________________________________________________________________________________________________")
        # f.write(str(m_frame_crop_arm_mean_lpft_current))
        # f.write("\n")
        # fp.write(str(m_frame_crop_peoplepass_flashcheck_mean_current))
        # fp.write("\n")




    # # Create window with freedom of dimensions
    # cv2.namedWindow("Color Frame", cv2.WINDOW_NORMAL)
    # # cv2.waitKey(0)
    # # Create window with freedom of dimensions
    # cv2.namedWindow("Monochrome Frame", cv2.WINDOW_NORMAL)
    # # cv2.waitKey(0)
    # # Create window with freedom of dimensions
    cv2.namedWindow("Sum Frame", cv2.WINDOW_NORMAL)
    # cv2.waitKey(0)

    # if the c_frame dimensions are empty, set them
    if W is None or H is None:
        # (H, W) = c_frame.shape[:2]
        (H, W) = mc_sum_frame.shape[:2]


    # if WOfcropwhite is None or HOfcropwhite is None:
    #     (HOfcropwhite, WOfcropwhite) = m_frame.shape[:2]

    # if we are supposed to be writing a video to disk, initialize
    # the writer
    if args["output"] is not None and writer is None:
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(args["output"], fourcc, 30,
                                 (W, H), True)

    # if args["outputOfcropwhite"] is not None and writerOfcropwhite is None:
    #     fourccOfcropwhite = cv2.VideoWriter_fourcc(*"MJPG")
    #     # fourccOfcropwhite = cv2.VideoWriter_fourcc(*'XVID')
    #     writerOfcropwhite = cv2.VideoWriter(args["outputOfcropwhite"], fourccOfcropwhite, 30,
    #                                        (WOfcropwhite, HOfcropwhite), True)

    # construct a tuple of information we will be displaying on the


    i_mf_a.write(str(mfsm_arm.m_frame_crop_mean_set[14]))
    i_mf_a_lpft.write(str(mfsm_arm.m_frame_crop_mean_lpft_set[2]))
    i_mf_err.write(str(mfm_peoplepass_flashcheck.m_frame_crop_mean))
    i_suw.write(str(mfsm_arm.status_up_count))
    i_tf.write(str(totalFrames))

    s_mf_err.write(str(fem_obj.people_pass_flash_check_status))
    s_fl.write(str(fem_obj.filter_low_value_status))
    s_s.write(str(mfsm_arm.status_up_down_slope_current))
    s_cl.write(str(mfsm_arm.status_count_lock))

    i_mf_a.write("\n")
    i_mf_a_lpft.write("\n")
    i_mf_err.write("\n")
    i_suw.write("\n")
    i_tf.write("\n")

    s_mf_err.write("\n")
    s_fl.write("\n")
    s_s.write("\n")
    s_cl.write("\n")


    info = [
        # ("[INFO] MF_A Set: ",str(mfsm_arm.m_frame_crop_mean_set)),
        
        ("[INFO] MF_A Set: ",str(mfsm_arm.m_frame_crop_mean_set)),
        ("[INFO] MF_A_LPFT Set: ",str(mfsm_arm.m_frame_crop_mean_lpft_set)),
        ("[INFO] MF_ERR : ",str(mfm_peoplepass_flashcheck.m_frame_crop_mean)),
        ("[INFO] MF_A_LPFT: ",str(mfsm_arm.m_frame_crop_mean_lpft_set[2])),
        ("[INFO] MF_A: ",str(mfsm_arm.m_frame_crop_mean_set[14])),
        ("People Counts", people_count),
        # ("People Counts", people_count),
        # ("[INFO] Total Frame: ", totalFrames),
        # ("[Status] People Pass or Flash: ",str(fem_obj.people_pass_flash_check_status)),
        # ("[INFO] Slope Up Wave Counts: ",str(mfsm_arm.status_up_count)),
        # ("[Status] Counter Lock Status: ",str(mfsm_arm.status_count_lock)),
        # ("[Status] Slope Current Status: ",str(mfsm_arm.status_up_down_slope_current)),
        # ("[Status] Slope Set Status: ",str(mfsm_arm.status_up_down_slope_set)),
        # ("[Status] Filter Low Value Status: ",str(fem_obj.filter_low_value_status)),
    

    ]

    info_2 = [

        ("[INFO] Total Error Count: ", str(mfsm_arm.error_count)),
        ("[INFO] Total Frame: ", totalFrames),
        ("[INFO] Wave Frame Counts: ",str(mfsm_arm.count_wave_set)),
        ("[INFO] Slope Up Wave Counts: ",str(mfsm_arm.status_up_count)),
        ("[Status] Counter Lock Status: ",str(mfsm_arm.status_count_lock)),
        ("[Status] Slope Current Status: ",str(mfsm_arm.status_up_down_slope_current)),
        ("[Status] Slope Set Status: ",str(mfsm_arm.status_up_down_slope_set)),
        ("[Status] Filter Low Value Status: ",str(fem_obj.filter_low_value_status)),
        ("[Status] People Pass or Flash: ",str(fem_obj.people_pass_flash_check_status)),
        ("[Status] Count In Peak Wave: ",str(mfsm_arm.count_in_peak_wave)),
        ("People Counts", people_count),
    # ("   MF_A          " + "MF_A_LPFT          ","MF_ERR   "),
    # ( str("%.5f" % mfsm_arm.m_frame_crop_mean_set[14]) + str("%.5f" % mfsm_arm.m_frame_crop_mean_lpft_set[2]),"          "+str("%.5f" % mfm_peoplepass_flashcheck.m_frame_crop_mean)),
    # ("   MF_A          " + "MF_A_LPFT          ","MF_ERR   "),
    # ("   MF_A          " + "MF_A_LPFT          ","MF_ERR   "),
    # ("   MF_A          " + "MF_A_LPFT          ","MF_ERR   "),
    # ("   MF_A          " + "MF_A_LPFT          ","MF_ERR   "),
    # ("MF_A Set: ",str(mfsm_arm.m_frame_crop_mean_set)),
    ]

    info_3 = [
        ("People Counts", people_count),
    ]

    # loop over the info tuples and draw them on our c_frame
    for (i, (k, v)) in enumerate(info):
        text = "{}: {}".format(k, v)
        cv2.putText(mc_sum_frame, text, (500+30, H - ((i * 40) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        
    for (i, (k, v)) in enumerate(info_2):
        text = "{}: {}".format(k, v)
        cv2.putText(mc_sum_frame, text, ((500*2)+30, H - ((i * 40) +100)), # + (281*2)-50
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
          
    for (i, (k, v)) in enumerate(info_3):
        text = "{}: {}".format(k, v)
        cv2.putText(mc_sum_frame, text, (30, H - ((i * 20) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # for (i, (k, v)) in enumerate(info_crop_white):
    #     text = "{}: {}".format(k, v)
    #     cv2.putText(m_frame, text, (10, H - ((i * 20) + 20)),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    # check to see if we should write the frame to disk
    if writer is not None:
        writer.write(mc_sum_frame)
        # writer.write(c_frame)


    # if writerOfcropwhite is not None:
    #     writerOfcropwhite.write(m_frame)



    

    # show the output c_frame
    # cv2.imshow("Color Frame", c_frame)
    # cv2.imshow('Monochrome Frame', m_frame)
    ## cv2.imshow('MonochromeCompoundColor Frame', mc_frame)
    # cv2.imshow('MonochromeCompoundColor A Frame', mc_a_frame)
    # cv2.imshow('MonochromeCompoundColor PF Frame', mc_pf_frame)
    cv2.imshow('Sum Frame', mc_sum_frame)



    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # increment the total number of frames processed thus far and
    # then update the FPS counter
    fps.update()
    totalFrames += 1
    # fpsOfcropwhite.update()

# stop the timer and display FPS information
fps.stop()
# fpsOfcropwhite.stop()
print("[INFO] Total Frame: "+ str(totalFrames))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] Total People Count: ", people_count)



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


# f.close()
# fp.close()



i_mf_a.write("End : "+str(datetime.datetime.now())+"___________________________________________")
i_mf_a_lpft.write("End : "+str(datetime.datetime.now())+"___________________________________________")
i_mf_err.write("End : "+str(datetime.datetime.now())+"___________________________________________")
i_suw.write("End : "+str(datetime.datetime.now())+"___________________________________________")
i_tf.write("End : "+str(datetime.datetime.now())+"___________________________________________")

s_mf_err.write("End : "+str(datetime.datetime.now())+"___________________________________________")
s_fl.write("End : "+str(datetime.datetime.now())+"___________________________________________")
s_s.write("End : "+str(datetime.datetime.now())+"___________________________________________")
s_cl.write("End : "+str(datetime.datetime.now())+"___________________________________________")



i_mf_a.write("\n")
i_mf_a_lpft.write("\n")
i_mf_err.write("\n")
i_suw.write("\n")
i_tf.write("\n")

s_mf_err.write("\n")
s_fl.write("\n")
s_s.write("\n")
s_cl.write("\n")


i_mf_a.write("People Count : "+ str(people_count))
i_mf_a_lpft.write("People Count : "+ str(people_count))
i_mf_err.write("People Count : "+ str(people_count))
i_suw.write("People Count : "+ str(people_count))
i_tf.write("People Count : "+ str(people_count))

s_mf_err.write("People Count : "+ str(people_count))
s_fl.write("People Count : "+ str(people_count))
s_s.write("People Count : "+ str(people_count))
s_cl.write("People Count : "+ str(people_count))



i_mf_a.write("\n")
i_mf_a_lpft.write("\n")
i_mf_err.write("\n")
i_suw.write("\n")
i_tf.write("\n")

s_mf_err.write("\n")
s_fl.write("\n")
s_s.write("\n")
s_cl.write("\n")







i_mf_a.close()
i_mf_a_lpft.close()
i_mf_err.close()
i_suw.close()
i_tf.close()

s_mf_err.close()
s_fl.close()
s_s.close()
s_cl.close()