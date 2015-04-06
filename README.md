# raytracer
A simple recursive 3D raytracer written in python.

During my studies at the RheinMain University of Applied Science we had to write a raytracer in python.
This took place in a fourth semester course called *Generative Computergrafik* lectured by Prof. Dr. U. Schwanecke in 2014.

This project is licensed under the MIT license (see LICENSE.txt for details), so feel free to fork the project.

## Requirements
* [Python 2.7 or higher](https://www.python.org/downloads/)
* [NumPy](http://www.numpy.org/)
* [PyOpenGL](http://pyopengl.sourceforge.net/)
* [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/)

Windows user can find suitable python packages here: http://www.lfd.uci.edu/~gohlke/pythonlibs/

## How to use
```
run.py [-h] -r  [-s ] [-v] [-m] [-a] [-o] [-set] [-nd]

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

## Results

### Image 1

Required result during the course. Larger version: [1920x1200](https://raw.githubusercontent.com/tilmanginzel/raytracer/master/saves/2014-04-20%2014-20-52%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a.jpg?token=ADuAraMf9HPug5LDwjCta0h8AJfGr6wvks5VK5W6wA%3D%3D)

```
run.py -r 3 -s 1920 1200 -m -o -a
```

![](saves/2014-04-20%2014-20-52%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a.jpg)

### Image 2

Texture to sphere mapping. Larger version: [1920x1200](https://raw.githubusercontent.com/tilmanginzel/raytracer/master/saves/2014-04-20%2018-48-40%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a%20-set%202.jpg?token=ADuAreeN6kNNPShB_pQIY00bg26Tun5aks5VK5cBwA%3D%3D)

```
run.py -r 3 -s 1920 1200 -m -o -a -set 2
```

![](saves/2014-04-20%2018-48-40%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a%20-set%202.jpg)

### Image 3

Fiddling around with some settings. Larger version: [1920x1200](https://raw.githubusercontent.com/tilmanginzel/raytracer/master/saves/2014-04-23%2019-31-16%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a%20-set%203.jpg?token=ADuArSYx6RSve0gBfvHkAf0cnGUUloNpks5VK5dXwA%3D%3D)

```
run.py -r 3 -s 1920 1200 -m -o -a -set 3
```

![](saves/2014-04-23%2019-31-16%20raytracer.py%20-r%203%20-s%201920%201200%20-m%20-o%20-a%20-set%203.jpg)

