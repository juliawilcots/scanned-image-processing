# scanned-image-processing
Python scripts for processing scanned rocks

The idea:
- User clicks photo of rock to crop and add scale bar

To run:
```python rock-crop.py 'path/to/directory/of/photos'```

Requirements:  
- Python packages:
    - sys, os, matplotlib, numpy, Python Image Library (PIL)
- Other:
    - All photos you want to process should be in one directory. 
    - All final (cropped and scaled) photos will be save in a sub-directory called 'cropped-photos'. I think you should make this directory ahead of time, but you *might* not have to.
    - Fonts in PIL are handled strangely and won't be scalable by default. There's a good chance what I have hard-coded is Mac-specific (or possibly even specific to my machine). If you need to change the path, edit this line:  
    ``` font_path = "/Library/Fonts/MyriadPro-Regular.otf"```  
    in the method ```add_scalebar``` in ```rock-crop.py```.
    

Example:
```python rock-crop.py 'test-folder'```   
will allow you to crop and add scales to three photos of Neoproterozoic rocks in South Australia.  

Sequence of events:  
***Note: you never click more than two (2) points on each pop-up window***
1. The active photo will appear in a pop-up window
2. You click the **top left** and **bottom right** corners of the area in the photo you would like to *keep* (make sure your scale bar is in this cropped area!!)
3. The photo is then cropped and will reappear (cropped). 
4. You click the **left** and **right** extents of the scale bar (e.g. click on "5" and "6" cm  markings on a ruler to  add a 1 cm scale bar.
5. Then, click the **top left** and **lower right** corners again to make your final crop!
6. Finally, click the spot where you want the **left extent** of the scale bar to appear. The writing will go *under* the scale bar.  

The final photo will be saved in an output folder called ```cropped-photos``` in the same directory as the input photos.  
