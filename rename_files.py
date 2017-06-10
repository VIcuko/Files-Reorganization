import os

def rename_files():
	file_list = os.listdir("./files")
	print(file_list)

rename_files()