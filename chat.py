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
	for line in lines: #讀取對話紀錄
		if line == 'tina':
			person = 'tina'
			continue
		elif line == '森':
			person = '森'
			continue
		if person:
			new.append(person + ': ' + line)
	return(new)

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #每一行寫入檔案


def main():
	lines = read_file('input.txt')
	lines = convert(lines) 
	write_file('output.txt', lines)
main()