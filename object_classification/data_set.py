import os, shutil
original_dataset_dir = r'C:\Users\Mahmud\Desktop\Projects\my_personal\paper\object_tracking\box_raw'
base_dir = r'C:\Users\Mahmud\Desktop\Projects\my_personal\paper\object_tracking\box_out'
test_dir = os.path.join(base_dir, 'test')
validation_dir = os.path.join(base_dir, 'validation')
train_dir = os.path.join(base_dir, 'train')

os.mkdir(base_dir)
#except:0
os.mkdir(train_dir)
os.mkdir(validation_dir)
os.mkdir(test_dir)
#except:0

train_cats_dir = os.path.join(train_dir, 'box')
os.mkdir(train_cats_dir)
#train_dogs_dir = os.path.join(train_dir, 'dogs')
#os.mkdir(train_dogs_dir)
validation_cats_dir = os.path.join(validation_dir, 'box')
os.mkdir(validation_cats_dir)
#validation_dogs_dir = os.path.join(validation_dir, 'dogs')
#os.mkdir(validation_dogs_dir)
test_cats_dir = os.path.join(test_dir, 'box')
os.mkdir(test_cats_dir)
#test_dogs_dir = os.path.join(test_dir, 'dogs')
#os.mkdir(test_dogs_dir)
fnames = ['box.{}.jpg'.format(i) for i in range(25)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(train_cats_dir, fname)
 shutil.copyfile(src, dst)
 fnames = ['box.{}.jpg'.format(i) for i in range(25, 50)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(validation_cats_dir, fname)
 shutil.copyfile(src, dst)
 fnames = ['box.{}.jpg'.format(i) for i in range(50, 75)]
for fname in fnames:
 src = os.path.join(original_dataset_dir, fname)
 dst = os.path.join(test_cats_dir, fname)
 shutil.copyfile(src, dst)
