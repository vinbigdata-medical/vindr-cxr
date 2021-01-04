# VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations


The VinDr-CXR is a large publicly available dataset of chest radiographs with radiologits' annotations for classification of common thoracic lung diseases and localization of critical findings. It was created by Vingroup Big Data Institute (VinBigdata). The dataset contains more than 18,000 CXR scans collected from two major hospitals in Vietnam from 2018 to 2020. The images were labeled for presence of 28 different radiographic findings and diagnoses. Each scan from the training set was annotated by a group of three radiologists. For the test set, five experienced radiologists participated in the labeling process and their consensus was used to establish the best reference standard for the test labels. 

To download the dataset, users are required to register and accept a data use agreement (DUA) described on our webpage at https://vindr.ai/datasets/cxr. By accepting the DUA, users agree that they will not share the data and that the dataset can be used for scientific research and educational purposes only.


# Code

This repository is intended to support use of the VinDr-CXR data. We provide codes for de-identifying a patient's Personal Health Information (PHI) from a DICOM header (de-identification directory). Additionlly, we also provide Python scripts for detecting outlier hest X-ray scans (outlier-detection directory).


# Citation

If you use the VinDr-CXR dataset in your work, the authors must cite [the original paper](https://arxiv.org/abs/2012.15029) as follows:

```
@misc{nguyen2020vindrcxr,
      title={VinDr-CXR: An open dataset of chest X-rays with radiologist's annotations}, 
      author={Ha Q. Nguyen and Khanh Lam and Linh T. Le and Hieu H. Pham and Dat Q. Tran and Dung B. Nguyen and Dung D. Le and Chi M. Pham and Hang T. T. Tong and Diep H. Dinh and Cuong D. Do and Luu T. Doan and Cuong N. Nguyen and Binh T. Nguyen and Que V. Nguyen and Au D. Hoang and Hien N. Phan and Anh T. Nguyen and Phuong H. Ho and Dat T. Ngo and Nghia T. Nguyen and Nhan T. Nguyen and Minh Dao and Van Vu},
      year={2020},
      eprint={2012.15029},
      archivePrefix={arXiv},
      primaryClass={eess.IV}
}
```

We also encourage such authors to release their code and models, which will help the community to reproduce experiments and to boost the research in the field of medical imaging.




