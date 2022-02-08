# MED Performance for Auto-spell Correction

**Introduction:**

In this assignment, we use Minimum Edit Distance to calculate the distance between a misspelled word and its correct form. we use [WordNet](https://en.wikipedia.org/wiki/WordNet#Database_contents) as a dictionary. This database contain 155,327 divided in 175,979 synsets for 207,016 word-sense pair. It is divided into 4 categories nouns, verbs, adjectives, and adverbs. The [birkbeck](https://www.dcs.bbk.ac.uk/~roger/corpora.html) is used as a misspelled corpus. This corpus contains 36,133 misspellings of 6,136 words. It includes the results of spelling tests and errors from free writing, mostly taken from schoolchildren, university students, or adult literacy students.

In this experiment we use The Levenshtein distance. For example, given two string 𝑠1 and 𝑠2 we want to find the numbers of edits/operations (e.g., insert, remove, replace) required to convert 𝑠1 to 𝑠2. we use Birkbeck spelling error corpus.

**Inputs:**

[birkbeck](https://www.dcs.bbk.ac.uk/~roger/corpora.html)

[Wordnet for python](https://pypi.org/project/PyDictionary/)

**Output**

Below table shows the real samples from the Birkbeck corpus and top-5 for a word from WordNet dictionary. 

![image](https://user-images.githubusercontent.com/75437827/152948419-fed87de4-981a-41a0-8cda-8a9a7c79fd72.png)

**Evaluations:**

Below table shows the average of s@1, s@5, s@10.

![image](https://user-images.githubusercontent.com/75437827/152949015-6b8648d4-5edb-413f-95c9-5f12883cc391.png)

