ClipCommand
===========

Runs submitted command line commands on clipboard data, saving the results back to the clipboard

To run, just execute python2 ClipCommand.py, and a window will pop up. Make sure that your desired data is in the clipboard. Type your command into the text box, and press enter. When the window closes, the results of the command will be placed into your clipboard.


Example
-------
 - Our clipboard data is "Hello world".
 - We run python2 ClipCommand.py, and type in base64 and press enter.
 - Now paste into a text editor, and we get "SGVsbG8gd29ybGQ=".

Notes
-----
 - This public version was developed so others could play around with the idea. A more involved version is in development, which also includes application/website shortcuts. Current revisions have shortcuts hard coded, and would be somewhat annoying to use.
 - Versioning and an install method will be added in the future.