# Python for Numerical Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC

## Week 2 Lesson 3

### HW 1
### Why is np.transpose(img, (1, 0, 2)) NOT the same as np.rot90(img)

### Practically speaking, np.transpose(img, (1, 0, 2)) results in an image that is rotated, and then inverted along the vertical axis, while np.rot90(img) performs the expected image manipulation.

### HW 2
### Use a *for* loop to create the figures in the following code.

# ```python
if __name__=="__main__":
    import matplotlib.pyplot as plt
    from matplotlib.image import imread 
    import numpy as np
    file_nm = "./ant_logo.png"
    img = imread(file_nm) ## Note we do not have to close this
    img.shape #(500,300,4) Look an alpha channel
    A = np.transpose(img, (1, 0, 2)).copy()
    B = np.rot90(img).copy()  ## We need to copy() here if we want a new object
    figs = {"A": A, "B": B, "img":img}
    for key in figs:
        plt.figure(key)
        plt.imshow(figs[key])
    plt.show()  # Display it to screen
    plt.close()  # Make sure everything is closed
# Lets view it But rotated
# A = np.transpose(img, (1, 0, 2)).copy()
# B = np.rot90(img).copy()  ## We need to copy() here if we want a new object
# plt.figure("A")
# plt.imshow(A) #Make an image plot object
# plt.figure("B")
# plt.imshow(B) #Make an image plot object
# plt.figure("Ant Logo")
# plt.imshow(img)

# ```


### HW 3
### When importing the following: numpy and pandas, what is the common alias used.

### Numpy is commonly imported 'as np'.  Pandas is commonly imported 'as pd'.