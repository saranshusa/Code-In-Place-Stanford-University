"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for px in patch:
        px.red *= red_scale
        px.green *= green_scale
        px.blue *= blue_scale
    return patch

def add_patch(images, patch):
    for X in range(0, WIDTH, PATCH_SIZE):
        for Y in range(0, HEIGHT, PATCH_SIZE):
            for x in range(PATCH_SIZE):
                for y in range(PATCH_SIZE):
                    pixel = patch.get_pixel(x,y)
                    images.set_pixel(X+x, Y+y, pixel)
    return images

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image = add_patch(final_image, patch)
    final_image.show()

if __name__ == '__main__':
    main()
