####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_visualization
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from PIL import Image

####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog,ttk
import numpy as np
import warnings
warnings.filterwarnings("ignore")

filename =''
img = None
bboximg = None
segimg = None
# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked, dataset, segmentor):
    global filename
    global img
    global bboximg   #stores the image with bounding boxes
    global segimg   #stores the image with segmentation masks
    fname = filedialog.askopenfilename(initialdir=r'data/imgs', title='select file', filetypes=[('jpg files', '*.jpg')])

    


    if fname == '':
        return

    filename = fname
    if e.get()!='': e.delete(0,5)
    st = filename[-5:]
    e.insert(0,st)
    x = int(st[0])

    print('********',fname,filename,x)


    print(dataset.getitem(x),"\n\n\n")

    img = ImageTk.PhotoImage(Image.open(filename))
    image = Image.open(filename)
    ar = np.array(image) / 255
    ar = ar.transpose(2, 0, 1)
    prediction_list = segmentor (ar)
    plot_visualization(prediction_list, ar.transpose(1, 2, 0).copy()
                       , r'Outputs/segmentation.jpg', 'segmentation')

    plot_visualization(prediction_list, ar.transpose(1, 2, 0).copy()
                       , r'Outputs/bbox.jpg', 'bounding_box')
    bbox_dir = r'Outputs/bbox.jpg'
    seg_dir = r'Outputs/segmentation.jpg'

    segimg = ImageTk.PhotoImage(Image.open(seg_dir))
    bboximg = ImageTk.PhotoImage(Image.open(bbox_dir))

    img_label = Label(image=img)   # label to display the original image
    img_label.grid(row=1, column=0,columnspan=2)
    tx = Label(root, text='Original Image', font=(
        'Calibri', 11, 'bold'), height=1, width=50, background="green", foreground="white")
    tx.grid(row=2, column=0,columnspan=2, pady=5)
    process(clicked)
    return


####### CODE REQUIRED (START) #######
# This function should pop-up a dialog for the user to select an input image file.
# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
# To have a better clarity, please check out the sample video.

####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):
    global filename
    if filename == '':
        print('<!> No file was choosen')
        return
    if clicked.get()=='Segmentation':
        primg_label = Label(image = segimg)   # label to display the image with segmentation mask
        primg_label.grid(row=1 ,column=3,columnspan=3, padx = (0,45))
        tx = Label(root, text='Image with Segmentation masks', font=(
            'Calibri', 11, 'bold'), height=1, width=50, background="green", foreground="white")
        tx.grid(row=2, column=3,columnspan=3, pady=5,padx=(0,41))
    else:
        primg_label = Label(image = bboximg) # label to display the image with bounding boxes
        primg_label.grid(row=1 ,column=3,columnspan=3,padx = (0,45))
        tx = Label(root, text='Image with Bounding Boxes', font=(
            'Calibri', 11, 'bold'), height=1, width=50, background="green", foreground="white")
        tx.grid(row=2, column=3,columnspan=3, pady=5)


####### CODE REQUIRED (START) #######
# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.

####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':
    ####### CODE REQUIRED (START) ####### (2 lines)
    root = Tk()
    root.title("Image Viewer GUI")
    # Instantiate the root window.
    # Provide a title to the root window.

    ####### CODE REQUIRED (END) #######

    # Setting up the segmentor model.
    annotation_file = './data/annotations.jsonl'
    transforms = []

    # Instantiate the segmentor model.
    segmentor = InstanceSegmentationModel()
    # Instantiate the dataset.
    dataset = Dataset(annotation_file, transforms=transforms)
    print("Number of data points= ",len(dataset))

    # Declare the options.
    options = ["Segmentation", "Bounding-box"]
    clicked = StringVar()
    clicked.set(options[0])

    e = Entry(root, width=50)
    e.grid(row=0, column=0,ipady = 3,padx=(30,5))

    ####### CODE REQUIRED (START) #######
    # Declare the file browsing button
    button = Button(root ,text='Choose File' ,borderwidth=2,bg= '#bcc0c4',command =lambda :fileClick(clicked,dataset,segmentor))
    button.grid(row=0 ,column=1,padx = 4, pady = 3,ipadx=2,ipady=2)
    ####### CODE REQUIRED (END) #######

    ####### CODE REQUIRED (START) #######
    # Declare the drop-down button
    drop = OptionMenu(root, clicked, *options)
    drop.config(bg= '#bcc0c4')
    drop.grid(row=0, column=2,pady = 3,padx=(0,4),ipadx=2,ipady=2,sticky=W)

 



    ####### CODE REQUIRED (END) #######

    # This is a `Process` button, check out the sample video to know about its functionality
    myButton = Button(root, text="Process",borderwidth=2,bg= '#bcc0c4', pady = 3, command=lambda: process(clicked))
    myButton.grid(row=0, column=3,ipadx=2,ipady=0.5,padx=(1,15),sticky=W)

####### CODE REQUIRED (START) ####### (1 line)
    root.mainloop()
# Execute with mainloop()

####### CODE REQUIRED (END) #######