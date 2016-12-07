import struct
import shutil
import os
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':
	path = raw_input("Path to demos or press ENTER to use current path: ").replace('/', '\\')
	make_copy = raw_input("Copy original files to new directory (original)? (y/n) ")

	if path == '':
		path = os.getcwd()

	if path[-1] != '\\':
		path = path+'\\'

	demo_files = [d for d in listdir(path) if isfile(join(path, d))]
	for demo_file in demo_files:
		if not demo_file[-4:] == '.dem':
			continue

		full_demo_path = path+demo_file

		map_name = ''
		with open(full_demo_path, 'rb') as demo:
			demo_data = demo.read()

			header_map_name = demo_data[536:796]
			mup = struct.unpack('260s', header_map_name)[0]
			map_name = mup.strip('\x00')

			demo.close()


		if make_copy.lower() == 'y':
			original_demos_dir = path+"\\original\\"
			if not os.path.exists(original_demos_dir):
				os.makedirs(original_demos_dir)

			shutil.copy(full_demo_path, original_demos_dir)


		new_demo_name = demo_file\
						.replace(path, '')\
						.replace('.dem', '')\
						+"_"+map_name+".dem"

		print "Renaming "+demo_file+" -> "+new_demo_name

		os.rename(full_demo_path, path+new_demo_name)

	raw_input("Done.")
