import string
from itertools import combinations_with_replacement 
from itertools import permutations 
class PassGenerator:
    def __init__(self, pattern):
        self.pattern = pattern
    def get_all(self, length):
        ret = set()
        for pass_version in combinations_with_replacement(self.pattern, length):
            new_string = ''.join(pass_version)
            all_passwords = set(permutations(new_string))
            for item in all_passwords:
                ret.add(''.join(item))

        return ret; 
    