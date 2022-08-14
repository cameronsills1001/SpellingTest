#just using this as a test file for each class that I make.

from Phrase_Maker import *
from Player import *
from Read_Write import *

phrase = Phrase_Maker()
player = Player()
scribe = Read_Write()

points = scribe.get_points()

print("You have %s points." % points)

