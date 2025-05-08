#　這是一個要判別年齡的程式
Name = input('你叫什麼名字？')
print(f'你好阿，{Name}！')
print('我有一些問題想問你')
user_input = input('請問你有開過車嗎？')
if user_input in [ '有','好像有','Yes','yes','有阿']:
	age = int(input('那請問你幾歲？'))
	if age < 18:
		legit_age3 = 18 - age
		print(f'{Name},依據法律，你還不能開車喔！這樣很危險。再等{legit_age3}年，考到駕照再開吧!')
	else:
		print(f'{Name},瞭解，你很守法！')
elif:
	age = int(input('那請問你幾歲？'))
	if age >= 18:
		legit_age1 = age - 18
		print(f'{Name},你已經年滿18歲經過{legit_age1}年了，怎麼不去考駕照？')
	else:
		legit_age2 = 18 - age
		print(f'{Name},再過{legit_age2}年，你就可以去考駕照了！')	
else:
	print('只能輸入有或沒有啦！')
