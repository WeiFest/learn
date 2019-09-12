# 单词词汇量测试程序

import requests, openpyxl,random
from bs4 import BeautifulSoup

url_shanbay = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
			}
category_list = ['CET4', 'GMAT', 'NGEE', 'CET4', 'CET6', 'TEM', 'TOEFL', 'GRE', 'IELTS', 'NONE']
wordbank_list = ['1566531600314', '1566531679773', '1566531723388', '1566532126683', '1566532149263', '1566532167158',
				 '1566532186676', '1566532210462', '1566532230021', '1566531759900']
while True:
	try:
		user_choice = int(input('请选择词库编号：0.GMT 1.考研 2.高考 3. 四级 4.六级 5.英专 6.托福 7.GRE 8.雅思 9.任意'))
		break
	except Exception as e:
		print('输入有误，请重新选择!')
		continue
params = {'category': category_list[user_choice],
		  '_': str(wordbank_list[user_choice]),
		  }
res_shanbay = requests.get(url_shanbay, headers=headers, params=params)
#print(res_shanbay.status_code)
json_res = res_shanbay.json()
i = 0
words_list = []
words_known =[]
words_unknown = []
words_grasp = []
for data in json_res['data']:
	words_list.append(data['content'])
	#print(words_list)
for word in words_list:
	while True:
		try:
			choice = int(input('是否认识单词{} ？ 不认识 按‘0’，任意数字测试下一个'.format(word)))
			break
		except Exception as e:
			print('输入有误，请重新选择！')
	if choice:
		words_known.append(word)
	else:
		words_unknown.append(word)


for definition_choices in json_res['data']:
	question = 0
	pk_list = []
	pk = definition_choices['pk']
	if definition_choices['content'] in words_known:
		print('单词{}测试，请选择正确的词义：'.format(words_known[i]))
		for definition in definition_choices['definition_choices']:
			print(question, '>', definition['definition'])
			pk_list.append(definition['pk'])
			question += 1
		print('————————————————————————')
		while True:
			try:
				answer = int(input('请输入你的选择：'))
				break
			except Exception as e:
				print('输入有误，请重新选择！')
		if answer in [0, 1, 2, 3]:
			if pk_list[answer] == pk:
				print('选择正确')
				words_grasp.append(words_known[i])
			else:
				print('选择错误')
		else:
			print('选择错误')
		i += 1
	else:
		pass
print('{}个单词中，你认识{}个单词，掌握{}个单词'.format(len(words_list), len(words_known), len(words_grasp)))
