I am posting this so that others can continue or modify it, as I currently have no further ideas and at the moment its not that hard to find in a screenshare.

To bypass detection, you should compile the .py file into a single .exe file using a tool like AutoPyToExe. Otherwise, a staff member could easily find the Python source code of the open file, leading to immediate detection.

It is preferable to place the PyLib file within the Python 'configuration' directories, as this can effectively confuse staff members and thus better conceal the file.

Notice that using a tool like Process Hacker to analyze the memory of the running process can reveal imported modules, such as pynput. If these modules are detected by a staff member, it could result in a ban.
