import logging
import unittest
import wave
from io import BytesIO

from marytts import MaryTTS


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
