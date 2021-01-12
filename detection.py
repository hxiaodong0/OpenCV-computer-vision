import cv2
#load, resize, import, export

# img = cv2.imread("galax.jpeg", 0) # Using 0 to read image in grayscale mode
#
# print(type(img))   #<class 'numpy.ndarray'>
# print(img)        # produce an array
# print(img.shape)    #(900, 1600)
# print(img.ndim)     # 2-D for grayscale, 3-D for colored image;
#
# resized_image = cv2.resize(img,(int(img.shape[1]* 0.5), int(img.shape[0]*0.5))) #  (img object, (dimensionx, dimensiony))
# cv2.imshow("Galaxy", resized_image)  #("filename", img object)
# cv2.imwrite("Galaxy_halfed.jpeg", resized_image)
# cv2.waitKey(0)       #(2000 for 2 seconds)
# cv2.destroyAllWindows()

######################## practice