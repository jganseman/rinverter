# Rhythm Inverter
# For Rhythm and Music Hackathon @ Spotify
# (c) Joachim Ganseman, 20 June 2015

# Usage: python ./rinverter.py FILENAME
import sys
import os
from music21 import *

for arg in sys.argv:
	print arg

sfilename = sys.argv[1]

# TODO : check if file exists
if (os.path.exists(sfilename)):
	sfile = sfilename
else:
	raise ValueError('File does not exist!')

# Read a file into music21
sfile = converter.parse(sfile)

# Get a list of all measures of this file and all notes in the measure

for curPart in sfile.getElementsByClass('Part'):
	for curMeasure in curPart.getElementsByClass('Measure'):
		# Get the notes, rests and chords
		mLength = curMeasure.duration.quarterLength
		curNotes = curMeasure.flat.getElementsByClass('GeneralNote')
			# Flattening merges all the separate voices ...
			# TODO figure out whether it is necessary
		listdurs = []
		for note in curNotes:
			listdurs.append( note.duration.quarterLength )
		print listdurs
		if not listdurs : continue	# Deal with empty measures

		# avgdur = sum(listdurs)/len(listdurs)
		reciproc = [ 1/x for x in listdurs if x>0 ]
			# The IF-statement necessary to handle grace notes
		
		# note: this is leftover from a previous try, manipulating harmonic means
			#print reciproc
			#avgrecip = sum(reciproc)/len(reciproc)
			#print avgrecip
			#fliprecip = [ 2*avgrecip-x for x in reciproc ]
			#print fliprecip
			#avgflip = sum(fliprecip)/len(fliprecip)
			#print avgflip
			#newdurs = [ 1/x for x in fliprecip if x>0 ]
			#print newdurs
		
		# re-fit the new durations into the measure's time
		# note: working directly on the reciprocals of quarternote values tends to give better results than working on harmonic means
		ratio = sum(reciproc) / mLength
		finaldurs = [ 1/ratio*x for x in reciproc ]
		print finaldurs
	
		print ('---') # end of measure

		# Assign the new note durations
		i=0
		for note in curNotes:
			if note.duration.quarterLength > 0:
				note.duration.quarterLength = finaldurs[i]
				i=i+1
		
# Finally: print score using your favourite editor
sfile.show()

		



