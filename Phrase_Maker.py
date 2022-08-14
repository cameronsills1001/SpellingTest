__author__ = 'cameron'

from gtts import gTTS

class Phrase_Maker:



    def make_phrase(self, phrase, title):
        """ Using gTTS to create an mp3 from a given string"""
        self.phrase = phrase
        self.title = title
        tts = gTTS(text = phrase, lang = 'en')
        #title needs to include a path as well as a file name
        # i.e. /home/new_sounds/sound_name.mp3
        tts.save("%s.mp3" % title)

    def __init__(self):
        """When an instance of the class is created the fixed phrases
        (the phrases that should not change) are created. It will recreate them each time
        it is run but that should eliminate any problems with corrupt or missing
        sound files"""
        greeting = "My name is Pearl. I'm going to help you with your spelling homework."
        next_word = "Your next word is."
        correct = "That is correct!"
        incorrect = "I'm sorry, that is incorrect."
        self.make_phrase(greeting, "fixed_phrases/greeting")
        self.make_phrase(next_word, "fixed_phrases/next_word")
        self.make_phrase(correct, "fixed_phrases/correct")
        self.make_phrase(incorrect, "fixed_phrases/incorrect")



