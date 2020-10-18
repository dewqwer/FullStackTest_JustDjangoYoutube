from PIL import Image
import numpy as np
import cv2

class MonitorManagement:
	# location11_x1 = 0 
	# location11_x2 = 0
	# location11_y1 = 0
	# location11_y2 = 0
	# location12_x1 = 0
	# location12_x2 = 0
	# location12_y1 = 0
	# location12_y2 = 0
	# location13_x1 = 0
	# location13_x2 = 0
	# location13_y1 = 0
	# location13_y2 = 0

	# location21_x1 = 0 
	# location21_x2 = 0
	# location21_y1 = 0
	# location21_y2 = 0
	# location22_x1 = 0
	# location22_x2 = 0
	# location22_y1 = 0
	# location22_y2 = 0
	# location23_x1 = 0
	# location23_x2 = 0
	# location23_y1 = 0
	# location23_y2 = 0

	# location31_x1 = 0 
	# location31_x2 = 0
	# location31_y1 = 0
	# location31_y2 = 0
	# location32_x1 = 0
	# location32_x2 = 0
	# location33_y1 = 0
	# location32_y2 = 0
	# location33_x1 = 0
	# location33_x2 = 0
	# location33_y1 = 0
	# location33_y2 = 0
# img = Image.new('RGB', (w, h), color = 'red')

	# frame_w1500 = Image.new('RGB', (1500,281+281+281 ), color = 'red')
	frame_w500_11 = 0
	frame_w500_12 = 0
	frame_w500_13 = 0
	frame_w500_21 = 0
	frame_w500_22 = 0
	frame_w500_23 = 0
	frame_w500_31 = 0
	frame_w500_32 = 0
	frame_w500_33 = 0
	moniter_value

	def __init__(self):
		pass

	# def __init__(self,frame_w1500):
	# 	self.frame_w1500 = frame_w1500
	# 	pass

	def _sumary_moniter(self,location_of_frame,frame_w500,frame_w1500):
		# 11 cl_frame
		if location_of_frame == 11 :
			frame_w1500[0:281,0:500] = frame_w500.copy()
		# 12 m_frame
		if location_of_frame == 12 :
			frame_w1500[281:281+281,0:500] = frame_w500.copy()
		# 13 c_frame
		if location_of_frame == 13 :
			frame_w1500[281+281:281+281+281,0:500] = frame_w500.copy()
		# 21 mc_a_frame
		if location_of_frame == 21 :
			frame_w1500[0:281,500:500+500] = frame_w500.copy()
		# 22 mc_pf_frame
		if location_of_frame == 22 :
			frame_w1500[281:281+281,500:500+500] = frame_w500.copy()
		# 23
		if location_of_frame == 23 :
			frame_w1500[281+281:281+281+281,500:500+500] = 0
		# 31 mc_frame
		if location_of_frame == 31 :
			frame_w1500[0:281,500+500:500+500+500] = frame_w500.copy()
		# 32
		if location_of_frame == 32 :
			frame_w1500[281:281+281,500+500:500+500+500] = 0
		# 33
		if location_of_frame == 33 :
			frame_w1500[281+281:281+281+281,500+500:500+500+500] = 0
		return frame_w1500


	# def _mc_a_frame_moniter(self,mc_frame_crop_arm):
	# 	return

	# def _sumary_moniter_by_mm_obj(self):
	# 	MonitorManagement.frame_w1500[0:281,0:500] = MonitorManagement.frame_w500_11#11
	# 	MonitorManagement.frame_w1500[281:281+281,0:500] = cv2.cvtColor(m_frame.copy(),cv2.COLOR_BGR2RGB) #12
	# 	MonitorManagement.frame_w1500[0:281,500:500+500] = mc_a_frame.copy() #21 
	# 	MonitorManagement.frame_w1500[281:281+281,500:500+500] = mc_pf_frame.copy() #22
	# 	MonitorManagement.frame_w1500[281+281:281+281+281,500:500+500] = 0 #23
	# 	MonitorManagement.frame_w1500[281+281:281+281+281,0:500] = c_frame.copy() #13
	# 	MonitorManagement.frame_w1500[281+281:281+281+281,500+500:500+500+500] = 0 #33
	# 	MonitorManagement.frame_w1500[281:281+281,500+500:500+500+500] = 0 #32
	# 	MonitorManagement.frame_w1500[0:281,500+500:500+500+500] = mc_frame.copy() #31
	

