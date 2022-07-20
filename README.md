
# Python GUI Assignment with Tkinter

## Introduction
In this project, I developed a software which helps in detecting objects from an image. The software consists of a Machine Learning model which reads the image as NumPy array and returns information regarding the detected objects. These informations were translated by me to relevant bounding boxes, segmentation masks, names and displayed as output. The model was already given to me and I implemented the entire Graphical User Interface for the software using the Tkinter library of Python. I also used the PIL library of Python to manipulate the images and display the output image in a more user-friendly fashion.

 

## Demo Video
https://youtu.be/zDNLTnqvjKo



## Implementation Details
- For this project, our professor gave us a Machine Learning model, and our task was to use this  
  model and create an application that performs many exciting tasks using this model.
- During the first half of the project, I created a python package containing many image  
  manipulatory modules.
- One of the modules named 'plot_visualiztion' is the main focus of this project. This module works 
  in unison with the ML model to perform all the functionalities of our application.
- The GUI for this project was created using the Tkinter library of python. 
- The GUI allows users to choose files easily from dialouge boxes and enjoy the functionalities of 
  this application just by pressing relevant buttons.
- On choosing an image file, the application uses the ML model to generate a list of predictions. 
  This prediction list is then sent to the 'plot_visualization' module for further processing.
- The 'plot_visualization' module uses the prediction list to draw segmentation masks, bounding 
  boxes, and labels for the detected objects in the image and create a new modified image containing these details.
- The modified image is then saved at a specific location known to the application. 
- After that, the application opens the modified image from that location and displays it on the 
  Graphical User Interface. 




