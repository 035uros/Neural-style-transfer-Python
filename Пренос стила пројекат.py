# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:39:48 2022

@author: Uroš
"""

from tkinter import *
from PIL import Image, ImageTk

import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2 

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2') #учитавање модела

#претпроцесирање слика
def load_image(img_path):
    img = tf.io.read_file(img_path)                         #учитавање слике
    img = tf.image.decode_image(img, channels=3)            #препознавање формата слике и осигуравање броја канала
    img = tf.image.convert_image_dtype(img, tf.float32)     #конвертовање у флоат32
    img = img[tf.newaxis, :]                                #"паковање слике" у низ
    return img


osnova = 'golf.png'
stilzatransfer = 'starrynight.jfif'

root=Tk()
root.geometry('900x1000')
myLabel = Label(root, text="Пренос стила помоћу неуронских мрежа")

def buttonfunction():
    index= l.get(ANCHOR)
    index1= l1.get(ANCHOR)
    osnova=slike[index]
    stilzatransfer=stilovi[index1]
    content_image = load_image(osnova)                  #претпроцесирање слике на коју примењујемо стил
    style_image = load_image(stilzatransfer)            #претпроцесирање слике са које узимамо стил

    content_image.shape #формат слике, број, ширина, висина, канали

    plt.imshow(np.squeeze(content_image)) #"вађење" слике
    plt.show()
    plt.imshow(np.squeeze(style_image)) #"вађење" слике
    plt.show()

    stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

    plt.imshow(np.squeeze(stylized_image))
    plt.show()

    cv2.imwrite('generated_img1.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))
    
    image3 = Image.open('generated_img1.jpg')
    test3 = ImageTk.PhotoImage(image3)

    label3 = Label(image=test3)
    label3.image = test3

    # Position image
    label3.place(x=100, y=500)
    root.mainloop()




myLabel.pack()


slike={
       'Голф': 'golf.png',
       'Урош': 'uros1.jpg',
       'ФИН - 1': 'fink.jpg',
       'Фин - 2': 'fink2.jpg'
       }
l=Listbox(root)
for x, y in enumerate(slike):
    l.insert(x+1, y)
l.pack(anchor='w')
l.place(x=200, y=30)

def slika(imga):
    
    image1 = Image.open(imga)
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=500, y=30)
    root.mainloop()
    

def slika2(imga2):
    
    image1 = Image.open(imga2)
    test = ImageTk.PhotoImage(image1)

    label2 = Label(image=test)
    label2.image = test

    # Position image
    label2.place(x=500, y=300)
    root.mainloop()



def odabirslike():
    index= l.get(ANCHOR)
    slika(slike[index])
    pass

b1= Button(root, text="Oдабери слику", command=odabirslike)
b1.pack()
b1.place(x=380, y=100)

stilovi={
       'Звездано небо - Ван Гог': 'starrynight.jfif',
       'Упорност сећања - Салвадор Дали': 'dali.jpeg',
       'Крик - Едард Мунк': 'scream.jpg',
       'Мона Лиза - Леонардо да Винчи': 'mona.png',
       }
l1=Listbox(root)
for x, y in enumerate(stilovi):
    l1.insert(x+1, y)
l1.pack(anchor='w')

l1.place(x=200, y=250)

#slika('starrynight.jfif')
def odabirstila():
    index= l1.get(ANCHOR)
    slika2(stilovi[index])
    pass


b2= Button(root, text="Одабери стил", command=odabirstila)
b2.pack()
b2.place(x=380, y=400)

b= Button(root, text="Пренос стила", command=buttonfunction)
b.pack()
b.place(x=380, y=480)

root.mainloop()