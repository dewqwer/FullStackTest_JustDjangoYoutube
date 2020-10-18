import numpy as np

class FilterAndCheckErrorManagement:
	m_frame_crop_mean_lpft_set = np.arange(15)
	people_pass_flash_check_status = False
	filter_low_value_status = False
	m_frame_crop_peoplepass_flashcheck_mean_current = 0
	def __init__(self):
		pass


	def _lowpassfilter_m_frame(self,m_frame_crop_mean_set,lpft_number):
		m_frame_crop_mean_lpft_current = (np.sum(m_frame_crop_mean_set))/lpft_number
		return m_frame_crop_mean_lpft_current


	def _people_pass_flash_check(self,m_frame_crop_peoplepass_flashcheck_mean_current):
		if(m_frame_crop_peoplepass_flashcheck_mean_current >= 150):
			FilterAndCheckErrorManagement.people_pass_flash_check_status = True
		else : 
			FilterAndCheckErrorManagement.people_pass_flash_check_status = False
		FilterAndCheckErrorManagement.m_frame_crop_peoplepass_flashcheck_mean_current = m_frame_crop_peoplepass_flashcheck_mean_current
		return FilterAndCheckErrorManagement.people_pass_flash_check_status

	def _filter_low_value(self,m_frame_crop_mean_lpft_current,low_value):
		FilterAndCheckErrorManagement.filter_low_value_status = False
		if m_frame_crop_mean_lpft_current <= low_value :
			m_frame_crop_mean_lpft_current = 0
			FilterAndCheckErrorManagement.filter_low_value_status = True
		return m_frame_crop_mean_lpft_current
