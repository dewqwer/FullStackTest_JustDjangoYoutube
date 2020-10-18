# from imutils.video import VideoStream
# from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import sys
import datetime
from imutils.video import VideoStream
from imutils.video import FPS


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

path_log_DT3 = "C:/Users/Nuntuch  Thongyoo/Desktop/Github_Projects/INT353_Senior-Project/NUM-SHOW_BANDIT/model/people_counter/graduation_ceremony/output/log_program.txt"
path_log_NB5 = "C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUM-SHOW_BANDIT/model/people_counter/graduation_ceremony/output/log_program.txt"

path_purelog_DT3 = "C:/Users/Nuntuch  Thongyoo/Desktop/Github_Projects/INT353_Senior-Project/NUM-SHOW_BANDIT/model/people_counter/graduation_ceremony/output/purelog_program.txt"
path_purelog_NB5 = "C:/GithubProjects/Work of SIT.KMUTT/INT353/INT353_Senior-Project/NUM-SHOW_BANDIT/model/people_counter/graduation_ceremony/output/purelog_program.txt"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="path_vdo_input_NB5_0",
                help="path to optional input video file")
ap.add_argument("-fp", "--purelog", type=str, default=path_purelog_NB5,
                help="path_purelog")
ap.add_argument("-f", "--log", type=str, default=path_log_NB5,
                help="path_log")
ap.add_argument("-o", "--output", type=str, default="D:/output_01t.avi",
                help="path to optional output video file")
ap.add_argument("-ocw", "--outputOfcutwhite", type=str, default="D:/outputOfcutwhite.avi",  # outputOfcutwhite.MJPG
                help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.4,
                help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=1,
                help="# of skip frames between detections")


args = vars(ap.parse_args())