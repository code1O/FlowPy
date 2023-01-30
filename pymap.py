# -*- coding: utf-8 -*-
# Hello world :)


# ====================================
# language: Spanish-MX, English-USA
# ====================================


from termcolor import colored
import platform
import os
from os import path
import psutil
from synthesizer import Synthesizer
from FlowPy.pv.mus import musnotes
import keyboard as kb
import FlowPy.pv.mus as muss
from FlowPy.pv.keys import keynum, ks, nums
import pyautogui as pyt


# =====================================
# Programming language based on python
# =====================================

if True:
   clear = lambda: os.system('cls')
   clear()
   print(colored(f"If this appears it´s because everything is fine, good job :) ", "green"))

class commands:

   __keys = []
   
   def Set(self, command, text):
      new = (command, text)
      self.__keys.append(new)

   def impr(text):

      """It prints any text"""

      txpr = (text)

      if txpr == False:
         print(colored(f"Error, Text not specified, found or empty", "red"))
      else:
         print(txpr)

   def ind(text):
      txinp = (text)

      if txinp == False:
         print(colored(f"Error, input not specified, false or not structured", "red"))
      else:
         input(txinp)

   def funt(Pyfunction):
      function
      return None




# ============================
# Music typing notes generator
# ============================




class typing:

   # ========================
   #  MUSIC NOTES BY KEYWORDS
   # ========================

   def _init_keynotes(status):
      """Status ON: True, status OFF: False"""
      st = (status)

      OFF = False
      ON = True

      if st == OFF:
         exit() 
      
      elif st == ON:

         synthesizer = Synthesizer

         if kb.is_pressed(ks): # if a key is pressed it´ll play a music note
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.DO2, 0.3))
         elif kb.is_pressed(ks):
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.RE2, 0.3))
         elif kb.is_pressed(ks): 
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.MI2, 0.3))
         elif kb.is_pressed(ks):
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.FA2, 0.3))
         elif kb.is_pressed(ks): 
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.SOL2, 0.3))


   # ========================
   #  MUSIC NOTES BY KEYNUMS
   # ========================

   def _init_note_nums(status):
      """Status ON: True, status OFF: False"""

      st = (status)

      OFF = False
      ON = True

      if st == OFF:
         exit()

      elif st == ON:

         synthesizer = Synthesizer

         if kb.is_pressed(keynum): # if a key is pressed it´ll play a music note
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.DO2, 0.3))
         elif kb.is_pressed(keynum):
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.RE2, 0.3))
         elif kb.is_pressed(keynum): 
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.MI2, 0.3))
         elif kb.is_pressed(keynum):
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.FA2, 0.3))
         elif kb.is_pressed(keynum): 
            musnotes.player.play_wave(Synthesizer.generate_constant_wave(synthesizer, musnotes.SOL2, 0.3))
      


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



# ========================
# DEF KEYBOARD KEYS EVENTS 
# ========================




class Keys:

   def holdkey(firstkey, secondkey):
   
      """KEYS ALLOWED: ALT, ALTGR, FN, CMD & SHIFT """

      fkey = (firstkey)
      skey = (secondkey)

      # Windows key: CTRL + ESC

      if fkey == "alt":
         pyt.keyDown("ALT")
         pyt.keyDown(skey)
      
      elif fkey == "altgr":
         pyt.keyDown("altgr")
         pyt.keyDown(skey)
      
      elif fkey == "cmd":
         pyt.keyDown("cmd")
         pyt.keyDown(skey)

   def prskey(Key):

      """Keyboard numbers & words"""

      frstkey = (Key)
      pyt.press(frstkey)