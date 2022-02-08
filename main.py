import pytrec_eval
import json
import numpy as np
import time
import pickle
from nltk.corpus import wordnet
##import nltk
##nltk.download('wordnet')
wordnet.all_synsets()
import evaluate
# for pytrec_eval
def DictonaryGeneration(topCorrections, Misspelleds, Corrects):
    Correction = {}
    for c in range(len(Misspelleds)):
        Correction[Misspelleds[c]] = {}
        comm = topCorrections[c]
        for n in range(len(comm)):
            Correction[Misspelleds[c]][comm[n]] = 1
    Truth = {}
    for c in range(len(Corrects)):
        Truth[Misspelleds[c]] = {}
        Truth[Misspelleds[c]][Corrects[c]] = 1
    return  Correction, Truth


def MED_DP(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+1,   # Insert
                                   dp[i-1][j]+1,   # Remove
                                   dp[i-1][j-1]+2) # Replace

    return dp[m][n]
## Dataset preprocess
dataset = [i.strip() for i in open("missp.dat").readlines()]
correct = []
misspelled = []

for w in dataset:
    if w[0]=='$':
        previous_word = w[1:]
    else:
        correct.append(previous_word.lower())
        misspelled.append(w.lower())
dictionary = []
for i in wordnet.all_synsets():
    dictionary.append(i.name().split('.')[0])
Dictionary = np.asarray(dictionary)
Dictionary = np.unique(Dictionary)


K=5
TOPS = []

for mcidx,msw in enumerate(misspelled):
    tic = time.time()
##    if mcidx == limit:
##        break
    distances = []
    beg = time.time()
    for cidx, c in enumerate(Dictionary):
##        if cidx%40000==0:
##            print(ms, c, cidx, time.time()-beg)
            #MED(ms,c,len(ms),len(c))
        distances.append(MED_DP(msw,c,len(msw),len(c)))
    distances = np.asarray(distances)
##    idx = distances.argsort()
    idx = distances.argpartition(range(K))[:K]
    Tops = Dictionary[np.array(idx)]
    TOPS.append(Tops)
    print(f'Most similar words to {msw}: {Tops}')
    print(f'Most similar edits: {distances[np.array(idx[:K])]}')
q, run = DictonaryGeneration(TOPS, misspelled, correct)
with open(f'corrections_at_k10.pkl', 'wb') as f:
    pickle.dump(q, f)
with open(f'golden_standard_at_k10.pkl', 'wb') as f:
    pickle.dump(run, f)

with open('corrections_at_k10.pkl', 'rb') as f:
    q = pickle.load(f)
with open('golden_standard_at_k10.pkl', 'rb') as f:
    run = pickle.load(f)
print(evaluate.eval('success_1', 'success_5', 'success_10'))


