# UniGram

import re
import math

class Tokenizer:
    def __init__(self, word2freq):
        self.totalfreq = sum(list(word2freq.values()))
        self.word2freq = {} # Trie Tree
        for word, freq in word2freq.items():
            self.word2freq[word] = freq
            for idx in range(len(word)):
                sub_word = word[:idx + 1]
                if sub_word not in self.word2freq:
                    self.word2freq[sub_word] = 0 # Path Compression, sacrifice space for insertion time

        self.re_eng = re.compile('[a-zA-Z0-9]', re.U)

    def get_graph(self, sentence):
        graph = {} # Directed Acyclic Graph
        for start_idx in range(len(sentence)):
            end_idx_list = []
            for end_idx in range(start_idx, len(sentence)):
                token = sentence[start_idx: end_idx + 1] if end_idx > start_idx else sentence[end_idx]
                if  token not in self.word2freq:
                    break
                if  self.word2freq.get (token) > 0:
                    end_idx_list.append(end_idx)
            graph[start_idx] = end_idx_list if end_idx_list else [start_idx]
        return graph

    def get_route(self, sentence, graph):
        route = {} # Dynamic Programming
        route[len(sentence)] = (0, 0) # (end_idx, score)
        for start_idx in range(len(sentence) -1, -1, -1):
            end_idx_scores = []
            for end_idx in graph[start_idx]:
                word = sentence [start_idx: end_idx + 1]
                freq = self.word2freq.get(word, 1)
                end_idx_score = route[end_idx + 1][1] + (math.log(freq) - math.log(self.totalfreq))
                end_idx_scores.append((end_idx, end_idx_score))
            route[start_idx] = max(end_idx_scores, key = lambda item: item[1])
        return route

    def tokenize(self, sentence):
        graph = self.get_graph(sentence)
        route = self.get_route(sentence, graph)
        tokens = []
        buffer = ''
        start_idx = 0
        seq_len = len(sentence)
        while start_idx < seq_len:
            end_idx = route[start_idx][0] + 1
            word = sentence[start_idx:end_idx]
            if (
                self.re_eng.match(word) and
                len(word) == 1
            ):
                buffer += word
                start_idx = end_idx
            else:
                if  buffer:
                    tokens.append(buffer)
                    buffer = ''
                tokens.append(word)
                start_idx = end_idx
        if  buffer:
            tokens.append(buffer)
        return tokens
