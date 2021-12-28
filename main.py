from modules.module1 import Tokenizer as Tokenizer1 # Maximum Matching
from modules.module2 import Tokenizer as Tokenizer2 # UniGram
from modules.module3 import Tokenizer as Tokenizer3 # HMM

print('initialize tokenizer1')

word_list = []
with open('datas/data1/dict.txt', 'r', encoding = 'utf-8') as txt_file:
    for line in txt_file:
        word = line.split()[0]
        word = word.strip()
        word_list.append(word)

tokenize1 = Tokenizer1(word_list)

print('initialize tokenizer2')

word2freq = {}
with open('datas/data1/dict.txt', 'r', encoding = 'utf-8') as txt_file:
    for line in txt_file:
        word , freq = line.split()[:2]
        word = word.strip()
        freq = freq.strip()
        word2freq[word] = int(freq)

tokenize2 = Tokenizer2(word2freq)

print('initialize tokenizer3')

from datas.data2.prob_start import P as start_prob
from datas.data2.prob_trans import P as trans_prob
from datas.data2.prob_emit  import P as emit_prob

tokenize3 = Tokenizer3(start_prob, trans_prob, emit_prob)

print('start tokenizing')

sentences = [
    '我是中国人，我出生在中华人民共和国',
    '南京市长江大桥欢迎您'
]

for idx, sentence in enumerate(sentences):
    print('*' * 70)
    print('sentences%d: %s' % (idx, sentence))
    print('tokenizer1:', tokenize1.tokenize(sentence))
    print('tokenizer2:', tokenize2.tokenize(sentence))
    print('tokenizer3:', tokenize3.tokenize(sentence))
