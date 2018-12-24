import logging

class Geomodel():
    _logger: logging
    def __init__(self):
        self._logger = logging.getLogger('org.allnix')

    def do_something(self):
        print(__name__)
        self._logger.info('do_something')
