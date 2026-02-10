# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:07:13 2026

@author: DELL
"""

import numpy as np
data = np.arange(24)
data_3d = data.reshape(4, 3, 2)
final_data = data_3d.transpose(0, 2, 1)
print("Final shape:", final_data.shape)
print("Final array:")
print(final_data)
