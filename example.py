!pip install mplsoccer
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen, VerticalPitch
import os

# importing the data parser through mplsoccer (alternative to the official statsbombpy package)
parser  = Sbopen()
