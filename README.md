# scanned-image-processing
Python scripts for processing scanned rocks

The idea:
- User clicks photo of rock to crop and add scale bar

To run:
```python testing.py 'path/to/directory/of/photos'```

As an example: running   
```python testing.py 'test-folder'```   
will allow you to crop and add scales to three photos of Neoproterozoic rocks in South Australia.  

First, the photo will appear in a pop-up window,  
Then, click the top left and lower right corners of the area you would like to keep,  
(The photo is then cropped and will reappear)  
Click the left and right extents of the scale bar you would like to add  
Then, crop again (click top left and lower right corners),  
Finally, click the spot where you want the left extent of the scale bar to appear.  

The final photo will be saved in an output folder.  


I do not yet have a clean way of changing the:
- output directory,
- scale bar length,
- scale bar text (font size, font, what font says)

(These are all hard-coded right now -- eventually I will have a .yaml)
