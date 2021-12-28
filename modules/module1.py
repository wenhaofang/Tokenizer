# Maximum Matching

class Tokenizer:
    def __init__( self , word_list ):
        self.word_list = word_list

    def fmm(self, sentence, max_len = 7):
        tokens = []
        str_min = 0
        str_max = len(sentence)
        start_idx = str_min
        while start_idx < str_max:
            for end_idx in range (
                min(str_max, start_idx + max_len), start_idx, -1
            ):
                if sentence[start_idx: end_idx] in self.word_list:
                    break
            tokens.append(sentence[start_idx: end_idx])
            start_idx = end_idx
        return tokens

    def bmm(self, sentence, max_len = 7):
        tokens = []
        str_min = 0
        str_max = len(sentence)
        end_idx = str_max
        while end_idx > str_min:
            for start_idx in range (
                max(str_min, end_idx - max_len), end_idx
            ):
                if sentence[start_idx: end_idx] in self.word_list:
                    break
            tokens.append(sentence[start_idx: end_idx])
            end_idx = start_idx
        return tokens[::-1]

    def tokenize(self, sentence, max_len = 7):
        f_result = self.fmm(sentence, max_len)
        b_result = self.bmm(sentence, max_len)
        if len(f_result) == len(b_result):
            f_number = sum([1 for token in f_result if len(token) == 1])
            b_number = sum([1 for token in b_result if len(token) == 1])
            if f_number == b_number:
                return (
                    f_result or b_result
                )
            elif f_number < b_number:
                return f_result
            elif b_number < f_number:
                return b_result
        elif len(f_result) < len(b_result):
            return f_result
        elif len(b_result) < len(f_result):
            return b_result
