'''
Programming Assignment 1 

Multiprocessing Algorithm
1) read datafile (in binary) and keep a list of byte positions for beginning of line for every CHUNK_SIZE
2) create a mulitprocessing pool with X number of processes
3) each worker process takes a byte starting position and moves the file pointer there,
   then it reads through CHUNK_SIZE number of lines and processes the tokens and counts them in a local counter
4) each worker process returns its lcoal counter for its chunk and the global counter is updated with it

'''

from collections import Counter
import timeit
import psutil
from multiprocessing.pool import Pool
import os

data_fh = (
    # "dataset/data_300MB.txt"
    "../data_2.5GB.txt"
     # "dataset/data_16GB.txt"
)

k = 3 # find most common k words

# punctuation = set("!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~–")

stopwords = set()
with open("../stopwords.txt", "r") as f:
    stopwords.update(f.read().splitlines())

#--------------------------------------------------


def process(start_position, chunk_size):

    # p_start = timeit.default_timer()

    local_counter = Counter()

    with open(data_fh, "r") as f:

        current_line = 0

        # fastforward pointer to starting position in chunk
        f.seek(start_position)
        for line in f:
            for token in line.split():
                if token.lower() not in stopwords: 
                    local_counter.update({token:1}) #add to counter

            current_line+=1
            if current_line == chunk_size: #only process number of lines in chunk_size
                break

    # p_end = timeit.default_timer()
    # print(f'process done in {p_end - p_start}', flush=True) 

    return local_counter
    # end process()


def main():

    CHUNK_SIZE = 1_000_000 #number of lines to process at once

    start = timeit.default_timer()

    byte_list = [0] # byte positions in file of beginning of every chunk 
    current_line = 0 
    with open(data_fh, 'rb') as fp:
        for _ in fp:
            current_line += 1
            if current_line % CHUNK_SIZE == 0:
                byte_list.append(fp.tell())

    line_time = timeit.default_timer()
    print(f'time to get total line count: {line_time - start}')

    global_counter = Counter()

    NUM_WORKER_PROC = os.cpu_count() # = 10 for M1 pro
    # NUM_WORKER_PROC = 20
    pool = Pool(NUM_WORKER_PROC)

    # each worker processes a chunk of the file starting with their specified byte position and returns the local counter dict
    for local_counter in pool.starmap(process, zip(byte_list, [CHUNK_SIZE]*len(byte_list))):
        global_counter.update(local_counter)
    
    pool.close()
    pool.join()

    k_list = global_counter.most_common(k)

    stop = timeit.default_timer()
    print(f'{data_fh}: Multiprocessing & separate counter per process - {NUM_WORKER_PROC} workers & {CHUNK_SIZE} chunk size - Time: {stop - start}') 
    print(k_list)  
    print(f"Execution time in minutes: {(stop-start)/60}")

    #providing time interval (seconds) as parameter to the function over which the average CPU usage will be calculated
    cpu_usage = psutil.cpu_percent(stop-start) 
    print("average CPU usage:", cpu_usage, "%")

    #This is written at the very end (after CPU consumption statements)
    p = psutil.Process()
    print("memory consumed in MiB",p.memory_info().rss/1024 ** 2)  # in bytes


if __name__ == "__main__":
    main()

# for verifying results
# 300MB: [('European, 318734), ('Mr', 210680), ('would', 180717)] 9 & 20
# 2.5GB: [('said', 2612132), ('would', 910781), ('one', 812226)] 123 & 207
# 16GB: [('said', 16958970), ('would', 5787939), ('one', 5015553)] 1138


'''
OUTPUT:

time to get total line count: 2.7351707499474287
process done in 14.68886500003282
process done in 87.48727949999738
process done in 88.71284758299589
dataset/data_2.5GB.txt: Multiprocessing & separate counter per process - 10 workers & 10000000 chunk size - Time: 92.85069495800417
[('said', 2612132), ('would', 910781), ('one', 812226)]
Execution time in minutes: 1.5475115826334027
average CPU usage: 6.6 %
memory consumed in MiB 476.234375

~~~~~

time to get total line count: 17.32083199999761
process done in 91.89085174998036
process done in 128.09788491600193
process done in 128.1672099159914
process done in 128.31682470801752
process done in 129.3176655410207
process done in 130.44224341702648
process done in 130.54924995801412
process done in 130.60426083399216
process done in 130.8450522919884
process done in 132.2896359169972
process done in 21.07913537498098
process done in 97.35952887497842
process done in 88.33427112497156
process done in 89.66290225001285
dataset/data_16GB.txt: Multiprocessing & separate counter per process - 10 workers & 10000000 chunk size - Time: 241.7983833749895
[('said', 16958970), ('would', 5787939), ('one', 5015553)]
Execution time in minutes: 4.029973056249825
average CPU usage: 7.3 %
memory consumed in MiB 1576.4375

time to get total line count: 18.050730791990645
dataset/data_16GB.txt: Multiprocessing & separate counter per process - 20 workers & 1000000 chunk size - Time: 205.03924366697902
[('said', 16958970), ('would', 5787939), ('one', 5015553)]
Execution time in minutes: 3.417320727782984
average CPU usage: 7.3 %
memory consumed in MiB 2152.15625

time to get total line count: 17.18193883402273
dataset/data_16GB.txt: Multiprocessing & separate counter per process - 20 workers & 5000000 chunk size - Time: 198.57349329197314
[('said', 16958970), ('would', 5787939), ('one', 5015553)]
Execution time in minutes: 3.309558221532886
average CPU usage: 6.5 %
memory consumed in MiB 1639.234375

'''
