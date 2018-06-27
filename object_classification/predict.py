from keras.models import load_model
model = load_model('box.h5')
img_path=r'C:\Users\Mahmud\Desktop\Projects\my_personal\paper\object_tracking\box_out\test\box\box.53.jpg'

from keras.preprocessing import image
import numpy as np

img = image.load_img(img_path,target_size=(150,150,3))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor , axis=0)
img_tensor /=255.

print(model.predict(img_tensor))
