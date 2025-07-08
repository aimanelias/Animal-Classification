from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text, Label
import os 
import tkinter.font as tkFont
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot as plt
import numpy as np
import os
import PIL

# from tensorflow import keras
# from tensorflow.keras import layers
# from tensorflow.keras.models import Sequential

import tempfile
from matplotlib import pyplot as plt

root = tk.Tk()
apps =[]

model = tf.keras.models.load_model('saved_model/my_model')
batch_size = 32
img_height = 300
img_width = 300
class_names = ['bear', 'cat', 'dog', 'elephant', 'giraffe', 'horse', 'panda']


if os.path.isfile('save.text'):
    with open('save.text','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

        # print(tempApps)

#function clear button
label = None
def clearProgram():
    apps.clear()
    lblresult.configure(text="")
    if label is not None:
        label.configure(image="")
        label.configure(text="")
        label.image = None
        # label.place(relx=0.5, rely=0.3)



#function browse button
# def browse_button():
#     global filename
#     global label
    
#     # Prompt the user to select a file
#     filename = filedialog.askopenfilename(initialdir="/",title="Select File",
#                                           filetypes= (("all files","*.*"),("exe","*.exe")))
#     apps.append(filename)
    
#     for app in apps:
#         label = tk.Label(frame2,text=app,bg="white" ) 
#         label.pack()
#         img = Image.open(filename)
#         img= img.resize ((200,150))
#         img = ImageTk.PhotoImage(img)
#         label.configure(image=img)
#         label.image = img
        
#     return filename         
def addApp():

    # for widget in frame.winfo_children():
    #     widget.destroy()

    global filename, label

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("all files","*.*"),("exe","*.exe")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()
        img = Image.open(filename)
        img= img.resize ((200,150))
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)
        label.image = img

new_model = tf.keras.models.load_model('saved_model/my_model')
#function run app button
# def runApp():
#     global filename
#     img = tf.keras.preprocessing.image.load_img(
#         filename, target_size=(img_height, img_width))
#     img_array = keras.preprocessing.image.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)  # Create a batch
#     predictions = model.predict(img_array)
#     score = tf.nn.softmax(predictions[0])
#     output = "The image is like a {} with a {:.2f} percent confidence.".format(
#         class_names[np.argmax(score)], 100 * np.max(score))

#     lblresult.configure(text=output)

def runApp():
    global filename

    if filename:
        img = tf.keras.preprocessing.image.load_img(
            filename, target_size=(img_height, img_width))
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        output = "The image is like a {} with a {:.2f} percent confidence.".format(
            class_names[np.argmax(score)], 100 * np.max(score))

        lblresult.configure(text=output)
    else:
        lblresult.configure(text="No file selected.")


# def runApps():
#     for app in apps:
#         os.startfile(app)


root.title("ANIMAL RECOGNITION")
root.configure(bg="#F0F0F0")

canvas = tk.Canvas(root, height=500, width=500, bg="#008000")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.3)

lbl_title = tk.Label(root, text="ANIMAL RECOGNITION", font=('Courier New', 14, 'bold'), bg="#F0F0F0")
lbl_title.pack(pady=10)


lblresult = tk.Label (canvas, font=('Courier New', 10, 'bold'), bg='#BEBEBE')
# result_window = canvas.create_window(10, 400, anchor=tk.NW, window=lblresult)
result_window = canvas.create_window(10, 10, anchor=tk.NW, window=lblresult)
openFile = tk.Button(root, text="Open File", padx=5, pady=2, fg="white", bg="#008000", command=addApp)
openFile.pack()

runApp = tk.Button(root, text="Run Apps", padx=5, pady=2, fg="white", bg="#008000", command=runApp)
runApp.pack()

clearProgram = tk.Button(root, text='Clear All', padx=5, pady=2, fg="white", bg="#263D42", command=clearProgram)
clearProgram.pack()



# lblresult.pack()


openFile.pack(pady=5)

runApp.pack(pady=5)

clearProgram.pack(pady=5)


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.text', 'w') as f:
    for app in apps:
        f.write(app +',')