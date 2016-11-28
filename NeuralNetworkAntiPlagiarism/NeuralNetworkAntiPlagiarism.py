# -*- coding: utf-8 -*-
import sys
from nltk.tokenize import sent_tokenize
from Atomizer import Atomizer

atomizer = Atomizer("dataSets/part1/suspicious-document00005");

list = atomizer.GetFullyPlagiarizedFragments()
for sent in list:
    print(str(sent).encode(sys.stdout.encoding, errors='replace'))
    print("\n\n\n")
    pass




