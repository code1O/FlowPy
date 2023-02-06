
"""Python Module for simplify some python libraries functions"""

# -*- coding: utf-8 -*-
# Hello world :)


# ====================================
# language: Spanish-MX, English-USA
# ====================================


from termcolor import colored
import os
from os import path
import psutil
from synthesizer import Synthesizer, Waveform, Player
import keyboard as kb
import playsound
import pyautogui as pyt
from time import sleep


# =====================================
# Programming language based on python
# =====================================


def checkStatus():
   if True:
      clear = lambda: os.system('cls')
      clear()
      print(colored(f"If this appears it´s because everything is fine, good job :) ", "green"))
      sleep(2)
      clear()


class commands:
   """Same functions as basic python"""

   def impr(text):

      """It prints any text"""

      txpr = (text)

      if txpr == False:
         print(colored(f"Error, Text not specified, found or empty", "red"))
      else:
         print(txpr)

   def ind(text):
      txinp = (text)

      """input data"""

      if txinp == False:
         print(colored(f"Error, input not specified, false or not structured", "red"))
      else:
         input(txinp)




# ============================
# Music typing notes generator
# ============================




class typing:

   # ========================
   #  MUSIC NOTES BY KEYWORDS
   # ========================

   def _init_keynotes(key):

      kb_key = (key)

      synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

      player = Player()

      player.open_stream()

      if kb.is_pressed(kb_key): # if a key is pressed it´ll play a music note
         player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 261.63, 0.1))
         if kb.is_pressed(kb_key):
               player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 293.66, 0.1))
         elif kb.is_pressed(kb_key): 
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 329.63, 0.1))
         elif kb.is_pressed(kb_key):
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 349.23, 0.1))
         elif kb.is_pressed(kb_key): 
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 392.00, 0.1))


   # ==========================
   #  MUSIC NOTES BY KEYNUMBERS
   # ==========================


   def _init_note_nums(key):

      """Play notes if a number is pressed (pc keyboard)"""

      numkey = (key)

      synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

      player = Player()

      player.open_stream()

      if kb.is_pressed(numkey): # if a key is pressed it´ll play a music note
         player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 261.63, 0.1))
         if kb.is_pressed(numkey):
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 293.66, 0.1))
         elif kb.is_pressed(numkey): 
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 329.63, 0.1))
         elif kb.is_pressed(numkey):
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 349.23, 0.1))
         elif kb.is_pressed(numkey): 
            player.play_wave(Synthesizer.generate_constant_wave(synthesizer, 392.00, 0.1))
      


# ======================================================
# PC information (Bytes, processor, frequency & more...)
#=======================================================



class pc:

   def get_bytes(bytes, suffix="B"):
      factorbytes = 1024
      for unit in ["", "K", "M", "G", "T", "P"]:
         if bytes < factorbytes:
            print(f"Bytes: {bytes: .2f}{unit}{suffix}")
         else:
            print(colored(f"Error bytes non calculated, try again", "red"))
         bytes /= factorbytes

   def get_freq():

      cpufreq = psutil.cpu_freq()

      print(f"max frequency: {cpufreq.max: .2f} MHz")
      print(f"min frequency: {cpufreq.min: .2f} MHz")


# ===================================
# COMMANDS (OS, PATHS & PIP COMMANDS)
# ===================================


class oscom:

   def _init_lib(library):
      libr = (library)
      if os.path.exists:
         print(colored(f"The library {libr} already exists on the system, try again with another library that doesn´t exists", "light_magenta"))
         exit()
      else:
         os.system(f"pip install {libr}")
      return None   
   
   def _init_os(command):
      comando = (command)
      os.system(comando)
      return None
   
   def _init_path(path):
      pth = (path)
      os.makedirs(pth)
      return None
   
   def _init_remove(path):
      pth = (path)
      if os.path.exists:
         os.remove(pth)
      return None

   def _init_two_commands(self, Command, command2):
      commands = (Command, command2)
      if commands == True:
         oscom._init_os(Command)
         oscom._init_os(command2)
      else:
         print(colored(f"The commands isn´t specified, try again", "red"))

# =============================
# DEFINES KEYBOARD PRESS EVENTS 
# =============================




class Keys:

   def holdkey(firstkey, secondkey):
   
      """KEYS ALLOWED: ALT, ALTGR, FN, CMD & SHIFT """

      fkey = (firstkey)
      skey = (secondkey)

      # Windows key: CTRL + ESC

      pyt.keyDown(fkey)
      pyt.keyDown(skey)

   def presskey(Key):

      """Keyboard numbers & words"""

      frstkey = (Key)
      pyt.press(frstkey)
   
   def _2key(Key, Secondkey):

      """Press two keys"""

      firstkey = (Key)
      secondkey = (Secondkey)

      pyt.press(firstkey)
      pyt.press(secondkey)
   
   def _3key(Key, Secondkey, Thirdkey):

      """Press three keys"""

      firstKey = (Key)
      secondkey = (Secondkey)
      thirdkey = (Thirdkey)

      pyt.press(firstKey)
      pyt.press(secondkey)
      pyt.press(thirdkey)
   
   def _4key(Key, Secondkey, Threekey, Fourthkey):

      """It´s enough to make a short phrase"""

      first = (Key)

      second = (Secondkey)

      thirst = (Threekey)

      fourth = (Fourthkey)

      pyt.press(first)

      pyt.press(second)

      pyt.press(thirst)

      pyt.press(fourth)
   
   def _5key(firstKey, secondKey, thirstKey, fourthKey, fiveKey):

      """Makes a middle phrase"""

      w = (firstKey)

      a = (secondKey)

      s = (thirstKey)

      d = (fourthKey)

      e = (fiveKey)

      pyt.press(w)

      pyt.press(a)

      pyt.press(s)

      pyt.press(d)

      pyt.press(e)
   
   def _10key(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10):

      frst5 = (_1, _2, _3, _4, _5)
      scnd5 = (_6, _7, _8, _9, _10)
      Keys._5key(frst5)
      Keys._5key(scnd5)

# =========================================
# Calls to a program or command with a key
# =========================================

class callKeys:

   def winbt(key): #Key that calls to windows button´s function
      keys = (key)
      if kb.is_pressed(keys):
         Keys.holdkey("CTRL", "ESC") #Windows button

   def Cmd(key): #Key that calls to CMD
      keys = (key)
      if kb.is_pressed(keys):
         os.system("cmd.exe")
   
   def task(key): #Key that calls to taskmgr.exe
      keys = (key)
      if kb.is_pressed(keys):
         os.system("taskmgr.exe")
   
   def path(key, path): #Key that open a path
      keys = (key)
      pth = (path)
      if kb.is_pressed(keys):
         if os.path.exists(pth):
            os.system(pth)
   
   def sound(key, path): #Key that play sound from a path (.mp4, mp3. wav, etc..)
      keys = (key)
      pth = (path)
      if kb.is_pressed(keys):
         playsound(pth)

class Opy:

   def IntVar(self, VariableInt:int, VariableString:str, VariableFloat: float,):

      VarsInt = (VariableInt)

      VarsFloat = (VariableFloat)

      Varstring = (VariableString)

      Opy.IntVar(Opy.IntVar.VarsInt)
   
      Opy.FlotVar(VarsFloat)

      Opy.strVar(Varstring)
   

if __name__ == '__main__':
   checkStatus()