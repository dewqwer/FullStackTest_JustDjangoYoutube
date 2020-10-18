# import numpy as np

# class CounterManagement:
#   status_up_down_slope_set = np.arange(2)
#   count_wave_set = 0
  

#   def _initial_frame_crop_mean_set(self,lpft_value):
#     CounterManagement.m_frame_crop_mean_set = np.arange(lpft_value)
#     CounterManagement.m_frame_crop_mean_set = np.zeros_like(CounterManagement.m_frame_crop_mean_set)
#     return CounterManagement.m_frame_crop_mean_set


#   def __init__(self):
#     pass

#   def _update_m_frame_crop_mean_set(self,m_frame_crop_mean_current):
#     # x[:-1] = x[1:]; x[-1] = newvalue
#     CounterManagement.m_frame_crop_mean_set[:-1] = CounterManagement.m_frame_crop_mean_set[1:]; CounterManagement.m_frame_crop_mean_set[-1] = m_frame_crop_mean_current
#     return CounterManagement.m_frame_crop_mean_set #m_frame_crop_mean_current stay on last index in this array

#   def _update_m_frame_crop_mean_lpft_set(self,m_frame_crop_mean_lpft_current):
#     # x[:-1] = x[1:]; x[-1] = newvalue
#     CounterManagement.m_frame_crop_mean_lpft_set[:-1] = CounterManagement.m_frame_crop_mean_lpft_set[1:]; CounterManagement.m_frame_crop_mean_lpft_set[-1] = m_frame_crop_mean_lpft_current
#     return CounterManagement.m_frame_crop_mean_lpft_set #m_frame_crop_mean_lpft_current stay on last index in this array


#   def _check_status_up_down_slope(self):
#     status_up_down_slope_current = 0
#     if CounterManagement.m_frame_crop_mean_lpft_set[0] < CounterManagement.m_frame_crop_mean_lpft_set[1] and CounterManagement.m_frame_crop_mean_lpft_set[1] < CounterManagement.m_frame_crop_mean_lpft_set[2] :
#       status_up_down_slope_current = 1 #up
#     if CounterManagement.m_frame_crop_mean_lpft_set[0] > CounterManagement.m_frame_crop_mean_lpft_set[1] and CounterManagement.m_frame_crop_mean_lpft_set[1] > CounterManagement.m_frame_crop_mean_lpft_set[2] :
#       status_up_down_slope_current = -1 #down
    
#     return status_up_down_slope_current






