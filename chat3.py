
lines = []
with open('line_chat2.txt', 'r', encoding='utf-8') as f: #打開檔案 讀取模式
	for line in f:
		lines.append(line. strip())

for line in lines:
	s = line.split(' ') #清單分割法，才可以取出想要的部分
	time = s[0][:5] #s[0]裡面的前四個字 0-5 不包含5
	name = s[0][5:]
	print(name)
