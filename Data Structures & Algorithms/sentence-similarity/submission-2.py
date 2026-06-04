class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        # if len(sentence1) == len(sentence2) and 
        # for i of range(len(sentence1)):
        # sentence1[i] and sentence[i] are in similarPairs[i]


        if len(sentence1) == len(sentence2):
            pairs = set(tuple(p) for p in similarPairs)

            for i in range(len(sentence1)):
                w1 = sentence1[i]
                w2 = sentence2[i]

                if w1 != w2 and (w1,w2) not in pairs and (w2,w1) not in pairs:
                    return False
            return True
        return False
