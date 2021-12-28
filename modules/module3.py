# HMM

import re

class Tokenizer:
    def __init__(self, start_prob, trans_prob, emit_prob):

        self.start_prob = start_prob
        self.trans_prob = trans_prob
        self.emit_prob  = emit_prob

        # B: Begin, M: Middle, E: End, S: Single
        self.all_state = ['B', 'M', 'E', 'S']
        # Optimization for Chinese
        self.end_state = ['E', 'S']
        self.pre_state = {
            'B': 'ES',
            'M': 'MB',
            'E': 'BM',
            'S': 'SE'
        }

        self.re_zhcn = re.compile('([\u4E00-\u9FD5]+)')
        self.re_skip = re.compile('([a-zA-Z0-9]+(?:\.\d+)?%?)')

    def viterbi(self, sentence):
        MIN_NUMBER = -3.14e100
        DP = [{} for _ in range(len(sentence))] # Dynamic Programming
        # init
        index = 0
        token = sentence[index]
        hist_path = {}
        for state in self.all_state:
            DP[index][state] = self.start_prob[state] + self.emit_prob[state].get(token, MIN_NUMBER)
            hist_path[state] = [state]
        # loop
        for index in range( 1, len(sentence) ):
            token = sentence[index]
            curr_path = {}
            for state in self.all_state:
                prob, pre_state = max([(
                    DP[index - 1][pre_state] + \
                    self.trans_prob[pre_state].get(state, MIN_NUMBER) + \
                    self.emit_prob [state].get(token, MIN_NUMBER),
                    pre_state
                ) for pre_state in self.pre_state[state]])
                DP[index][state] = prob
                curr_path[state] = hist_path[pre_state] + [state]
            hist_path = curr_path
        prob, state = max((DP[len(sentence) - 1][state], state) for state in self.end_state)
        return hist_path[state]

    def tokenize_block(self, sentence):
        tokens = []
        states = self.viterbi(sentence)
        start_idx, end_idx = 0, 0
        for idx in range(len(sentence)):
            state = states[idx]
            if state not in self.all_state:
                assert ValueError()
            elif state == 'B':
                start_idx = idx
            elif state == 'E':
                end_idx = idx + 1
                tokens.append(sentence[start_idx: end_idx])
            elif state == 'S':
                end_idx = idx + 1
                tokens.append(sentence[end_idx - 1])
        if  end_idx < len(sentence):
            tokens.append(sentence[end_idx:])
        return tokens

    def tokenize(self, sentence):
        tokens = []
        blocks = self.re_zhcn.split(sentence)
        for block in blocks:
            if self.re_zhcn.match(block):
                for token in  self.tokenize_block(block):
                    token and tokens.append(token)
            else:
                for token in  self.re_skip.split (block):
                    token and tokens.append(token)
        return tokens
