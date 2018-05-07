import PIL
import matplotlib.pyplot as plt
import os.path     

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
chair_file = os.path.join(directory, 'chair.jpg')

# Open and show the chair in a new Figure window
chair_img = PIL.Image.open(chair_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(chair_img, interpolation='none')

# Display chair in second axes and set window to the right eye
axes[1].imshow(chair_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(300, 600) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(400, 225)
fig.show()

# Open, resize, and display bunny
bunny_file = os.path.join(directory, 'bunny.png')
bunny_img = PIL.Image.open(bunny_file)
bunny_small = bunny_img.resize((200, 200)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(bunny_img)
axes2[1].imshow(bunny_small)
fig2.show()

# Paste bunny on to chair
# Uses alpha from mask
# Change chair background color
pixels = chair_img.load() # create the pixel map
for i in range(chair_img.size[0]):    # for every col:
    for j in range(chair_img.size[1]):    # For every row
        if sum(pixels[i,j])>500: # brightness R+G+B goes up to 3*255=765
            pixels[i,j] = (100, j-150, 255) # set the colour accordingly

chair_img.paste(bunny_small, (300, 150), mask=bunny_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(chair_img, interpolation='none')
axes3[1].imshow(chair_img, interpolation='none')
axes3[1].set_xlim(250, 550)
axes3[1].set_ylim(350, 150)
fig3.show()