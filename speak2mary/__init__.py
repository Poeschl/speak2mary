"""Speak2Mary"""
import http.client as http
from urllib.parse import urlencode

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 59125
DEFAULT_INPUT_TYPE = "TEXT"
DEFAULT_OUTPUT_TYPE = "AUDIO"
DEFAULT_CODEC = "WAVE_FILE"
DEFAULT_LOCALE = "en_US"
DEFAULT_VOICE = "cmu-slt-hsmm"


class MaryTTS(object):

    def __init__(self,
                 host=DEFAULT_HOST,
                 port=DEFAULT_PORT,
                 codec=DEFAULT_CODEC,
                 locale=DEFAULT_LOCALE,
                 voice=DEFAULT_VOICE):

        self._host = host
        self._port = port
        self._codec = codec
        self._locale = locale
        self._voice = voice

    def speak(self, message, effects=None):
        if effects is None:
            effects = {}

        raw_params = {
            "INPUT_TEXT": message.encode('UTF8'),
            "INPUT_TYPE": DEFAULT_INPUT_TYPE,
            "OUTPUT_TYPE": DEFAULT_OUTPUT_TYPE,
            "LOCALE": self._locale,
            "AUDIO": self._codec,
            "VOICE": self._voice,
        }

        for effect, parameter in effects.items():
            raw_params["effect_%s_selected" % effect] = "on"
            raw_params["effect_%s_parameters" % effect] = parameter

        conn = http.HTTPConnection(self._host, self._port)

        conn.request("POST", "/process", urlencode(raw_params))
        response = conn.getresponse()

        if response.status != 200:
            raise Exception("{0} - {1}: '{2}''".format(response.status, response.reason, response.readline()))
        return response.read()

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def locale(self):
        return self._locale

    @property
    def voice(self):
        return self._voice

    @property
    def codec(self):
        return self._codec

    @staticmethod
    def supported_codecs():
        return ["WAVE_FILE", "AU_FILE", "AIFF_FILE"]

    @staticmethod
    def supported_effects():
        """Returns a dict of available effects and the default arguments"""
        return {
            "Volume": "amount:2.0;",
            "TractScaler": "amount:1.5;",
            "F0Scale": "f0Scale:2.0;",
            "F0Add": "f0Add:50.0;",
            "Rate": "durScale:1.5;",
            "Robot": "amount:100.0;",
            "Whisper": "amount:100.0;",
            "Stadium": "amount:100.0",
            "Chorus": "delay1:466;amp1:0.54;delay2:600;amp2:-0.10;delay3:250;amp3:0.30",
            "FIRFilter": "type:3;fc1:500.0;fc2:2000.0",
            "JetPilot": ""
        }
