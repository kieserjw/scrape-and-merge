#!/bin/bash

pip install Pillow

#download images
python scrape.py

#merge images
python merge.py

