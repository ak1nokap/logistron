import random
symbols ='йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'


text = "".join(random.choice(symbols) for _ in range(8))
print(text)