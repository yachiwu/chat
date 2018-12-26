def read_file(filename): #讀取檔案
	lines = []
	with open(filename,'r',encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines 
def convert(lines): #將檔案的資料做轉換
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:	
			new.append(person + ' : '+line)	
	return(new)
def write_file(filename,lines): #寫入新的檔案中
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')
def main():	#main執行
	lines = read_file('input.txt')	
	lines = convert(lines)	
	write_file('output.txt',lines)
main()