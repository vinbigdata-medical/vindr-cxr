# VinDr-CXR Dataset



The VinDr-CXR is a large publicly available dataset of chest radiographs with radiologits' annotations for classification of common thoracic lung diseases and localization of critical findings. It was created by Vingroup Big Data Institute (VinBigdata). The dataset contains more than 18,000 CXR scans collected from two major hospitals in Vietnam from 2018 to 2020. The images were labeled for presence of 28 different radiographic findings and diagnoses. Each scan from the training set was annotated by a group of three radiologists. For the test set, five experienced radiologists participated in the labeling process and their consensus was used to establish the best reference standard for the test labels. 


To download the dataset, users are required to register and accept a data use agreement (DUA) described on our webpage at https://vindr.ai/datasets/cxr. By accepting the DUA, users agree that they will not share the data and that the dataset can be used for scientific research and educational purposes only.

# Code

This repository is intended to support use of the VinDr-CXR data. We provide codes for de-identifying a patient's Personal Health Information (PHI) from a DICOM header (de-identification directory). Additionlly, we also provide Python scripts for detecting outlier hest X-ray scans (outlier-detection directory).

# Citation

If you use the VinDr-CXR dataset in your work, the authors must cite this original paper as follows:

Ha Q. Nguyen et al. “VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations” – A preprint available at https://arxiv.org

We also encourage such authors to release their code and models, which will help the community to reproduce experiments and to boost the research in the field of medical imaging.


