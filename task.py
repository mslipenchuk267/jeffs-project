from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random

# Path to working directory
numTrials = 10;
itiDuration = 1;
decisionDuration = 5;
trialType = [''] * len(numTrials)
# Logging Data
key = ['']
responses = [''] * len(numTrials)


directory = os.getcwd()

# Get subjID
subjDlg=gui.Dlg(title="JOCN paper- rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id)<1: # Make sure participant entered name
    core.quit()

# Initialzing Window, insruction text, and thank you screen text, and money option text;
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor', color = [-.9,-.9,-.9])
instruction_screen = visual.TextStim(win, text="""To select the option presented on the left press ‘f’.\n
                                            To select the option presented on the right press ‘g’.\n
                                            You will have 6 seconds to make your choice.\n
                                            \n Press any key to start""")
thank_you_screen = visual.TextStim(win, text="""Thank you for choosing!""")
moneyOption = visual.TextStim(win, text=moneyOptions[0])
moneyOption = visual.TextStim(win, text=moneyOptions[0])

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
leftMachine = visual.ImageStim(win=win, image=image, units='pix', pos=[0, 200], size = [300,300])
rightMachine = visual.ImageStim(win=win, image=image, units='pix', pos=[0, 200], size = [300,300])

# Main Loop
for i in range(0, numTrials):
    # The size parameter rescales images.
    # Stretch can be mitigated by cropping images to a resolution that would scale to the specified one bellow.
    
    event.clearEvents()
    timer.reset()
    while key[0] not in ['escape', 'esc'] and timer.getTime() < decisionDuration:
        if trialType[i] == 1:
            
        key = event.waitKeys()
        if event.getKeys(['escape']):
            core.quit()

    # assigns response to corresponding image
    responses[imageList.index(image)] = ratingScale.getRating()
    familiarity[imageList.index(image)] = familiarityScale.getRating()
    
    win.flip()
    core.wait(itiDuration)  # brief pause, slightly smoother for the subject



# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' task a results.csv','w')
for i in range(0,len(imageList)):
    # Remove filepath from imageList[i] string
    picName = os.path.relpath(imageList[i], '..\..\JOCN\task a\images\\') #..\..\JOCN\task a\images\
    f.write(picName +','+ratings[i]+','+familiarity[i]+"\n")
f.close()

# Thank participant
thank_you_screen.draw()
win.flip()
core.wait(1.5)
