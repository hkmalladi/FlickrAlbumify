#!/usr/bin/python3
import json
import os
import glob
import shutil
with open('albums.json') as f:
  data = json.load(f)
  album_list = data.get('albums')
  for album in album_list:
        pics = album.get('photos')
        title = album.get('title')
        print('PROCESSING: ' + title)
        folder =  title.replace(' ', '_').replace('<','LT').replace('>','GT')
        try:
            os.mkdir(folder)
        except:
            print('Folder ', folder, ' exists')
        for pic in pics:
            list_of_files = glob.glob('*_' + pic + '_*')
            for filename in list_of_files:
                filename = filename.strip('\n')
                try:
                    shutil.move(filename, folder)
                    print('mv ' + filename + ' ' + folder)
                except:
                    print('mv ' + filename + ' ' + folder + ' FAILED')
