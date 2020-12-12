import argparse
import os
import pydicom
import numpy as np
from tqdm import tqdm
import pandas as pd 
import hashlib

if __name__ == "__main__":
    os.makedirs('dataset_masked', exist_ok = True)

    tag_df = pd.read_csv('tags.csv')
    SOPInstanceUIDs = []
    StudyInstanceUIDs = []
    encoded_ids = []

    for mset in ['test', 'train']:
        os.makedirs('dataset_masked/' + mset, exist_ok = True)
        
        for rdir,_,files in os.walk('dataset/' + mset):
            for file in files:
                dicom_path = os.path.join(rdir, file)
                print(dicom_path)
                dcm = pydicom.read_file(dicom_path)

                dcm.file_meta.ImplementationClassUID = "1.2.3.4"

                MediaStorageSOPInstanceUID = dcm.file_meta.MediaStorageSOPInstanceUID
                hash_object = hashlib.md5(MediaStorageSOPInstanceUID.encode())
                encoded = str(hash_object.hexdigest())
                dcm.file_meta.MediaStorageSOPInstanceUID = encoded

                SOPInstanceUIDs.append(dcm.SOPInstanceUID)
                StudyInstanceUIDs.append(dcm.StudyInstanceUID)
                encoded_ids.append(encoded)

                dcm_keys = list(dcm.keys())
                for k in dcm_keys:
                    if k not in tag_df.keyword.values:
                        dcm.pop(k, None)

                print(dcm)
                new_dicom_path = dicom_path.replace('dataset/', 'dataset_masked/').replace(file, encoded+'.dicom')
                dcm.save_as(new_dicom_path)

    image_uid_encode_df = pd.DataFrame()
    image_uid_encode_df['encode_id'] = np.array(encoded_ids)
    image_uid_encode_df['SOPInstanceUID'] = np.array(SOPInstanceUIDs)
    image_uid_encode_df['StudyInstanceUID'] = np.array(StudyInstanceUIDs)
    image_uid_encode_df.to_csv('encoded_id.csv', index=False)
