import requests
import time
import os

BASE_URL = 'https://sdo.gsfc.nasa.gov/assets/img/browse/'
INI_IMG = 6
WAVELENGTH = 'wavelength'
FILTER_BY = 'wavelength'
FILTER = '0304'
IMG_DIMENSION = 1024
SAVE_STEP = 10
IMG_DAY_LIMIT = 100000000

def get_img_wavelength(img_name):
    return img_name.split('.')[0].split('_')[-1]

def get_img_dimensions(img_name):
    return img_name.split('.')[0].split('_')[2]

def filter_img_wavelength(filter, img_name):
    img_wavelength = get_img_wavelength(img_name)
    
    if filter == img_wavelength:
        return True
    return False

def parse_day(day_body, initial_parse=0,  parse_limit=1, filter=FILTER, filter_by=FILTER_BY):
    day_images_name = []
    i = initial_parse
    while True:
        try:
            img_name = parse_image_str(str(day_body).split('<a')[INI_IMG + i])
            img_file_dim = int(get_img_dimensions(img_name))            

            if not img_file_dim == IMG_DIMENSION:
                i += 1
                continue
            
            if filter_img_wavelength(filter, img_name) and filter_by == WAVELENGTH:
                day_images_name.append(img_name)
            
            elif filter_by == '':
                day_images_name.append(img_name)
            i += 1

            if i >= parse_limit:
                break
        except IndexError:
            return None

    return day_images_name

def parse_image_str(image_str):
    return image_str.split("\"")[1]

def create_img_dir(dir_name):
    try:
        cwd = os.curdir
        path = os.path.join(cwd, dir_name)
        os.mkdir(path)
    except FileExistsError:
        return None

def download_image(image_url, file_name):
    r = requests.get(image_url)
    with open(file_name, 'wb') as file:
        file.write(r.content)
        file.close()

def save_images(folder, day_body, day_url, parse_start, parse_step, filter=FILTER, filter_by=FILTER_BY):
    num_saved_imgs = 0
    daily_images = parse_day(day_body, parse_start, parse_start + parse_step, filter, filter_by)
    if daily_images is None:
        return None
    for image_name in daily_images:
        sub_dir_name = get_img_wavelength(image_name)
        image_url = f'{day_url}/{image_name}'
        num_saved_imgs += 1
        
        dir_path = os.path.join(os.curdir, f'{folder}', sub_dir_name)
        create_img_dir(dir_path)
        
        file_name = f'./{folder}/{sub_dir_name}/{image_name}'
        download_image(image_url, file_name)
    return num_saved_imgs

def save_daily_images(folder, year, month, initial_day=1, end_day=None, save_step=SAVE_STEP, img_limit=IMG_DAY_LIMIT, filter=FILTER, filter_by=FILTER_BY, show_status=False):
    if end_day is None:
        end_day = initial_day
    
    if filter_by is None:
        filter_by = ''
    
    ini_time = time.time()
    saved_imgs = 0
    for day in range(initial_day, end_day + 1):
        day_url = BASE_URL + f'{year}/{month:02d}/{day:02d}'
        r = requests.get(day_url)
        day_body = r.content
        
        print(f'day {day}')
        for i in range(0 , img_limit, save_step):
            saved_now = save_images(folder, day_body, day_url, i, save_step, filter, filter_by)
            print(saved_now)
            if saved_now is None:
                break
            saved_imgs += saved_now
            if show_status:
                total_time = time.time() - ini_time
                os.system('cls')
                print(f'>>> saving images...', )
                print(f'{saved_imgs} images saved!')
                print(f'{saved_imgs/total_time} images per second')



# TESTS
def main_test1():
    passed_time = time.time()
    save_daily_images(2024, 5, 1, 3)
    passed_time = time.time() - passed_time
    print(f'>>> process ended in {passed_time:.0f} seconds')

def main_test2():
    passed_time = time.time()
    save_daily_images(2024, 5, 1, 3, show_status=True)
    passed_time = time.time() - passed_time
    print(f'>>> process ended in {passed_time:.0f} seconds')

def main_test3():
    r= requests.get('https://sdo.gsfc.nasa.gov/assets/img/browse/2024/05/01')
    day_body = r.content
    day = parse_day(day_body, 0,  parse_limit=2000, filter='0304', filter_by='wavelength')
    print(day)

if __name__ == "__main__":
    main_test2()