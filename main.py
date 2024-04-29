import time
import pygame
import os
import signal
import sys
import glob
import random
from adafruit_servokit import ServoKit
from pygame import mixer

def sig_handler(signal, frame):
    """ Handle signals """
    print('Cleaning Up')
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)

kit = ServoKit(channels=16)

os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.joystick.init()
pygame.display.init()
pygame.init()

while True:
    pygame.joystick.quit()
    pygame.joystick.init()
    num_joysticks = pygame.joystick.get_count()
    if __debug__:
        print(f"Waiting for joystick... (count {num_joysticks})")
    if num_joysticks != 0:
        break
    time.sleep(5)

j = pygame.joystick.Joystick(0)
j.init()

#########################################################
# Ripped this out of my R2 Control system! 
class _AudioLibrary(object):
    """
    The class for playing audio samples via pygame mixer

    Sounds are stored in a single directory. The following prefixes are used
    to group sets of sounds for random play. Any other filenames can be played
    as normal.

    """

    def __init__(self, sounds_dir, volume):
        """
        Init of AudioLibrary class

        Parameters
        ----------
        sounds_dir : str
             Directory containing sound files
        volume : float
             Initial volume level
        """

        if __debug__:
            print(f"Initiating audio: sounds_dir = {sounds_dir}")
        mixer.init()
        mixer.music.set_volume(float(volume))
        self.sounds_dir = sounds_dir

    def TriggerSound(self, data):
        """
        Play a sound

        Parameters
        ----------
        data : str
             Name of file (not including extension)
        """

        if __debug__:
            print(f"Playing {data}")
        audio_file = self.sounds_dir + data + ".mp3"
        # mixer.init()
        if __debug__:
            print("Init mixer")
        mixer.music.load(audio_file)  # % (audio_dir, data))
        if __debug__:
            print(f"{audio_file} Loaded")
        mixer.music.play()
        if __debug__:
            print("Play")

    def TriggerRandomSound(self, data):
        """
        Take one of the prefixes and play a random sound from the library

        Parameters
        ----------
        data : str
             Sound group prefix
        """

        file_list = glob.glob(self.sounds_dir + data + "/*.mp3")
        file_idx = len(file_list) - 1
        audio_file = file_list[random.randint(0, file_idx)]
        if __debug__:
            print(f"Playing {data}")
        mixer.init()
        if __debug__:
            print("Init mixer")
        mixer.music.load(audio_file)  # % (audio_dir, data))
        if __debug__:
            print(f"{audio_file} Loaded")
        mixer.music.play()
        if __debug__:
            print("Play")

    def ListSounds(self):
        """ Returns the list of sounds available """
        files = ', '.join(glob.glob(self.sounds_dir + "*.mp3"))
        files = files.replace(self.sounds_dir, "", -1)
        files = files.replace(".mp3", "", -1)
        return files


audio = _AudioLibrary("./sounds/", 0.3)
 
# Play a sound on startup
audio.TriggerSound("bd-1-woo-hoo")

# There is a joystick!
joystick = True
debug_me = False

########################################################################
# Main loop. Whilst joystick is true, constantly run this. If the joystick disappears then joystick will get set to false, causing the 
# whole script to end and get restarted by systemd. 
while joystick:
   if os.path.exists('/dev/input/js0'):
      if debug_me:
         print("Joystick still there....")
   else:
      print("No joystick")
      joystick = False
   events = pygame.event.get()
   for event in events:
      if event.type == pygame.JOYAXISMOTION:
         if event.axis == 0:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[0].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 1:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[1].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 2:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[2].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 3:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[3].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 4:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[4].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 5:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[5].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 6:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[6].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

         if event.axis == 7:
            print(f"Joystick value = {event.value} Servo angle = {(event.value + 1) * 90}")
            try:
               kit.servo[7].angle = (event.value + 1) * 90
            except Exception as e:
               print(f"Error! {e}")

      if event.type == pygame.JOYBUTTONDOWN:
         if event.button == 0:
            try:
               audio.TriggerSound("bd-1-woo-hoo")
            except Exception as e:
               print(f"Failed to play sound: {e}")
         if event.button == 1:
            try:
               audio.TriggerRandomSound("BD/Happy")
            except Exception as e:
               print(f"Failed to play sound: {e}")
         if event.button == 2:
            try:
               audio.TriggerRandomSound("BD/Angry")
            except Exception as e:
               print(f"Failed to play sound: {e}")
         if event.button == 3:
            try:
               audio.TriggerRandomSound("BD/Sad")
            except Exception as e:
               print(f"Failed to play sound: {e}")


