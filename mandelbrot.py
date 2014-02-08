from PIL import Image
import random
from datetime import datetime
from os.path import abspath
import argparse

def map_range(value, start1, length1, start2, length2):
    '''
    Maps value from range determined by given values:
    
    @param start1: start of first interval
    @param length1: length of first interval
    @param start2: start of second interval
    @param length2: length of second interval
    
    @return: mapped value
    '''
    v1 = (value + start1) / float(length1)
    value = length2*v1 + start2
    return value

def mandelbrot(filename, width, height, max_iteration):
    '''
    Generates Mandelbrot fractal.
    
    @param filename: file name of file that will be created
    @param width: width of the image
    @param height: height of the image
    @param max_iteration: maximum number of iteration
    
    @return: absolute filename of generated image
    '''
    gradient_factor = 255.0 / max_iteration

    image = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    image.save(filename)

    pixels = image.load()
    for i in range(width):
        for j in range(height):
            x0 = map_range(i, 0, width, -2.5, 3.5)
            y0 = map_range(j, 0, height, -1, 2)
            
            (x, y) = (0, 0)
            
            iteration = 0
            
            while(x*x + y*y < 2*2 and iteration < max_iteration):
                xtemp = x*x - y*y + x0
                y = 2*x*y + y0
                x = xtemp
                iteration += 1
#                print iteration
            if iteration >= max_iteration:
                color = (0, 0, 10*iteration, 255)
            else:
                color = (int(gradient_factor*(iteration)), 0, 0, 255)
            
            pixels[i, j] = color
    image.save(filename)
    return abspath(filename)
    
if __name__=='__main__':
    command_line = argparse.ArgumentParser()
    command_line.add_argument('-x', '--width', type=int, required=True)
    command_line.add_argument('-y', '--height', type=int, required=True)
    command_line.add_argument('-i', '--iterations', type=int, required=True)
    command_line.add_argument('-o', '--output', required=True)
    args = command_line.parse_args()

    filename = mandelbrot(args.output, args.width, args.height, args.iterations)
    print('File {} created'.format(filename))

