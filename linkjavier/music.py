#!/usr/bin/env python3
""" Testing Vanilla Model for Music Generation """

#library for understanding music
from music21 import *

#for listing down the file names
import os

import numpy as np


#defining function to read MIDI files
def read_midi(file):
    
    print("Loading Music File:",file)
    
    notes=[]
    notes_to_parse = None
    
    #parsing a midi file
    midi = converter.parse(file)
  
    #grouping based on different instruments
    s2 = instrument.partitionByInstrument(midi)

    #Looping over all the instruments
    for part in s2.parts:
    
        #select elements of only piano
        if 'Piano' in str(part): 
        
            notes_to_parse = part.recurse() 
      
            #finding whether a particular element is note or a chord
            for element in notes_to_parse:
                
                #note
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                
                #chord
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)


# Specify the path to midi files
path='Schubert/'

# Read all the filenames
files=[i for i in os.listdir(path) if i.endswith(".mid")]

# Reading each midi file info
notes_array = np.array([read_midi(path+i) for i in files])