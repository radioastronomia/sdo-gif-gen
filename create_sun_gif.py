from my_util import *
import imageio.v2 as imageio
import os

IMAGES_DIR = r'./'
               
def gify_imgs(folder_name, file_name, filter, ini_date, fin_date):
    file_list = os.listdir(folder_name + f'/{filter}/') 

    full_files = [os.path.join(IMAGES_DIR, folder_name, filter, file) for file in file_list]
    
    with imageio.get_writer(file_name, mode="I") as writer:
        for file_path in full_files:
            img_data = file_path.split('\\')[2].split('_')[0]
            if int(ini_date) <= int(img_data) <= int(fin_date):
                img = imageio.imread(file_path)
                writer.append_data(img)
        


def create_gif_one_filter(filter):

    folder_name = str(get_sys_arg())
    print(f'folder_name={folder_name}')
    file_name = str(get_sys_arg())
    print(f'file_name={file_name}')
    year = int(get_sys_arg())
    print(f'year={year}')
    month = int(get_sys_arg())
    print(f'month={month}')
    initial_day = int(get_sys_arg())
    print(f'initial_day={initial_day}')
    end_day = int(get_sys_arg())
    print(f'end_day={end_day}')

    ini_date = f'{year}{month:02d}{initial_day:02d}'
    fin_date = f'{year}{month:02d}{end_day:02d}'

    print('>>> generating gif...')
    gify_imgs(folder_name, file_name, filter, ini_date, fin_date)
    print('>>> gif created!')

create_gif_one_filter(get_sys_arg())