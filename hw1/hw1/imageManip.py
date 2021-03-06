import math
import skimage #import skimage package 

import numpy as np
from PIL import Image
from skimage import color, io


def load(image_path):
    """Loads an image from a file path.

    HINT: Look up `skimage.io.imread()` function.

    Args:
        image_path: file path to the image.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = None
    
    ### YOUR CODE HERE
    
    out = skimage.io.imread(image_path) # Use skimage io.imread
    
    ### END YOUR CODE

    # Let's convert the image to be between the correct range.
    out = out.astype(np.float64) / 255
    return out


def dim_image(image):
    """Change the value of every pixel by following

                        x_n = 0.5*x_p^2

    where x_n is the new value and x_p is the original value.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None

    ### YOUR CODE HERE
    
    out=0.5*image**2 #pixels value chnged consequently
    
    ### END YOUR CODE

    return out


def convert_to_grey_scale(image):
    """Change image to gray scale.

    HINT: Look at `skimage.color` library to see if there is a function
    there you can use.

    Args:
        image: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width).
    """
    out = None

    ### YOUR CODE HERE
    
    
    out=skimage.color.rgb2gray(image) #skimage library for color change implemented
    
    ### END YOUR CODE

    return out


def rgb_exclusion(image, channel):
    """Return image **excluding** the rgb channel specified

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "R", "G" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None

    ### YOUR CODE HERE
    out=image.copy()
    
    rgb_channel={'R':0,'G':1,'B':2} 
 
    out[:,:,rgb_channel.get(channel)]=0*image[:,:,rgb_channel.get(channel)] #respective channels will be excluded i.e. 0
        
    ### END YOUR CODE

    return out


def lab_decomposition(image, channel):
    """Decomposes the image into LAB and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "L", "A" or "B".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    #lab = color.rgb2lab(image)
    out = None

    ### YOUR CODE HERE
    
    #lab=image.copy()
    lab=skimage.color.rgb2lab(lab)
    out = np.zeros(lab.shape) #create array of zeros of lab size
    #out=[]
    lab_channel={'L':0,'A':1,'B':2}
    out[:,:,lab_channel.get(channel)]=lab[:,:,lab_channel.get(channel)] 
   
    ### END YOUR CODE

    return out 


def hsv_decomposition(image, channel='H'):
    """Decomposes the image into HSV and only returns the channel specified.

    Args:
        image: numpy array of shape(image_height, image_width, 3).
        channel: str specifying the channel. Can be either "H", "S" or "V".

    Returns:
        out: numpy array of shape(image_height, image_width).
    """

    #hsv = color.rgb2hsv(image)
    out = None

    ### YOUR CODE HERE
    
    
    hsv = color.rgb2hsv(image) #library implemented for hsv decomposition
    out = np.zeros(hsv.shape) #create array of zeros of hsv size
    #out=[]
    hsv_channel={'H':0,'S':1,'V':2}
    out[:,:,hsv_channel.get(channel)]=hsv[:,:,hsv_channel.get(channel)] #will provide respective hsv channels
    ### END YOUR CODE

    return out


def mix_images(image1, image2, channel1, channel2):
    """Combines image1 and image2 by taking the left half of image1
    and the right half of image2. The final combination also excludes
    channel1 from image1 and channel2 from image2 for each image.

    HINTS: Use `rgb_exclusion()` you implemented earlier as a helper
    function. Also look up `np.concatenate()` to help you combine images.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).
        image2: numpy array of shape(image_height, image_width, 3).
        channel1: str specifying channel used for image1.
        channel2: str specifying channel used for image2.

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """

    out = None
    ### YOUR CODE HERE
    #left=image1.copy()
    #right=image2.copy()
    out=[]
    #below we call exclusion method to exclude respective channels
    left=rgb_exclusion(image1, channel1)
    right=rgb_exclusion(image2, channel2)

    out=np.concatenate((left[:,0:150,:],right[:,150:,:]), axis=1) #np.concatenate library to concatenate both 'halved' images
    
    
    
    ### END YOUR CODE

    return out


def mix_quadrants(image):
    """THIS IS AN EXTRA CREDIT FUNCTION.

    This function takes an image, and performs a different operation
    to each of the 4 quadrants of the image. Then it combines the 4
    quadrants back together.

    Here are the 4 operations you should perform on the 4 quadrants:
        Top left quadrant: Remove the 'R' channel using `rgb_exclusion()`.
        Top right quadrant: Dim the quadrant using `dim_image()`.
        Bottom left quadrant: Brighthen the quadrant using the function:
            x_n = x_p^0.5
        Bottom right quadrant: Remove the 'R' channel using `rgb_exclusion()`.

    Args:
        image1: numpy array of shape(image_height, image_width, 3).

    Returns:
        out: numpy array of shape(image_height, image_width, 3).
    """
    out = None

    ### YOUR CODE HERE
    
    pass
    ### END YOUR CODE

    return out
