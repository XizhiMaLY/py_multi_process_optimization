This markdown records a problem I met about sorting in multiprocessing.
# background
There are two sorting ways:
```
sorted_word_count = sorted(count_words.keys(), key=lambda x: count_words[x], reverse=True)

and

sorted_word_count = (sorted(count_words.items(), key=lambda x: x[1], reverse=True))
```

In theory there shouldn't be much different in terms of time and it does not.
(for indexing in tuple and finding in dictionary are both O(1)) **Howeverm, 
In the multi_processing code below, the second way is thousands of times slower.**

```python
"""read the file as a whole, after smallcaped, devide the words list into serveral parts,
and perform the following steps by multi-procesing
loop through the txt and create word count dictionary,
then sort the dictionary and get top k words.
"""

# import packages
import multi_wordcount
from multiprocessing import Pool
import time

if __name__ == '__main__':
    filename = '../small_50MB_dataset.txt'
    filename = '../data_300MB.txt'
    filename = '../data_2.5GB.txt'
    # filename = '../data_16GB.txt'
    stopWordsFilename = '../NLTK\'s list of english stopwords'
    start_time = time.time()
    words, stops = multi_wordcount.getWordsNStops(filename, stopWordsFilename)
    time_1 = time.time()
    print('time for split text:', time_1-start_time)

    num_processes = 8
    pool = Pool(processes=num_processes)

    """
    Here we try to remove stop words while mapping"""
    # split words into list of list(subset of words)
    wordslt = multi_wordcount.split_list_into_n_parts(words, num_processes*40)


    count_words = pool.starmap(multi_wordcount.get_count_words, [(word_s, stops) for word_s in wordslt])
    time_2 = time.time()
    print('time for mapping:', time_2-time_1)

    # reduce
    from functools import reduce
    count_words = reduce(multi_wordcount.merge_counts, count_words)
    time_3 = time.time()
    print('time for reducing:', time_3-time_2)
    # sort
    sorted_word_count = sorted(count_words.keys(), key=lambda x: count_words[x], reverse=True)
    # sorted_word_count = (sorted(count_words.items(), key=lambda x: x[1], reverse=True))
    time_4 = time.time()
    print('time for sorting:', time_4-time_3)
    # get first k words
    k = 10 
    print(sorted_word_count[:k])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
```

