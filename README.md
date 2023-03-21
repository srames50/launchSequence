# launchSequence
A short project I made to make logging onto work a little easier :)


This Python script opens multiple URLs in Google Chrome and launches Discord using the OS module. It uses the webbrowser and os libraries to accomplish these tasks.

The URLs are stored in a list named "urls," and the for loop iterates through each URL and opens them in new tabs in the Chrome browser. Add the URL's that you want to open into the list. 

After opening the tabs, the script launches Discord using the OS module's startfile function. The path to the Discord executable is stored in the "command" variable, and it is passed to startfile to launch the program. Change this file path to any app you would like to open. 

Usage
Install Python: Before running this script, you'll need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

The script uses two libraries, webbrowser and os, which are typically included in standard Python installations. If you don't have these libraries installed, you can install them using pip, the Python package installer, by running the following commands in your command prompt or terminal:

pip install webbrowser
pip install os-sys

Modify URLs and Discord path: If you want to open different URLs in Chrome or launch a different program with the OS module, you can modify the values in the "urls" and "command" variables accordingly.

Save the code in a Python file (e.g., open_tabs.py) and run it by typing "python open_tabs.py" in your command prompt or terminal. The script will open the URLs in new tabs in Chrome and launch Discord.
