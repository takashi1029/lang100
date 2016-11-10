import re
from collections import Counter

sentence = []
content = []



def sentence_to_dict(elements):
    sent_dict = {}
    sent_dict["surface"] = elements[0]
    sent_dict["base"] = elements[-3]
    sent_dict["pos"] = elements[1]
    sent_dict["pos1"] = elements[2]
    return sent_dict


with open("neco.txt.mecab", "r") as f:
    for line in f:
        elements = re.split(r"\s|\,", line)
        if elements[0] != "EOS":
            sent_dict = sentence_to_dict(elements)
            sentence.append(sent_dict)
        else:
            content.append(sentence)
            sentence = []

vocab = []
for cont in content:
    for sent in cont:
        vocab.append(sent["base"])

count = Counter(vocab)

for (word,cnt) in count.most_common(10):
    print word,cnt

