from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random

# Path to working directory
numTrials = 10
itiDuration = 1
decisionDuration = 5
tryFasterDuration = 1
trialType = [''] * len(numTrials) # 1 denotes money and machine selection game
                                  # 2 denotes 2 machine selection game
# Logging Data
key = ['']
responses = [''] * len(numTrials)


directory = os.getcwd()

# Get subjID
subjDlg = gui.Dlg(title="JOCN paper - rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id) < 1: # Make sure participant entered name
    core.quit()

# Initialzing Window, insruction text, and thank you screen text, and money option text;
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor', color = [-.9,-.9,-.9])
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

# Show instruction screen
event.clearEvents()
instruction_screen.draw()
win.flip()

# Lets participant quit at any time by pressing escape button
if 'escape' in event.waitKeys():
    core.quit()

# Initialize image list
imageList = [os.path.join(directory, image) for image in
                 glob.glob('images/*.jpg')]

# Randomize order of images
leftMachine = visual.ImageStim(win=win, image=image[0], units='pix', pos=[0, 200], size = [300,300])
rightMachine = visual.ImageStim(win=win, image=image[0], units='pix', pos=[0, 200], size = [300,300])

# Main Loop
for i in range(0, numTrials):
    # The size parameter rescales images.
    # Stretch can be mitigated by cropping images to a resolution that would
    # scale to the specified one bellow.

    event.clearEvents()
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
        if 'escape' in event.waitKeys():
            core.quit()

    if responses[i] = '':
        responses[i] = 'n/a'
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)
        continue

    iti.draw()
    win.flip()
    core.wait(itiDuration)  # brief pause, slightly smoother for the subject



# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' task a results.csv','w')
for i in range(0, numTrials):
    f.write(trialType[i] + ',' + responses[i] + "\n")
f.close()

# Thank participant
thank_you_screen.draw()
win.flip()
core.wait(1.5)
