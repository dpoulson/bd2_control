# bd2_control

## Prereqs.

You will need pygame and servokit installed

## Install

Download repo either using git clone, or download the zip

Enter the directory and run the install script:

./install.sh

This will enable the systemd service so that everything will start on boot. 

You may need to adjust the volume using:

alsamixer

Just set it to max volume. 

If its still too quiet, you can edit the line that starts 'audio = _AudioLibrary' and change the number from 0.3 to something higher (anything below 1)
