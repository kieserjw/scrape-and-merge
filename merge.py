#!/usr/bin/env python

from PIL import Image

def merge_images(image1, image2, side_by_side, offset):
   """Merge two images into one, displayed side by side, or one on top of the other
   :param image1: first image
   :param image2: second image
   :param side_by_side: boolean indicating whether to merge horizontally or vertically
   :param offset: int indicating vertical offset that cuts overlapped pixels out
   :return: the merged Image object
   """
	
   (width1, height1) = image1.size
   (width2, height2) = image2.size

   if(side_by_side):
      result_width = width1 + width2
      result_height = max(height1, height2)
   else:
      result_width = max(width1, width2)
      result_height = height1 + height2


   result = Image.new('RGB', (result_width, result_height - offset))
   result.paste(im=image1, box=(0, 0))
   
   if(side_by_side):
      result.paste(im=image2, box=(width1, 0))
   else:
      result.paste(im=image2, box=(0, height1 - offset))
   return result


if __name__ == '__main__':
   
   ext = '.jpeg'
   final_image = Image
   
   #the images have about 4 pixels of vertical overlap
   offset = 4
   
   rows = 14
   cols = 10
   
   for i in range(0, rows - 1):
      final_row = Image.open(str(i) + '_0' + ext)

      for j in range(0, cols - 1):         
         #print i,j
         file2 = Image.open(str(i) + '_' + str(j + 1) + ext)
         final_row = merge_images(final_row, file2, True, 0)
      
      if(i is 0):
         #don't need to merge the first row with itself
         final_image = final_row
      else:
         final_image = merge_images(final_image, final_row, False, offset)

   final_image.save('final_image.jpeg')
