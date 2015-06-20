# rinverter
Rhythm Inverter
(c) Joachim Ganseman

Little project done at the Monthly Music Hackathon in NYC, 20 June 2015 @ Spotify HQ

Goal: Invert the rhythm of every measure in a given score. Just run the script with the score file as input!

Used Software: 
* Python 2.7.9
* music21 2.0.5
* MuseScore 1.3

How it works: 
* For every measure in every part of the score, the durations of every note, chord and rest are collected. 
* Every duration, expressed in quarter notes, is inverted (such that a duration ratio of 1:2 becomes 2:1, 1:3 becomes 3:1, ...).
* The result is scaled back to the original measure's duration, so the duration ratio between the notes remains the same.
* Grace notes (with duration 0) are ignored.

Bugs / Features:
* The script can't deal with separate voices within a single measure very well. Depending on how the score was encoded, this may be an important issue. Currently, all voices within a measure are merged.
* Some more exotic staff notations also cause trouble, like cross-staff beams.
* Given the uncommon duration values in which this results, notation editors have it difficult to quantize the new rhythms. Expect some very eccentric tuplets :)

