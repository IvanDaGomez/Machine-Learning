from tensorflow import keras
import matplotlib.pyplot as plt
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()
datagen = keras.preprocessing.image.ImageDataGenerator(
    rotation_range = 40, 
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode= 'nearest'
)

test_img = train_images[14]
img = keras.preprocessing.image.img_to_array(test_img)

img = img.reshape((1,) + img.shape) #Reshape image
#plt.imshow(train_images[14]) Initial image
#plt.show()
i = 0

for batch in datagen.flow(img, save_prefix='test', save_format = 'jpeg'):
    plt.figure(i)
    # ARRAY TO IMAGE
    plot = plt.imshow(keras.preprocessing.image.array_to_img(batch[0]))
    i += 1
    if i > 4: # Show 4 images
        break
plt.show()