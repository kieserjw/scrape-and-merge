#!/usr/bin/env python

import urllib
import time 

if __name__ == '__main__':
   url = 'http://extrazoom.com/files/gef/image-5418/13/'
   ext = '.jpeg'
   sleep_time = 10
   
   rows = 14
   cols = 10
   
   for i in range(0, rows):
      for j in range(0, cols):

         file_name = str(i) + "_" + str(j) + ext         
         
         #save the file to disk
         urllib.urlretrieve(url + file_name, file_name)
         print url + file_name
         
         #A lot of requests in a row might cause timeouts
         time.sleep(sleep_time)
