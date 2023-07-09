import os
file = '../small_50MB_dataset.txt'
file_size = os.stat(file).st_size
print(file_size, file_size/(1024*1024))

with open('../small_50MB_dataset.txt', 'r') as file:
    for i in range(5):
        # words_chunk = file.readlines(100)
        # print(words_chunk)
        words_chunk = file.read(15)
        print(words_chunk)
        print('-------------------------')
