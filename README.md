# py2ducky
Translate your python code into DuckyScript for quick injection.
# Use Cases
Py2Ducky will take a .py, .pyi, or any python file and translate it to a DuckyScript friendly format, allowing for fast typing or injection. Py2ducky is perfect for when you want to inject a python script into a terminal, a plain text file, or anything that would require tedious translating to deal with spacing. 
# How To use
The script will prompt you to enter the name of the python file. Enter the file name including the ending. For example: `payload.py`. The script will then ask if you would like to save it under a custom file name. By defualt, it will save under the name of your input file. Example: `payload.py.txt`. That concludes your input!
# Extra info 
While using this script, make sure that your code contains no sytnax errors, as py2ducky will likely make them worse and harder to debug once you find them in the `.txt` file. Additionaly, the script may not act correctly if there are errors and the script will inject inncorect code when used. 
