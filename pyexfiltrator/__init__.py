# __version__ = '0.1.0'

import sys
from typing import Dict

# setting global vars inside modules seem to be problematic in Python:
# https://stackoverflow.com/questions/1977362/how-to-create-module-wide-variables-in-python
exfiltrated: Dict = dict()

def exfiltrate(n_frames_back=1):
    global exfiltrated

    previous_frame = sys._getframe(n_frames_back)
    previous_frame_locals = previous_frame.f_locals

    exfiltrated.update(previous_frame_locals) # does not set te global var, so it works fine

    return previous_frame_locals
