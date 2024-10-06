from get_sun_image import save_daily_images
from my_util import *

if __name__ == "__main__":
    my_args = {'folder': 'solar_imgs', 'year': 2024, 'month': 5, 'initial_day': 1, 'end_day': 10, 'save_step': 10, 'img_daily_limit': 100000000000, 'filter': '335', 'filter_by': 'wavelength'}
    
    my_args['folder'] =  str(get_sys_arg())
    my_args['year'] = int(get_sys_arg())
    my_args['month'] = int(get_sys_arg())
    my_args['initial_day'] = int(get_sys_arg())
    my_args['end_day'] = int(get_sys_arg())
    my_args['save_step'] = int(get_sys_arg()) 
    #my_args['img_daily_limit'] = int(get_sys_arg()) # uncomment if you want to limit the limit of daily images yourself
    my_args['filter'] = get_sys_arg() # example frequencies: 0335, 0304, 211193171, checkout https://sdo.gsfc.nasa.gov/assets/img/browse/ to see more
    my_args['filter_by'] = get_sys_arg() # to ignore filters, set filter_by as 'None'

    save_daily_images(my_args['folder'], my_args["year"], my_args["month"], my_args['initial_day'], my_args['end_day'], my_args['save_step'], my_args['img_daily_limit'], my_args['filter'], my_args['filter_by'], show_status=True)
    print(f'images from {my_args["year"]}/{my_args["month"]}/{my_args['initial_day']} to {my_args["year"]}/{my_args["month"]}/{my_args['end_day']} saved!')