#提示：
#1.分析数据存在哪里（打开“检查”工具，刷新页面，查看第0个请求，看【response】）
#2.观察网址规律（多翻几页，看看网址会有什么变化）
#3.获取、解析和提取数据（需涉及知识点：queue、gevent、request、BeautifulSoup、find和find_all）
#4.存储数据（csv本身的编码格式是utf-8，可以往open（）里传入参数encoding='utf-8'。这样能避免由编码问题引起的报错。)
#注：在练习的【文件】中，你能找到自己创建的csv文件。将其下载到本地电脑后，请用记事本打开，因为用Excel打开可能会因编码问题出现乱码。
from gevent import monkey
monkey.patch_all()
import gevent
from gevent.queue import Queue
import time,csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

start = time.time()


def get_tv_info(my_url):
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	browser = webdriver.Chrome(options=chrome_options)
	# browser = webdriver.Chrome()
	browser.get(my_url)
	time.sleep(0.5)
	films_info = browser.find_elements_by_class_name("mov_con")
	# print(films_info)
	films_info_list = []
	for film in films_info:
		film_name = film.find_element_by_tag_name('h2').text
		# print(film_name)
		film_info = film.find_elements_by_tag_name('p')
		film_info_list = [film_name]
		for film_function in film_info:
			film_info_list.append(film_function.text)
		films_info_list.append(film_info_list)
	browser.close()
	print('get tv info')
	return films_info_list
# print(films_info_list)


def mtime_writer(tv_list):
	with open('时光网电视剧top100.csv', 'a+', newline='', encoding='utf-8-sig') as file1:
		my_writer = csv.writer(file1)
		for line in tv_list:
			my_writer.writerow(line)
	time.sleep(0.5)
	print('cvs write ok')


# url = "http://www.mtime.com/top/tv/top100/index-10.html"
# print(get_tv_info(url))


url_list = ["http://www.mtime.com/top/tv/top100/"]
for i in range(2, 11):
	url = "http://www.mtime.com/top/tv/top100/index-" + str(i) + ".html"
	url_list.append(url)
# print(url_list)
work = Queue()
for url1 in url_list:
	work.put_nowait(url1)


def spider():
	while True:
		if work.empty():
			print('mission done')
			break
		else:
			url2 = work.get_nowait()
			top100_info = get_tv_info(url2)
			# print(top100_info)
			mtime_writer(top100_info)
			print('loop')
	print('spider')


tasks_list = []
for x in range(4):
	task = gevent.spawn(spider)
	tasks_list.append(task)
gevent.joinall(tasks_list)
print('ok')
end = time.time()
print(end-start)