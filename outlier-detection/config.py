import os


# Checkpoints
parent_folder = '/' + os.path.join(*(__file__.split('/')[:-1]),)
WEIGHT = os.path.join(parent_folder, 'checkpoints/chest_xray_outliers_detector.pth')
