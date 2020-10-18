import numpy as np
import requests

class MFrameSetManagement:
  m_frame_crop_mean_set = np.arange(30)
  m_frame_crop_mean_lpft_set = np.arange(3)
  status_up_down_slope_set = np.arange(2)
  people_count = 0
  count_wave_set = 0
  status_up_count = 0
  status_down_count = 0
  status_count_lock = True
  status_up_down_slope_current = 0
  count_in_peak_wave = False
  error_count = 0
  

  def _initial_frame_crop_mean_set(self,lpft_value):
    MFrameSetManagement.m_frame_crop_mean_set = np.arange(lpft_value)
    MFrameSetManagement.m_frame_crop_mean_set = np.zeros_like(MFrameSetManagement.m_frame_crop_mean_set)
    return MFrameSetManagement.m_frame_crop_mean_set

  def _initial_frame_crop_mean_lpft_set(self,size_array):
    MFrameSetManagement.m_frame_crop_mean_lpft_set = np.arange(size_array)
    MFrameSetManagement.m_frame_crop_mean_lpft_set = np.zeros_like(MFrameSetManagement.m_frame_crop_mean_lpft_set)
    return MFrameSetManagement.m_frame_crop_mean_lpft_set

  def __init__(self):
    pass

  def _update_m_frame_crop_mean_set(self,m_frame_crop_mean_current):
    # x[:-1] = x[1:]; x[-1] = newvalue
    MFrameSetManagement.m_frame_crop_mean_set[:-1] = MFrameSetManagement.m_frame_crop_mean_set[1:]; MFrameSetManagement.m_frame_crop_mean_set[-1] = m_frame_crop_mean_current
    return MFrameSetManagement.m_frame_crop_mean_set #m_frame_crop_mean_current stay on last index in this array

  def _update_m_frame_crop_mean_lpft_set(self,m_frame_crop_mean_lpft_current):
    # x[:-1] = x[1:]; x[-1] = newvalue
    MFrameSetManagement.m_frame_crop_mean_lpft_set[:-1] = MFrameSetManagement.m_frame_crop_mean_lpft_set[1:]; MFrameSetManagement.m_frame_crop_mean_lpft_set[-1] = m_frame_crop_mean_lpft_current
    return MFrameSetManagement.m_frame_crop_mean_lpft_set #m_frame_crop_mean_lpft_current stay on last index in this array


  def _check_status_up_down_slope(self):
    status_up_down_slope_current = 0
    if MFrameSetManagement.m_frame_crop_mean_lpft_set[0] < MFrameSetManagement.m_frame_crop_mean_lpft_set[2]  :
      status_up_down_slope_current = 1 #up
    if MFrameSetManagement.m_frame_crop_mean_lpft_set[0] > MFrameSetManagement.m_frame_crop_mean_lpft_set[2]  :
      status_up_down_slope_current = -1 #down
    if status_up_down_slope_current == 1 :
      MFrameSetManagement.status_up_count = MFrameSetManagement.status_up_count + 1
    if MFrameSetManagement.status_up_count >= 2 and MFrameSetManagement.status_up_count <= 15 :
      MFrameSetManagement.status_count_lock = False
    else:
      MFrameSetManagement.status_count_lock = True
      pass
    
    MFrameSetManagement.status_up_down_slope_current = status_up_down_slope_current

    return status_up_down_slope_current

  def _update_status_up_down_slope(self,status_up_down_slope_current):
    # x[:-1] = x[1:]; x[-1] = newvalue

    if status_up_down_slope_current == 0 :
      status_up_down_slope_current = MFrameSetManagement.status_up_down_slope_set[0]
      MFrameSetManagement.status_up_down_slope_set[:-1] = MFrameSetManagement.status_up_down_slope_set[1:]; MFrameSetManagement.status_up_down_slope_set[-1] = status_up_down_slope_current
    else:
      MFrameSetManagement.status_up_down_slope_set[:-1] = MFrameSetManagement.status_up_down_slope_set[1:]; MFrameSetManagement.status_up_down_slope_set[-1] = status_up_down_slope_current
      pass
    
    
    return MFrameSetManagement.status_up_down_slope_set

  def _initial_status_up_down_slope_set(self,size_array):
    MFrameSetManagement.status_up_down_slope_set = np.arange(size_array)
    MFrameSetManagement.status_up_down_slope_set = np.zeros_like(MFrameSetManagement.status_up_down_slope_set)
    return MFrameSetManagement.status_up_down_slope_set

  def _counter(self):
    if (MFrameSetManagement.status_up_down_slope_set[0] == 0 and MFrameSetManagement.status_up_down_slope_set[1] == 1) or (MFrameSetManagement.status_up_down_slope_set[0] == -1 and MFrameSetManagement.status_up_down_slope_set[1] == 1) :
      MFrameSetManagement.count_wave_set = MFrameSetManagement.count_wave_set + 1
      MFrameSetManagement.status_up_count = 0
      MFrameSetManagement.count_wave_set = 0
      MFrameSetManagement.count_in_peak_wave = False #40

    if (MFrameSetManagement.status_up_down_slope_set[0] == 1 and MFrameSetManagement.status_up_down_slope_set[1] == -1) and MFrameSetManagement.status_up_count <=15 and MFrameSetManagement.status_up_count >= 2 :
      MFrameSetManagement.count_wave_set = MFrameSetManagement.count_wave_set + 1
      MFrameSetManagement.people_count = MFrameSetManagement.people_count + 1
      MFrameSetManagement.count_in_peak_wave = True

      self._send_request_to_django()
    else:
      MFrameSetManagement.count_wave_set = MFrameSetManagement.count_wave_set + 1
      pass


    if MFrameSetManagement.count_wave_set >= 40 and MFrameSetManagement.count_in_peak_wave == True :
      MFrameSetManagement.people_count = MFrameSetManagement.people_count - 1  
      MFrameSetManagement.count_in_peak_wave = False
      print("Dectect Error Big Wave")
      MFrameSetManagement.error_count = MFrameSetManagement.error_count + 1

    print("MFrameSetManagement.count_wave_set : "+ str(MFrameSetManagement.count_wave_set))
    return MFrameSetManagement.people_count
     
  def _send_request_to_django(self):
    # # api-endpoint
    # URL = "http://localhost:8000"

    # # location given here
    # people_count = MFrameSetManagement.people_count

    # # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'people_count': people_count}

    # # sending get request and saving the response as response object
    # r = requests.get(url=URL, params=PARAMS)

    pass
