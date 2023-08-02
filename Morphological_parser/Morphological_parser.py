from janome.tokenizer import Tokenizer
text = '彼女と国立新美術館へ行った。'
t = Tokenizer()
for token in t.tokenize(text):
  print(token)