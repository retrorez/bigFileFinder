#! python3

# Deleting Unneccessary Files - Searches for files over
# 100mb and prints them and their directory to the screen

import os

print('Welcome to the Big File Finder! \nI find all files over 100mb and show them to you!')

for folderName, subfolders, filenames in os.walk('C:\\'):

    for filename in filenames:
        try:
            if os.path.getsize(folderName + '\\' + filename) > 100 * 1024 * 1024:
                print(filename + ' \n ' + os.path.join('C:\\code\\python', filename))
                fileSize = os.path.getsize(folderName + '\\' + filename) / 1024 / 1024
                print(str(int(fileSize)) + 'mb')
        except Exception as err:
            print('An exception has happened: ' + str(err))
