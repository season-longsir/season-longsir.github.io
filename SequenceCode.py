import random
text = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
tl = list(text)
textl=random.sample([i for i in tl],len(tl))
print('您的序列码为:',''.join(textl))
