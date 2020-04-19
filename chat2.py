#input 寫入檔案output

import os 
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())#把每一行裝進清單 所以上面要寫一個line的空清單
	return lines


def convert(lines):
	new = []
	person = None
	tina_word_count = 0 #字的計數
	tina_sticker_count = 0
	tina_image_count = 0
	Jane_word_count = 0
	Jane_sticker_count = 0
	Jane_image_count = 0

	for line in lines: #讀取對話紀錄
		s = line.split(' ') #遇到空白建 幫我切一刀 切割完後會變成一個清單
		time = s[0]
		name = s[1] 
		if name == 'tina':
			if s[2] == '貼圖': #s2表示對話紀錄開始的部分
				tina_sticker_count += 1
			elif s[2] == '圖片':
				tina_image_count += 1
			else:
				for msg in s[2:]: # 讀取每一行
					tina_word_count += len(msg) # msg 長度加進tina word count裡面
		elif name == '趙真':
			if s[2] == '貼圖':
				Jane_sticker_count += 1
			elif s[2] == '圖片':
				Jane_image_count += 1
			else:
				for msg in s[2:]: 
					Jane_word_count += len(msg)
	print('tina說了', tina_word_count, '傳了', tina_sticker_count, '個貼圖', tina_image_count, '個圖片')
	print('趙真說了', Jane_word_count, '傳了', Jane_sticker_count, '個貼圖', Jane_image_count, '個貼圖')	
		#print(s)
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #每一行寫入檔案


def main():
	lines = read_file('line_chat.txt')
	lines = convert(lines) 
	#write_file('output.txt', lines)

	
main()