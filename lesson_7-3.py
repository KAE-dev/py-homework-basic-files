from os import listdir
import operator

sorted_file_path = 'resources/files/sorted/result.txt'
file_extension = '.txt'
files_path = 'resources/files/'


def sorted_and_writing_files():
    all_files = listdir(files_path)
    text_files_list = list(filter(lambda x: x.lower().endswith(file_extension), all_files))
    dict = {}
    for text_file in text_files_list:
        with open(files_path + text_file, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            data_length = len(data)
            dict[text_file] = [data_length, data]

    with open(sorted_file_path, "w") as file_write:
        file_write.write("")

    for key, value in sorted(dict.items(), key=operator.itemgetter(1)):

        with open(sorted_file_path, "a", encoding='UTF-8') as file_write:
            file_write.write(key + "\n")
            file_write.write(str(value[0]) + "\n")
            for date in value[1]:
                file_write.write(date.strip() + "\n")


sorted_and_writing_files()
