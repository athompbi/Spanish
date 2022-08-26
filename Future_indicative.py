from Unicode_letters import *

### Future indicative

class Future():
    def __init__(self, verb):
        self._verb = verb

    """
    yo -'e
    tu -'as
    usted/el/ella -'a
    nosotros -emos
    vosotros -'eis
    ustedes/ellos/ellas -'an
    """

    def get_yo(self):
        self._verb += e_accent
        return self._verb

    def get_tu(self):
        self._verb += a_accent + 's'
        return self._verb

    def get_el(self):
        self._verb += a_accent
        return self._verb

    def get_nos(self):
        self._verb += 'emos'
        return self._verb

    def get_vos(self):
        self._verb += e_accent + 'is'
        return self._verb

    def get_ellos(self):
        self._verb += a_accent + 'n'
        return self._verb

