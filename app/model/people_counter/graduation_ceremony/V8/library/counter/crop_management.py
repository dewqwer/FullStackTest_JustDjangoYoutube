import numpy as np
import cv2

class CropManagement:
	width_crop_arm_frame = 0
	hight_crop_arm_frame = 0
	x1_crop_arm_frame = 0
	x2_crop_arm_frame = 0
	y1_crop_arm_frame = 0
	y2_crop_arm_frame = 0
	width_crop_peoplepass_flashcheck_frame = 0
	hight_crop_peoplepass_flashcheck_frame = 0
	x1_crop_peoplepass_flashcheck_frame = 0
	x2_crop_peoplepass_flashcheck_frame = 0
	y1_crop_peoplepass_flashcheck_frame = 0
	y2_crop_peoplepass_flashcheck_frame = 0
	type_of_cropframe = "Unknow"


	def __init__(self):
		pass

# _by_hand

	def _set_width_hight_x1_y1(self,width,height,x1,y1,type_of_cropframe):

		if type_of_cropframe == "MFrameCropArm" :
			CropManagement.width_crop_arm_frame = width
			CropManagement.hight_crop_arm_frame = height
			CropManagement.x1_crop_arm_frame = x1
			CropManagement.x2_crop_arm_frame = x1 + width
			CropManagement.y1_crop_arm_frame = y1
			CropManagement.y2_crop_arm_frame = y1 + height
			CropManagement.type_of_cropframe = "MFrameCropArm"

		if type_of_cropframe == "PeoplePassCheckAndFlashCheck" :
			CropManagement.width_crop_peoplepass_flashcheck_frame = width
			CropManagement.hight_crop_peoplepass_flashcheck_frame = height
			CropManagement.x1_crop_peoplepass_flashcheck_frame = x1
			CropManagement.x2_crop_peoplepass_flashcheck_frame = x1 + width
			CropManagement.y1_crop_peoplepass_flashcheck_frame = y1
			CropManagement.y2_crop_peoplepass_flashcheck_frame = y1 + height
			CropManagement.type_of_cropframe = "PeoplePassCheckAndFlashCheck"
		pass
	
	def _crop_form_m_frame(self,m_frame,start_x,start_y,end_x,end_y):

		m_frame_crop = m_frame[start_y:end_y,start_x: end_x]

		return m_frame_crop

	def _create_m_frame_line(self,c_frame,start_x,start_y,end_x,end_y,type_of_cropframe):
		if type_of_cropframe == "MFrameCropArm" :
			#|
			c_frame = cv2.line(img=c_frame, pt1=(start_x, start_y), pt2=(start_x, end_y), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#   |
			c_frame = cv2.line(img=c_frame, pt1=(end_x, start_y), pt2=(end_x, end_y), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#_
			c_frame = cv2.line(img=c_frame, pt1=(start_x, end_y), pt2=(end_x, end_y), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#--
			c_frame = cv2.line(img=c_frame, pt1=(start_x, start_y), pt2=(end_x, start_y), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

		if type_of_cropframe == "PeoplePassCheckAndFlashCheck" :
			#|
			c_frame = cv2.line(img=c_frame, pt1=(start_x, start_y), pt2=(start_x, end_y), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#   |
			c_frame = cv2.line(img=c_frame, pt1=(end_x, start_y), pt2=(end_x, end_y), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#_
			c_frame = cv2.line(img=c_frame, pt1=(start_x, end_y), pt2=(end_x, end_y), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#--
			c_frame = cv2.line(img=c_frame, pt1=(start_x, start_y), pt2=(end_x, start_y), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

		return c_frame

# _by_cm_obj

	def _crop_form_m_frame_by_cm_obj(self,m_frame):

		if CropManagement.type_of_cropframe == "MFrameCropArm" :
			m_frame_crop = m_frame[
				CropManagement.y1_crop_arm_frame : CropManagement.y2_crop_arm_frame,
				CropManagement.x1_crop_arm_frame : CropManagement.x2_crop_arm_frame
				]

		if CropManagement.type_of_cropframe == "PeoplePassCheckAndFlashCheck" :
			m_frame_crop = m_frame[
				CropManagement.y1_crop_peoplepass_flashcheck_frame : CropManagement.y2_crop_peoplepass_flashcheck_frame,
				CropManagement.x1_crop_peoplepass_flashcheck_frame : CropManagement.x2_crop_peoplepass_flashcheck_frame
				]
			
		return m_frame_crop

	def _create_m_frame_line_by_cm_obj(self,c_frame):
		if CropManagement.type_of_cropframe == "MFrameCropArm" :
			#|
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_arm_frame, CropManagement.y1_crop_arm_frame), pt2=(CropManagement.x1_crop_arm_frame, CropManagement.y2_crop_arm_frame), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#   |
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x2_crop_arm_frame, CropManagement.y1_crop_arm_frame), pt2=(CropManagement.x2_crop_arm_frame, CropManagement.y2_crop_arm_frame), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#_
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_arm_frame, CropManagement.y2_crop_arm_frame), pt2=(CropManagement.x2_crop_arm_frame, CropManagement.y2_crop_arm_frame), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

			#--
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_arm_frame, CropManagement.y1_crop_arm_frame), pt2=(CropManagement.x2_crop_arm_frame, CropManagement.y1_crop_arm_frame), color=(0, 255, 0), thickness=5, lineType=8, shift=0)

		if CropManagement.type_of_cropframe == "PeoplePassCheckAndFlashCheck" :
			#|
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_peoplepass_flashcheck_frame, CropManagement.y1_crop_peoplepass_flashcheck_frame), pt2=(CropManagement.x1_crop_peoplepass_flashcheck_frame, CropManagement.y2_crop_peoplepass_flashcheck_frame), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#   |
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x2_crop_peoplepass_flashcheck_frame, CropManagement.y1_crop_peoplepass_flashcheck_frame), pt2=(CropManagement.x2_crop_peoplepass_flashcheck_frame, CropManagement.y2_crop_peoplepass_flashcheck_frame), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#_
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_peoplepass_flashcheck_frame, CropManagement.y2_crop_peoplepass_flashcheck_frame), pt2=(CropManagement.x2_crop_peoplepass_flashcheck_frame, CropManagement.y2_crop_peoplepass_flashcheck_frame), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

			#--
			c_frame = cv2.line(img=c_frame, pt1=(CropManagement.x1_crop_peoplepass_flashcheck_frame, CropManagement.y1_crop_peoplepass_flashcheck_frame), pt2=(CropManagement.x2_crop_peoplepass_flashcheck_frame, CropManagement.y1_crop_peoplepass_flashcheck_frame), color=(255, 0, 0), thickness=5, lineType=8, shift=0)

		return c_frame






	

