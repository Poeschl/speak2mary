import unittest
import wave
from io import BytesIO

from speak2mary import MaryTTS


class TestMaryTTS(unittest.TestCase):

    def test_speak(self):
        mary = MaryTTS()

        audio = mary.speak("Hello World")
        waves = wave.open(BytesIO(audio))

        self.assertEqual(waves.getnchannels(), 1)
        self.assertEqual(waves.getframerate(), 48000)
        self.assertGreater(waves.getnframes(), 10000)

    def test_speak_with_effects(self):
        mary = MaryTTS()

        audio = mary.speak("Hello World", {"volume": "amount:2.0;", "robot": "amount:100.0;"})
        waves = wave.open(BytesIO(audio))

        self.assertEqual(waves.getnchannels(), 1)
        self.assertEqual(waves.getframerate(), 48000)
        self.assertGreater(waves.getnframes(), 10000)

    def test_speak_as_emotionalxml(self):
        mary = MaryTTS(input_type="EMOTIONML")

        xml = """
        <emotionml version="1.0" xmlns="http://www.w3.org/2009/10/emotionml" 
        category-set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories">        
            <emotion><category name="angry"/>
                Hello World
            </emotion>
        </emotionml>
        """

        audio = mary.speak(xml)
        waves = wave.open(BytesIO(audio))

        self.assertEqual(waves.getnchannels(), 1)
        self.assertEqual(waves.getframerate(), 48000)
        self.assertGreater(waves.getnframes(), 10000)
        # Make sure only "Hello World" is in the output, not the whole xml
        self.assertLess(len(audio), 200000)
