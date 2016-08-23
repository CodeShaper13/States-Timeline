################################################################################
## I don't think this works, but at least it has all the files names in it... ##
################################################################################

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32': base = 'Win32GUI'
#if sys.platform == 'win64': base = 'Win64GU'

opts={'include_files':['icon.png',
                       'music.mp3',
                       'delaware.png',
                       'pennsylvania.png',
                       'newJersey.png',
                       'georgia.png',
                       'connecticut.png',
                       'massachusetts.png',
                       'maryland.png',
                       'southCarolina.png',
                       'newHampshire.png',
                       'virginia.png',
                       'newYork.png',
                       'northCarolina.png',
                       'rhodeIsland.png',
                       'vermont.png',
                       'kentucky.png',
                       'tennessee.png',
                       'ohio.png',
                       'louisiana.png',
                       'indiana.png',
                       'mississippi.png',
                       'illinois.png',
                       'alabama.png',
                       'maine.png',
                       'missouri.png',
                       'arkansas.png',
                       'michigan.png',
                       'florida.png',
                       'texas.png',
                       'iowa.png',
                       'wisconsin.png',
                       'california.png',
                       'minnesota.png',
                       'oregon.png',
                       'kansas.png',
                       'westVirginia.png',
                       'nevada.png',
                       'nebraska.png',
                       'colorado.png',
                       'northDakota.png',
                       'southDakota.png',
                       'montana.png',
                       'washington.png',
                       'idaho.png',
                       'wyoming.png',
                       'utah.png',
                       'oklahoma.png',
                       'newMexico.png',
                       'arizona.png',
                       'alaska.png',
                       'hawaii.png',], 'includes':['re']}

setup( name = 'States Timeline',
       version = '1.0',
       description = 'Testing',
       author = 'PJ',
       options = {'build_exe':opts},
       executables = [Executable('main.py',base = base)])
