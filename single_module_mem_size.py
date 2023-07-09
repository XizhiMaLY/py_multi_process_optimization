"""
This module print the memory usage based on single_solver, for we
want to settle the best chunk_size for multi_processing, so that our
8 processers can use the same amount of memory and our 16GB memory can all be used.
So far, to read 300MB, a python process takes about 3.7GB memory.
So once we get the avaliable memory, we need to devide it by 8 and
then devide it by 3.7*1024*1024*1024, and mutiply by 300*1024*1024.
"""
from base_module import *
import sys
import psutil
import os
import time


class SingleSolver(BaseSolver):
    
    def get_process_memory(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss

    def get_topK_s(self, K: int, filename: str, stop_filename: str) -> list[str]:
        """
        Accept K, filename and stop words filename,
        return a list with top K most frequent words,
        s means small, if the dataset is small that
        machine can read into memory as a whole, then
        go with this, otherwise choose get_topK_l.
        """
        with open(filename, 'r') as file:   
            words = file.read()
        with open(stop_filename, 'r') as file:
            stops = file.read()
        print(os.getpid())

        print(sys.getsizeof(words))
        print(self.get_process_memory())
        # time.sleep(60)

        print(psutil.virtual_memory())

        words = self.split_into_words(words)

        print(sys.getsizeof(words))
        print(self.get_process_memory())

        stops = self.split_into_words(stops)
        word_count = self.get_word_count(words, stops)

        print(sys.getsizeof(word_count))
        print(self.get_process_memory())

        word_count = sorted(word_count.keys(), key=lambda x: word_count[x], reverse=True)
        
        return word_count[:K]


    def get_topK_l(self, chunk_size: int, K: int, filename: str, stop_filename: str) -> list[str]:
        """
        Accept chunk_size, which is the size every chunk which is feed
        into memory.
        The while loop will process each chunk a time,
        and word_count_accum will concatenate them together.
        """

        def merge_counts(counts1, counts2):
            """
            Combine two word count dictionaries.
            """
            for word, count in counts2.items():
                if word not in counts1:
                    counts1[word] = 0
                counts1[word] += counts2[word]
            return counts1
        
        with open(stop_filename, 'r') as file:
            stops = file.read()
        stops = self.split_into_words(stops)
        
        words_count_accum = {}
        with open(filename, 'r') as file:
            while True:
                words_chunk = file.read(chunk_size)
                # chunk_size is the number of bytes you want to read.
                if not words_chunk:
                    break
                words_chunk = self.split_into_words(words_chunk)
                words_count = self.get_word_count(words_chunk, stops)
                words_count_accum = merge_counts(words_count_accum, words_count) 
        
        words_count = sorted(words_count_accum.keys(), key=lambda x: words_count_accum[x], reverse=True)
        return words_count[:K]


    def get_topK(self, size: str, K: int, filename: str, stop_filename: str, chunk_size: int=0) -> list[str]:
        """
        Size = s means small data set(<2.5GB), = l means large set.
        For large set, program will read a filestring of chunk_size a time.
        """
        if size == 's':
            return self.get_topK_s(K, filename, stop_filename)
        else:  # i.e. if size == 'l':
            return self.get_topK_l(chunk_size, K, filename, stop_filename)


single_solver = SingleSolver()


