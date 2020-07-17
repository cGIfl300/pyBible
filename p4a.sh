#!/bin/bash
p4a apk --private $HOME/code/myapp --package=org.rtfd.pybible --name "pyBible" --version 1.0 --bootstrap=sdl2 --requirements=python3,tkinter,pillow,peewee,pygame
