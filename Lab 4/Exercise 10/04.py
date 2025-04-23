import os

source_dir = 'Folder'            
file_name = 'abcdefg.txt'               
destination_dir = 'NEW'

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    print("Subdirectory created:", destination_dir)
else:
    print("Subdirectory already exists:", destination_dir)


source_file_path = os.path.join(source_dir, file_name)
destination_file_path = os.path.join(destination_dir, file_name)


if os.path.exists(source_file_path):
    
    with open(source_file_path, 'rb') as source_file:
        file_data = source_file.read()

    with open(destination_file_path, 'wb') as dest_file:
        dest_file.write(file_data)

    print("File copied successfully from", source_dir, "to", destination_dir)
else:
    print("Source file does not exist:", source_file_path)