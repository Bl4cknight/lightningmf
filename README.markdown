Lightning MAME Frontend
=======================

This program is a MAME frontend designed for Linux. It was created to be easy to use, be very fast and focus on the essential features.

[See the website for info about it.](http://lightningmf.neoname.eu)

###To launch:

From the program folder, type:

    python lightningmf

###Changelog:
- 1.0.5:
  - Improved rom loading updating only new added/removed roms
  - Fixed Segmentaton Fault on close
- 1.0.4:
  - Resolved bottleneck on roms data loading
  - A box dialog is shown during roms loading
  - When a rom entry is selected the application shows a random snapshot taken from rom snapshots folder if exists.
- 1.0.3:
  - corrected crash under ubuntu
  - changed the installation method to pip
- 1.0.2:
  - corrected error message when closing the application
- 1.0.1:
  - now only displays owned roms
  - fixed memory leak during rom charging
  - displays the number of roms
