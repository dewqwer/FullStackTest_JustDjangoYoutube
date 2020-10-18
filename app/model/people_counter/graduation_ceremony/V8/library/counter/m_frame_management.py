import numpy as np

class MFrameManagement:
  m_frame_crop_mean = 0
  def _find_avg_value_of_m_frame(self,m_frame_crop):
    m_frame_crop_mean = m_frame_crop.flatten().mean()
    MFrameManagement.m_frame_crop_mean = m_frame_crop_mean
    return m_frame_crop_mean

  def __init__(self):
    pass
