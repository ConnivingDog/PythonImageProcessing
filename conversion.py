import os
import io
import math

from PIL import Image

# canvas size
width = 200
height = 200
size = width, height

# canvas color
canvas_color = 255, 255, 255

current_dir = str(os.getcwd()) + '\\'

files = os.listdir(current_dir)

save_path = input('folder name : ')

for f in files:
    if not str(f).startswith('.'):
        if not str(os.path.splitext(f)[1]) == '.py':

            converted_name = '\\' + str(os.path.splitext(f)[0]) + '.jpg'

            im = Image.open(current_dir + f).convert('RGB')
            
            im.thumbnail(size, Image.ANTIALIAS)

            orig_img_width = im.width
            orig_img_height = im.height

            conv_img = Image.new('RGB', size, canvas_color)

            # center alignment
            x1 = int(math.floor((width - im.width) / 2))
            y1 = int(math.floor((height - im.height) / 2))

            #pasting to canvas
            conv_img.paste(im,(x1, y1, x1 + orig_img_width, y1 + orig_img_height))

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            conv_img.save(save_path + converted_name ,'JPEG',quality = 95)
        
        else:
            pass
            break

#destroy original files
for f in files:
    if str(f).lower().endswith('.png') or str(f).lower().endswith('.jpg') :
        os.remove(os.path.join(current_dir, f))