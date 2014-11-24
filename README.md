ClipCommand
===========

Runs submitted command line commands on clipboard data, saving the results back to the clipboard

To run, just execute python2 ClipCommand.py, and a window will pop up. Make sure that your desired data is in the clipboard. Type your command into the text box, and press enter. When the window closes, the results of the command will be placed into your clipboard.

Requirements
------------
pygtk

Example
-------
Our clipboard data is "Hello world".

We run python2 ClipCommand.py, and type in base64 and press enter.

![ClipCommand](http://i.imgur.com/lXJ6N4m.png)

Now paste into a text editor, and we get "SGVsbG8gd29ybGQ=".

Notes
-----
 - This public version was developed so others could play around with the idea. A more involved version is in development, which also includes application/website shortcuts. Current revisions have shortcuts hard coded, and would be somewhat annoying to use.
 - Versioning and an install method will be added in the future.
 - It is suggested that this script is assigned to a keyboard/mouse shortcut, but provides no means to do this itself. Suggestions on how to go about this will be provided later.
 - It has only been tested on Ubuntu so far.
 - In order to use the clipboard in this way on the command line, I suggest using xclip for X based systems. For other operating systems, Google is your friend.