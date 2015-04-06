# raytracer
A simple 3D raytracer written in python.

During my studies at the RheinMain University of Applied Science we had to write a raytracer in python.
This took place in a fourth semester course called *Generative Computergrafik* lectured by Prof. Dr. U. Schwanecke in 2014.

This project is licensed under the MIT license (see LICENSE.txt for details), so feel free to fork the project.

```
usage: run.py [-h] -r  [-s ] [-v] [-m] [-a] [-o] [-set] [-nd]

Simple raytracer by Tilman Ginzel. Copyright (c) 2014

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
```
