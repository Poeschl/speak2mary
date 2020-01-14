"""Speak2Mary"""
import http.client as http
import logging
from urllib.parse import urlencode

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 59125
DEFAULT_INPUT_TYPE = "TEXT"
DEFAULT_OUTPUT_TYPE = "AUDIO"
DEFAULT_CODEC = "WAVE"
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
            logging.error(response.getheaders())
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
