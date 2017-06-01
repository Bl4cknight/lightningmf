Lightning MAME Frontend
=======================

This program is a MAME Qt frontend designed for Linux. It was created to be easy to use, be very fast and focus on the essential features.
Tested with MAME 0.154 and 0.179

## Prerequisites:

    sudo apt-get install mame mame-tools


## RUN:
Standalone version tested on ubuntu 16.04 (GLIBC >= 2.23):
Created with cx-Freeze 4.3.3 and megastep-makeself. Needs qt4 libs installed on system.

    sudo chmod 755 lightningmf.run
    ./lightningmf.run

Unfrozen version:

    pip install -r requirements.txt
    ./lightningmf

## Save time installing pyside from wheels:

    (x64) pip install wheelhouse/PySide-1.2.4-cp27-cp27mu-linux_x86_64.whl
    (i686)pip install wheelhouse/PySide-1.2.4-cp27-cp27mu-linux_i686.whl

## PySide building system requirements:

    sudo apt-get install python-dev cmake qt4-qmake build-essential
    sudo apt-get install libqtcore4 libqt4-dev libqtgui4 qt4-dev-tools

## Changelog:
- 1.1.5 Final
  - fix snapshot progressbar
  - add mamedb as images source
  - new logo
- 1.1.4 First Release
  - Multiarch standalone version
  - Added requirements.txt
  - removed menu bar
- 1.1.3
  - Roms sorting
  - Improved table layout
  - Added Ctrl+C KeyEvent
- 1.1.2
  - Changed snapshots source
  - now compatible with mame 0.179
- 1.1.1
  - Fix progress bar display issue
  - set user home as starting dir for config folders selection dialog.
- 1.1.0
  - Main window is shown maximized and progressbar widgets are now centered.
- 1.0.9
  - Created all-in-one executable lightningmf.run using cx_freeze4.3.3 and megastep makeself.
- 1.0.8
  - Key press events added to manage rom launch (enter) and application quit (escape)
- 1.0.7
  - Download snapshots from mamedb
- 1.0.6
  - Fixed Segmentaton Fault on close
  - ProgressBar on roms loading/updating
  - Code Refactoring
- 1.0.5:
  - Improved rom loading/updating (processing only new added/removed roms)
- 1.0.4:
  - Resolved bottleneck on roms data loading
  - A box dialog is shown during roms loading
  - When a rom entry is selected the application shows a random snapshot taken from rom snapshots folder if exists.

