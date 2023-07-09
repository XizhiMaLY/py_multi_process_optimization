from single_module import single_solver
from multi_module import multi_solver
from multi_module_unoptimized import multi_solver_unoptimized
import argparse
import os
import psutil
from multiprocessing import cpu_count


FILES = {
        '50': '../small_50MB_dataset.txt',
        '300': '../data_300MB.txt',
        '2.5': '../data_2.5GB.txt',
        '16': '../data_16GB.txt'
        }
stop_filename = "../NLTK's list of english stopwords"


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('file_number', type=str,
                           help='50:50MB, 300:300MB, 2.5:2.5GB, 16:16GB',
                           default='50')
    argparser.add_argument('mode', type=str,
                           help='single:single process, multi:multi process, multi_uno:multi process unoptimized')
    argparser.add_argument('K', type=int,
                           help='top K most frequent words')
    args = argparser.parse_args()

    if args.mode == 'single':

        # single processing
        if args.file_number == '16':
            # large file, need to calculate chunk size
            file_process_mem_rate = 300/(3.9*1024)
            spared_ram = psutil.virtual_memory().available * 0.9
            num_cpu = cpu_count()
            inflate_rate = 1
            file_chunk_size = int(spared_ram/num_cpu/inflate_rate*file_process_mem_rate)
            file_process_mem_rate = 300/(3.9*1024)
            topK = single_solver.get_topK('l', args.K, FILES[args.file_number],
                                         stop_filename, file_chunk_size)
            print(topK)
        else:
            # small file, read directly.
            topK = single_solver.get_topK('s', args.K, FILES[args.file_number],
                                          stop_filename)
            print(topK)

    elif args.mode == 'multi':
        topK = multi_solver.get_topK_main(args.K, FILES[args.file_number],
                                          stop_filename)
        print(topK)
    else:  # multi_uno
        topK = multi_solver_unoptimized.get_topK_main(args.K, FILES[args.file_number],
                                                      stop_filename)
        print(topK)

if __name__ == "__main__":
    main()


