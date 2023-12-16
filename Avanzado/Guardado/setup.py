from distutils.core import setup
import py2exe
import os
from time import sleep
from random import randrange
import sqlite3
from pathlib import Path
import re
import glob


setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      console=["Horror_Script.py"])