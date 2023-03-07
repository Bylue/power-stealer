import os
import requests
import ctypes

new_wallpaper_url = ""

SPI_SETDESKWALLPAPER = 20
def set_wallpaper(image_path):
    # Download the image if the path is a URL
    if image_path.startswith('http'):
        response = requests.get(image_path, stream=True)
        if response.status_code == 200:
            # Save the image to a temporary file
            temp_path = os.path.join(os.environ['TEMP'], 'wallpaper.png')
            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            image_path = temp_path
        else:
            print('Failed to download image')
            return

    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print('Wallpaper changed successfully')
if __name__ == '__main__':
    # Example usage with a URL
    image_url = new_wallpaper_url
    set_wallpaper(image_url)
