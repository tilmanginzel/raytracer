'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 18.04.2014
'''

from Tkinter import Tk, Frame, Canvas, Label, PhotoImage
from PIL import ImageTk, Image , ImageFile
from settings.DefaultSetting import DefaultSetting
from settings.SpaceSetting import SpaceSetting
from settings.RoomSetting import RoomSetting
from main.Processor import Processor
from datetime import datetime
import time
import os
import sys
import argparse

def saveImage(image, args):
    """
    This method generates a filename dependent on given parameters and saves the file afterwards to ./saves.
    The folder ./saves will be created if it does not exist already.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename = timestamp + ' raytracer.py'
    filename += ' -r '+ str(args['recursive'][0])
    filename += ' -s '+ str(args['size'][0]) +' '+ str(args['size'][1])
    filename += ' -v' if args['verbose'] else ''
    filename += ' -m' if args['material'] else ''
    filename += ' -o' if args['output'] else ''
    filename += ' -a' if args['antialiasing'] else ''
    filename += ' -set '+ str(args['setting'][0])

    if not os.path.exists('saves'):
        os.makedirs('saves')
        print 'created folder ./saves'
    
    image.save('saves/'+filename+'.jpg', 'JPEG', quality=100, optimize=True, progressive=True)
    print 'image saved to "./saves/'+filename+'.jpg"'

def checkPositiveInt(value):
    """This method checks if an argparse parameter has a positive integer value."""
    
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError('%s is an invalid positive int value' % (value))
    return value

def main():   
    ImageFile.MAXBLOCK = 4096*2304 # this is only required for older PIL versions, if PILs output buffer is not large enough. see: https://mail.python.org/pipermail/image-sig/1999-August/000816.html
    
    parser = argparse.ArgumentParser(description='Simple Raytracer by Tilman Ginzel')
    parser.add_argument('-r', '--recursive', help='sets recursive depth, e.g. -r 3 (required)', nargs=1, type=checkPositiveInt, required=True, metavar='')
    parser.add_argument('-s', '--size', help='sets the size, e.g. -s 400 400', nargs=2, default=[400, 400], type=checkPositiveInt, required=False, metavar='')
    parser.add_argument('-v', '--verbose', help='enable live visualization while processing (slower)', required=False, action='store_true')
    parser.add_argument('-m', '--material', help='enable materials', required=False, action='store_true')
    parser.add_argument('-a', '--antialiasing', help='enables 4xSSAA (hence, 4 times slower)', required=False, action='store_true')
    parser.add_argument('-o', '--output', help='saves image to "./saves/"', required=False, action='store_true')
    parser.add_argument('-set', '--setting', help='choose a setting. -set 1 - 3', required=False, nargs=1, default=[1], type=int, metavar='')
    parser.add_argument('-nd', '--no-display', help='this should only be set if the script runs on a server without a $DISPLAY environment variable set!', required=False, action='store_true')
    
    try:
        args = vars(parser.parse_args())
    except:
        parser.print_help()
        sys.exit(1)

    settingId =  args['setting'][0]
    if settingId == 1: # default setting
        setting = DefaultSetting(width=args['size'][0], height=args['size'][1], recursiveDepth=args['recursive'][0], showMaterial=args['material'])
    elif settingId == 2: # space setting
        setting = SpaceSetting(width=args['size'][0], height=args['size'][1], recursiveDepth=args['recursive'][0], showMaterial=args['material'])
    elif settingId == 3: # room setting
        setting = RoomSetting(width=args['size'][0], height=args['size'][1], recursiveDepth=args['recursive'][0], showMaterial=args['material'])
    else: # default setting
        setting = DefaultSetting(width=args['size'][0], height=args['size'][1], recursiveDepth=args['recursive'][0], showMaterial=args['material'])

    # display is used to set whether you want to have a visual feedback in a graphical user interface.
    display = not args['no_display'] # easier to read and you do not have to negotiate it on every call 

    if display:
        window = Tk()
        window._root().wm_title('Raytracer - Tilman Ginzel (173388)')

        if args['verbose']:
            can = Canvas(window, width=setting.WIDTH, height=setting.HEIGHT)
        else:
            frame = Frame(window, width=setting.WIDTH, height=setting.HEIGHT)
            can = Canvas(frame, width=setting.WIDTH, height=setting.HEIGHT)
            frame = Frame(window)
        
        can.pack()

        # photoImage is used to show live changes while processing
        if args['verbose']:
            photoImage = PhotoImage(width=setting.WIDTH, height=setting.HEIGHT)
            can.create_image((setting.WIDTH/2, setting.HEIGHT/2), image=photoImage, state="normal")
    
    # pilImage is used to save the image after processing or if verbose is deactivated
    pilImage = Image.new("RGB", (setting.WIDTH, setting.HEIGHT), (0, 0, 0))
    
    start = time.clock()
    processor = Processor(setting, display=display, ssaa=args['antialiasing'])
    print 'start processing...'
    for pixel in processor.startProcessing():
        if display and args['verbose']:
            photoImage.put("#%02x%02x%02x" %((pixel[1][0], pixel[1][1], pixel[1][2])), (pixel[0][0], pixel[0][1]))
            if pixel[0][1] == setting.HEIGHT-1: # if y == bottom, update canvas
                can.update()
        
        pilImage.putpixel((pixel[0][0], pixel[0][1]), ((pixel[1][0], pixel[1][1], pixel[1][2])))
    
    end = time.clock()
    print 'done'
    print 'duration: %2.2f seconds' %(end-start)
    
    if display and not args['verbose']:
        tkImage = ImageTk.PhotoImage(pilImage)
        label = Label(image=tkImage)
        label.image = tkImage
        label.pack()
        can.pack()
        
    if args['output']:
        saveImage(pilImage, args)
    
    if display:
        window.mainloop()
        
if __name__ == '__main__':
    main()
    
    