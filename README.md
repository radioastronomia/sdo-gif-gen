|==--== HOW TO USE ==--==| 

>>>download_sun_images.py
>>>example usage (cli):  python download_sun_images.py folder=solar_images year=2024 month=5 initial_day=5 end_day=9 save_step=10 filter=0335 filter_by=wavelength 
>>> download images with frequency 0335 from day 2024/05/05 up to 2024/05/09 in folder solar_images (folder must exist!)

>>>create_sun_gif.py
>>>example usage (cli): python download_sun_images.py filter=0335 folder_name=solar_images file_name=example.gif year=2024 month=5 initial_day=5 end_day=9 
>>> creates a gif in the current working directory with the downloaded images from the specified filter (frequency) located at the folder specified

!! WARNING !! 
!! too large gifs (a lot of days) may not be fully created due to python's proccess being killed. !!

@ IMAGES SOURCE @
https://sdo.gsfc.nasa.gov/assets/img/browse

for more info, go to https://sdo.gsfc.nasa.gov

$ DEPENDENCIES $
$   requests   $
$   imageio    $