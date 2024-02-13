import glob
import os
from PIL import Image, ImageSequence


def data_maker(project_path):
    data_dict, random_limits, items_name = [], [], []
    folders = [folder+"/" for folder in sorted(glob.glob("/"+project_path + "*"))]
    for folder in folders:
        data_dict.append([])
        items_name.append([])
        print(f'Getting data from {folder}')
        for img_counter, img in enumerate(sorted(glob.glob(folder + '*.*'))):
            image = Image.open(img)
            head, tail = os.path.split(image.filename)
            items_name[-1].append(tail.replace(".png", ""))
            match image.format:
                case 'PNG':
                    new_image = image.convert('RGBA').resize((150, 150))
                    data_dict[-1].append([new_image for _ in range(10)])
                case 'GIF':
                    data_dict[-1].append([frame.convert('RGBA').resize((150, 150)) for frame in ImageSequence.Iterator(image)])
        random_limits.append(img_counter)


    return data_dict, folders, random_limits, items_name
