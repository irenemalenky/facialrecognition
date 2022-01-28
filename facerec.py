# create a program for facial detection
# use opencv
# use tkinter
# have user select image
# have user enter scale factor
# include a submit button
# print number of faces found

import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("face count")

# function for submit button
def pickImage():
    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)

# function for pick image
def imageFile():
     
    imagePath = file_path
    print(imagePath)

    # cascade file
    cascPath = 'haarcascade_frontalface_default.xml'

    # create the haar cascade
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # read the image
    image = cv2.imread(imagePath)
    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scale = float(scale_entry.get())

    # detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = scale,  # take user scale entry
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    print("found {0} faces!".format(len(faces)))

    # draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("faces found", image)
    cv2.waitKey(0)

# ask for user to enter scale factor in box
scale = tk.Label(root, text="please enter scale factor")
scale.grid(row=0, column=0)
# entry box
scale_entry = tk.Entry(root)
scale_entry.grid(row=0, column=1)

# ask for user to select image from browse
intro = tk.Label(root, text="please select an image")
intro.grid(row=1, column=0)

# submit button
tk.Button(root, text='pick image', width=10, command=pickImage).grid(row=3,column=1)
tk.Button(root, text='submit', width=10, command=imageFile).grid(row=4,column=1)

