"""
This module creates a multi_solver class,
which contains mathods for words count by multi_processing.
"""
from base_module import *
import psutil
import os
from multiprocessing import Pool, cpu_count

class MultiSolver(BaseSolver):

    def read_file_start_end(self, filename: str, start: int, end: int) -> str:
        """
        Return a filestring from start to end.
        """ 
        with open(filename, 'r', encoding='utf-8') as f:
            f.seek(start)
            seek_right_start = 1
            bit = 0
            while seek_right_start:
                # print('end:', end, 'start:', start)
                try:
                    content = f.read(end - start)
                    return content
                except UnicodeDecodeError:  # For more information, see README file note! part.
                    print('Detected UnicodeDecodeError at', start, '. Trying to skip this byte.')
                    bit += 1
                    f.seek(start + bit)
            return -1

    def concatenate_words_counts(self, word_counts):
        word_count = {}
        for partial_result in word_counts:
            for word, count in partial_result.items():
                word_count[word] = word_count.get(word, 0) + count
        return word_count

    def get_topK_sub(self, filename: str, stop_filename: str, start: int, end: int) -> dict:
        """
        Each child(sub) process will run this function simutaniously.
        Read words and stops, split, remove stops and count.
        Return words_counts.
        """

        # Read words and stops
        print('Reading file at', int(start/1024/1024), 'MB.')
        words = self.read_file_start_end(filename, start, end)
        with open(stop_filename, 'r', encoding='utf-8') as file:
            stops = file.read()
        
        # Split
        words = self.split_into_words(words)
        stops = self.split_into_words(stops)
        
        # Remove stops and count
        word_count = self.get_word_count(words, stops)

        return word_count

    def get_topK_main(self, K: int, filename: str, stop_filename: str) -> list[str]:
        """
        In order to process large file, we split the file by following steps:
            1. Get the min of ram and filesize, devide that number by number of cpus,
            name it as chunk_size.
            2. Chunk_size is the number of file content we want to feed in into starmap,
            which is a function performing multi-processing.
        Question:
            After we read the file according to chunk_size, we still need to perform
            some actions, do we have ram space for that?
            The answer is no. In line 68 if you uncomment it to read file according to
            chunk_size, you will notice that swap memory is high and not every cpu is
            running on max load. Meaning that the memory is not enouth that system need to 
            use some disk space as vertual memory.
        """
        
        # In order to solve the question, I processed a 300MB file and recorded its memory use,
        # which is 3900MB, so the file size to memory size rate can be calculated as below:
        file_process_mem_rate = 300/(3.9*1024)
        # file_process_mem_rate = 1
        # Meaning that in our case, for 1 byte of memory,
        # python can process file_process_mem_rate byte of txt file,
        # this is tested out in single_module_mem_size.py,
        # what a efficient language!
        file_size = os.path.getsize(filename)
        spared_ram = psutil.virtual_memory().available * 0.9
        num_cpu = cpu_count()
        inflate_rate = 1
        file_chunk_size = int(spared_ram/num_cpu/inflate_rate*file_process_mem_rate)

        print("Allocated memory for multi processing: {}GB.".format(int(spared_ram/1024/1024/1024)))
        print("Number of processes in use: {}.".format(num_cpu))
        print('File chunk size to be read for each process: {}MB.'.format(int(file_chunk_size/1024/1024)))

        # Calculate file read ranges for each process to maximum performance.
        num_chunks = file_size // file_chunk_size
        ranges = [(i * file_chunk_size, (i + 1) * file_chunk_size)
                  for i in range(int(num_chunks))]
        ranges[-1] = (ranges[-1][0], file_size)  # let last item cover the end.


        with Pool(processes=num_cpu*inflate_rate) as pool:
            word_counts = pool.starmap(self.get_topK_sub, 
                                       [(filename, stop_filename, start, end) for start, end in ranges])
        
        word_count = self.concatenate_words_counts(word_counts)

        return sorted(word_count.keys(), key=lambda x: word_count[x], reverse=True)[:K]

multi_solver = MultiSolver()

    
