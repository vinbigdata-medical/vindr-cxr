import pydicom
import magic
import cv2

from PIL import Image
from torchvision import transforms
from torch.autograd import Variable


# data transform
infer_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(20),
    transforms.Resize(size=(224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])


def getUUID():
    return uuid.uuid4().urn[9:]

# load X-ray image
def load_xrayImg(file_path):
    """ 
    Return the numpy array image from given file_path
    
    file_path: path to the image/dicom file
    """
    file_type, file_extension = magic.from_file(file_path, mime=True).split('/')
     
    if file_type == "image":
        image = load_image(file_path)
    elif file_extension == "dicom":
        image = load_dcm_image(file_path)
    else:
        raise ValueError('A very specific bad thing happened with given files! Cannot read it.')

    return image


def load_image(image_path):
    
    image = Image.open(image_path).convert('L')
    image = image.convert('RGB')
    image_tensor = infer_transform(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    image_tensor = Variable(image_tensor)

    return image_tensor
    
def load_dcm_image(dicom_file):
    
    # Read dicom file.  
    dcm_file = pydicom.dcmread(dicom_file)

    # Bits Stored' value should match the sample bit depth of the JPEG2000 pixel (16 bit) data in order to get the correct pixel data.
    
    if dcm_file.BitsStored in (10,12):
        dcm_file.BitsStored = 16
    
    raw_image = dcm_file.pixel_array
    
    # Normalize pixels to be in [0, 255].
    rescaled_image = cv2.convertScaleAbs(dcm_file.pixel_array,
                                        alpha=(255.0/dcm_file.pixel_array.max()))
    
    # Correct image inversion.
    if dcm_file.PhotometricInterpretation == "MONOCHROME1":
        rescaled_image = cv2.bitwise_not(rescaled_image)

    # Perform histogram equalization if the input is original dicom file.
    if dcm_file.pixel_array.max() > 255:
        adjusted_image = cv2.equalizeHist(rescaled_image)
    else:
        adjusted_image = rescaled_image

    image = Image.fromarray(adjusted_image)
    image = image.convert('RGB') 
    image_tensor = infer_transform(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    image_tensor = Variable(image_tensor)
       
    return image_tensor