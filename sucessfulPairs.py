import bisect
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        pairs = []

        for spell in spells:
            threshold = (success + spell -1) // spell # ciel(success/spell)
            index = bisect.bisect_left(potions, threshold)
            pairs.append(m-index)
        
        return pairs
