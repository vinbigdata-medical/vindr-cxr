# Detecting chest Xray outliers

This program is used to reject outliers. Normal chest X-ray images (frontal view) will be passed to the general chest X-ray classifier.

# Usage:

```python

from .main import OutlierDetector

# Import module
module = OutlierDetector()
# Path to the input X-ray image (.dicom; .jpeg; .jpg)
file_path = "path/to/image/file"
# Predict
index = module.predict(file_path)
print(index)

"""
Note that:

index = 0: Normal / Valid Chest X-ray
index = 1: Outlier
"""


```