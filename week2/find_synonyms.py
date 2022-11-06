import fasttext

mpdel = fasttext.train

f = open('/workspace/datasets/fasttext/top_words.txt', 'r')
model = fasttext.load_model('/workspace/datasets/fasttext/title_model_25.bin')

results = []
with open('/workspace/datasets/fasttext/top_words.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        neigh = model.get_nearest_neighbors(line)
        results.append([line]+[word for dist, word in neigh if  dist >= 0.75])


with open('/workspace/datasets/fasttext/synonyms.csv', 'w') as f:
    for words in results:
        f.write(','.join(words) + '\n')

