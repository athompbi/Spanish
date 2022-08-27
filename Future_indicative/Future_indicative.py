from Unicode_letters import *

class Future():
    """Conjugating the given verb to the future indicative tense."""

    def __init__(self, verb):
        self._verb = verb

    def get_yo(self):
        """Adds an accented e to the end of the given verb to 
        conjugate the verb to the future tense for the yo pronoun.

        Return:
            self._verb = conjugated verb"""

        self._verb += e_accent
        return self._verb

    def get_tu(self):
        """Adds an accented a and 's' to the end of the given verb to 
        conjugate the verb to the future tense for the tu pronoun.
        
        Return:
            self._verb = conjugated verb"""

        self._verb += a_accent + 's'
        return self._verb

    def get_el(self):
        """Adds an accented a to the end of the given verb to conjugate 
        the verb to the future tense for the el/ella/usted pronouns.
        
        Return:
            self._verb = conjugated verb"""

        self._verb += a_accent
        return self._verb

    def get_nos(self):
        """Adds 'emos' to the end of the given verb to conjugate the 
        verb to the future tense for the nosotros pronoun.
        
        Return:
            self._verb = conjugated verb"""

        self._verb += 'emos'
        return self._verb

    def get_vos(self):
        """Adds an accented e and 'is' to the end of the given verb to 
        conjugate the verb to the future tense for the vosotros pronoun.
        
        Return:
            self._verb = conjugated verb"""

        self._verb += e_accent + 'is'
        return self._verb

    def get_ellos(self):
        """Adds an accented a and 'n' to the end of the given verb to 
        conjugate the verb to the future tense for the ellos/ellas/ustedes pronouns.
        
        Return:
            self._verb = conjugated verb"""

        self._verb += a_accent + 'n'
        return self._verb
