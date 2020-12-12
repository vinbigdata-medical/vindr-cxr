import pydicom
import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import cv2
from PIL import Image

def get_image(dicom_path):
    dcm = pydicom.read_file(dicom_path)
    raw_pixel = dcm.pixel_array
    img = cv2.convertScaleAbs(raw_pixel, alpha=(255.0/dcm.pixel_array.max()))
    if len(raw_pixel.shape) == 2:
        if dcm.PhotometricInterpretation == "MONOCHROME1":
            img = cv2.bitwise_not(img)   
        img = cv2.equalizeHist(img)
        img = Image.fromarray(img)
        img = img.convert('RGB')
        img = np.array(img)
    return img

if __name__ == "__main__":
    os.makedirs('images', exist_ok = True)
    encoded_id_df = pd.read_csv('encoded_id.csv')

    for mset in ['test', 'train']:
        os.makedirs('images/' + mset, exist_ok = True)
        
        for rdir,_,files in os.walk('dataset/' + mset):
            for file in tqdm(files):
                dicom_path = os.path.join(rdir, file)
                
                SOPInstanceUID = file.replace('.dicom', '')
                tmp_df = encoded_id_df.loc[encoded_id_df['SOPInstanceUID'] == SOPInstanceUID]
                encoded_id = tmp_df.encode_id.values[0]

                new_dicom_path = dicom_path.replace('dataset/', 'dataset_masked/').replace(file, encoded_id+'.dicom')
                new_image_path = 'images/{}/{}.png'.format(mset, encoded_id)
                
                img = get_image(dicom_path)
                anonymized_img = get_image(new_dicom_path)
                if (img==anonymized_img).all() == False:
                    print(file, encoded_id)
                
                cv2.imwrite(new_image_path, anonymized_img)
