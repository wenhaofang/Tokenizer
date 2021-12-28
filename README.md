## Tokenizer

This repository includes some demo tokenizers (especially for Chinese).

Note: The project refers to [jieba](https://github.com/fxsjy/jieba)

Methods:

* `method1 (DONE)`: Maximum Matching
* `method2 (DONE)`: UniGram
* `method3 (DONE)`: HMM
* `method4 (TODO)`: CRF

### Catalog Description

```
+ datas
    + data1
        - dict.txt # Synchronize with `jieba/dict.txt`
    + data2
        - prob_emit.py  # Synchronize with `jieba/finalseg/prob_emit.py`
        - prob_start.py # Synchronize with `jieba/finalseg/prob_start.py`
        - prob_trans.py # Synchronize with `jieba/finalseg/prob_trans.py`
+ modules
    - module1
    - module2 # Refering to `jieba/__init__.py`
    - module3 # Refering to `jieba/finalseg/__init__.py`
```

### Start

```shell
PYTHONIOENCODING=utf-8 PYTHONPATH=. python main.py
```
