class Allergies:

    # returns a list of the binary components in any given number 
    # ie. bin(22) = 10110 and bits(22) returns [2, 4, 16]
    def bits(self, n):
        bin_rep = []
        # keep only last 8 bits (128 and below)
        n = n & 255
        while n:
            b = n & (~n + 1)
            bin_rep.append(b)
            n = n ^ b
        return bin_rep

    def __init__(self, score):
        allergy_values = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}
        # store the binary components of the given score 
        self.values = self.bits(score)
        # using allergy_values, store a list of the allergies corresponding to the binary components 
        self._allergies = list(map(allergy_values.get, self.values))


    def allergic_to(self, item):
        return item in self._allergies

    @property
    def lst(self):
        return self._allergies
