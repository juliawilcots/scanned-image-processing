import sys
import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # makes plots appear in new window
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont



def rectangular_crop(image):
    '''
    User clicks upper left and bottom right corner
    Coordinates: (x,y); origin is top left corner
    
    Crop photo to that rectangle
    Returns cropped photo
    '''
    print('Click upper left and lower right corners of cropped area')

    #plt.imshow(image)
    corners = plt.ginput(2)
    #plt.close()
    
    [x0,y0],[x1,y1] = corners
    area = (x0,y0,x1,y1)
    
    cropped_image = image.crop(area)
    
    return cropped_image

def calc_scale(image):
    '''
    Takes image, and scale length as input
    User clicks 2 points on image = to length (input value)
    '''
    print('Click left and right points of scale (straight line)')
    
    #plt.imshow(image)
    [x0,y0],[x1,y1] = plt.ginput(2)
    #plt.close()
    
    # Calculate distance (in pixels) between points
    scale_len = np.sqrt((np.abs(x1-x0))**2 + (np.abs(y1-y0))**2)
    
    return scale_len

def add_scalebar(image,scale,color,length,length_units,**kwargs):
    '''
    image
    scale = pixels
    length = real world length
    
    **kwargs options:
    font_size (int) : specify font size on scale bar (very dependent on actual image size). default = 40
    buffer (int) : distance (in points) between scale bar label and scale bar itself. default = 15
    
    assumes you want horizontal line (change later?)
    '''
    
    print('Click where you\'d like your scale bar to appear')
    
    scale_bar_font_size = 40
    scale_label_buffer = 15
    
    for key, value in kwargs.items():
        if key == 'font_size':
            scale_bar_font_size = value
        if key == 'buffer':
            scale_label_buffer = value
        
    plt.imshow(image)
    
    # Click location of scale bar on photo
    point = plt.ginput(1)
    x0 = point[0][0]; y0 = point[0][1]
    
    # Draw scalebar on photo
    draw = ImageDraw.Draw(image)
    draw.line((x0,y0) + (x0+scale,y0), fill='white', width=8)
    
    # Optional: specify line weight in **kwargs
    
    # Add text to scalebar
    text = '%s %s' %(length,length_units)
    font_path = "/Library/Fonts/MyriadPro-Regular.otf" # path to where your computer stores fonts.
    font = ImageFont.truetype(font_path, scale_bar_font_size)
    draw.text((x0,y0+scale_label_buffer), text, font=font)
    
    del draw
    plt.close()
    
    return image
    


if __name__ == "__main__":
    
    # The directory your photos are in:
    directory = sys.argv[1]
    print(directory)
    
    # Length of your scale bar:
    scale_bar_length = 1.0
    scale_bar_units = 'cm'
    
    # Aesthetics of the scale bar
    scale_bar_color = 'white'
    
    
    
    for file in os.listdir(directory): # loop through files in folder
        
        filename = file.lower() # convert to lowercase for string matching
        
        if filename.endswith('jpg') or filename.endswith('tif'): # only include images
            
            file_name = filename.split('.')[0]
            print(file_name)
            file_ext = filename.split('.')[1]
            
            scan = os.path.join(directory, filename) # make path to photo
            image = Image.open(scan) # open image
            #im_np = np.asarray(im)
            #plt.imshow(im_np)
            #plt.draw()
            #plt.pause(3) # show for 3 seconds
            #plt.close()
            
            # Show image:
            plt.imshow(image)
            
            # 1. Initial crop -- make sure to include scale and all of rock area you ultimately want!
            crop1 = rectangular_crop(image)
            plt.close()
            
            plt.imshow(crop1)
            # 2. Click ends of scale! (e.g. edges of coin or 1,2cm on ruler)
            scale = calc_scale(crop1)
            
            # 3. Final crop -- only keep area you want to save!
            crop2 = rectangular_crop(crop1)

            # 4. Add scale bar to final image (writing will be on the bottom!)
            #########
            # IF YOU WANT TO CHANGE ANYTHING ABOUT THE APPEARANCE OF THE TEXT, DO THAT HERE:
            #########
            add_scalebar(crop2,
                         scale = scale, 
                         color = scale_bar_color,
                         length = scale_bar_length,
                         length_units = scale_bar_units)

            
            # 5. Save new image in new folder (don't delete original)
            output_file = '%s-cropped.%s' %(file_name,file_ext)
            crop2.save('%scropped-photos/%s' %(directory,output_file))