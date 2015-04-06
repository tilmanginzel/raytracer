'''
Copyright (c) 2014 Tilman Ginzel
This code is licensed under MIT license (see LICENSE.txt for details).

Created on 20.04.2014

usage: run.py [-h] -r  [-s ] [-v] [-m] [-a] [-o] [-set] [-nd]

Simple Raytracer by Tilman Ginzel

optional arguments:
  -h, --help          show this help message and exit
  -r , --recursive    sets recursive depth, e.g. -r 3 (required)
  -s  , --size        sets the size, e.g. -s 400 400
  -v, --verbose       enable live visualization while processing (slower)
  -m, --material      enable materials
  -a, --antialiasing  enables 4xSSAA (hence, 4 times slower)
  -o, --output        saves image to "./saves/"
  -set , --setting    choose between two settings. -set 1 or -set 2
  -nd, --no-display   this should only be set if the script runs on a server
                      without a $DISPLAY environment variable set!
'''
import main.raytracer
main.raytracer.main()