import os

def rename_files():
	file_list = os.listdir("/Users/iTurbo/Google Drive/3. Developer/4. Python/Udacity/files_reorganization/files")
	print(file_list)
	
	saved_path = os.getcwd()
	print ("Current working directory is: " + saved_path)

        os.chdir("/Users/iTurbo/Google Drive/3. Developer/4. Python/Udacity/files_reorganization/files")

	for file_name in file_list:
                os.rename(file_name, file_name.translate(None,"0123456789"))
		
	os.chdir(saved_path)
	
rename_files()
