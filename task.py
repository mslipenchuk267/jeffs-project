from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random

# Path to working directory
directory = os.getcwd()

# Timings
itiDuration = 1
decisionDuration = 5
tryFasterDuration = 1
thankYouScreenDuration = 1.5

# Trial data initlization
numTrials = 10
trialType = [''] * len(numTrials) # 1 denotes money and machine selection game
                                  # 2 denotes machine and machine selection game
moneyTypes = [5,10,50]

# Data Logging
key = ['']
responses = [''] * len(numTrials)

# Get subjID
subjDlg = gui.Dlg(title="JOCN paper - rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id) < 1: # Make sure participant entered name
    core.quit()

# Initialzing Window
win = visual.Window(fullscr=True, size=[1200, 800], units='pix', monitor='testMonitor', color = [-.9,-.9,-.9])

# Initalize Text Stim
instruction_screen = visual.TextStim(win, text="""To select the option presented on the left press ‘f’.\n
                                            To select the option presented on the right press ‘g’.\n
                                            You will have 6 seconds to make your choice.\n\n
                                            Press any key to start""")
thank_you_screen = visual.TextStim(win, text="""Thank you for playing!""")
try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
iti = visual.TextStim(win, text="""*""")
moneyOptionChoice = visual.TextStim(win, text=moneyOptions[0])
moneyOptionLeftMachine = visual.TextStim(win, text=moneyOptions[0])
moneyOptionRightMachine = visual.TextStim(win, text=moneyOptions[0])

# Populate imageList with slot machine images
imageList = [os.path.join(directory, image) for image in
                 glob.glob('images/*.jpg')]

# Initalize Image Stim
leftMachine = visual.ImageStim(win=win, image=image[0], units='pix', pos=[0, 200], size = [300,300])
rightMachine = visual.ImageStim(win=win, image=image[0], units='pix', pos=[0, 200], size = [300,300])

# Show instruction screen
event.clearEvents()
instruction_screen.draw()
win.flip()

# Lets participant quit at any time by pressing escape button
if 'escape' in event.waitKeys():
    core.quit()

# Main Loop
for i in range(0, numTrials):
    event.clearEvents() # If participant presses key(s) during iti
    timer.reset()
    while timer.getTime() < decisionDuration:
        if trialType[i] == 1:
            moneyOptionChoice.draw()
            moneyOptionRightMachine.draw()
            rightMachine.draw()
        else:
            moneyOptionLeftMachine.draw()
            leftMachine.draw()
            moneyOptionRightMachine.draw()
            rightMachine.draw()

        key = event.waitKeys()
        if key[0] in ['f','g']:
            responses[i] = key[0]
            break # Ends trial before specified decisionDuration
        if 'escape' in event.waitKeys(): # Allows subject to leave game
            core.quit()

    if responses[i] = '':
        responses[i] = 'n/a'
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)

    iti.draw()
    win.flip()
    core.wait(itiDuration)  # brief pause, slightly smoother for the subject

# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' results.csv','w')
for i in range(0, numTrials):
    f.write(trialType[i] + ',' + responses[i] + "\n")
f.close()

# Thank participant
thank_you_screen.draw()
win.flip()
core.wait(thankYouScreenDuration)
