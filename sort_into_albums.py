#!/usr/bin/python3
import json
import os
import glob
import shutil

list_of_files = glob.glob('*.json')
for filename in list_of_files:
   os.remove(filename)
quit()

with open('albums.json') as f:
  data = json.load(f)
  album_list = data.get('albums')
  for album in album_list:
        pics = album.get('photos')
        title = album.get('title')
        print('PROCESSING: ' + title)
        folder =  title.replace(' ', '_').replace('<','LT').replace('>','GT')
        try:
            if not os.path.exists(folder):
                os.mkdir(folder)
        except Exception as e:
            print('Folder ', folder, ' exists')
            print('Exception: ', e)
        for pic in pics:
            list_of_files = glob.glob('photo_' + pic + '.json')
            for filename in list_of_files:
                  os.remove(filename)

        for pic in pics:
            list_of_files = glob.glob('*_' + pic + '_*')
            for filename in list_of_files:
                filename = filename.strip('\n')
                try:
                    shutil.move(filename, folder)
                    print('mv ' + filename + ' ' + folder)
                except Exception as e:
                    print('mv ' + filename + ' ' + folder + ' FAILED')
                    print('Exception: ', e)
        for pic in pics:
            list_of_files = glob.glob(pic + '_*')
            for filename in list_of_files:
                filename = filename.strip('\n')
                try:
                    shutil.move(filename, folder)
                    print('mv ' + filename + ' ' + folder)
                except Exception as e:
                    print('mv ' + filename + ' ' + folder + ' FAILED')
                    print('Exception: ', e)
        for pic in pics:
            list_of_files = glob.glob('*_' + pic + '.*')
            for filename in list_of_files:
                filename = filename.strip('\n')
                try:
                    shutil.move(filename, folder)
                    print('mv ' + filename + ' ' + folder)
                except Exception as e:
                    print('mv ' + filename + ' ' + folder + ' FAILED')
                    print('Exception: ', e)

for pic in pics:
    list_of_files = glob.glob('*.json')
    for filename in list_of_files:
        os.remove(filename)
