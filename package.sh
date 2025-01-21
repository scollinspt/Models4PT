#!/bin/bash

# Make a ZIP package containing
# the current version of the Models4PT GUI
# and store it in a file called Models4PT.zip

( cd jslib/ ; make )
( cd gui ; zip -r ../Models4PT.zip * )

