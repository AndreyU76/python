Удовиченко

import os 
import shutil
 
def new_path(name):
    path = os.path.join(name)
    try:
        os.makedirs(path)
        print('Создана папка ' + name)
    except FileExistsError:
         print('Директория с таким именем уже есть')
          
if __name__ == "__main__":
    for i in range(1, 10):
    new_path('{}_{}'.format('dir', i))
 
