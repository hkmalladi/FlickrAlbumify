import json
import os
with open('meta/albums.json') as f:
  data = json.load(f)
  album_list = data.get('albums')
  for album in album_list:
        pics = album.get('photos')
        title = album.get('title')
        print('PROCESSING: ' + title)
        folder = 'media/' + title.replace(' ', '_')
        os.system('mkdir ' + folder)
        for pic in pics:
            os.system('ls media/*' + pic + '* > tmp.txt')
            with open('tmp.txt', 'r') as g:
                filenames = g.readlines()
                for filename in filenames:
                    filename = filename.strip('\n')
                    os.system('mv ' + filename + ' ' + folder)
