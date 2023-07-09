# Py multi-process optimization
The goal of this project is too implement python multi-processing and find out
the attributes that affect a process' speed. The conclusion is that multiprocessing is way fast
in terms of large file processing and memory allocation is something need to be take care of.
## Use
```python
python main.py -h

# For example
# Get top10 most frequent word count
# By multi-process for 2.5GB file.
python main.py 2.5 multi 10

```

## Goal
The task of this assignment is to optimize the performance of reading a huge text tile, do simple cleaning, count the frequency of words, and return the top k words with highest frequency.

Main issues to take care of:

* The largest file can't fit into memory;
* Allocate memory to different process correctly so that all cpu runs on full load and no swap memory provoked.

## Environment
* Device: MacBook Air M1, 4 performance cpu and 4 efficient cpu, 16GB memory.
* python: 3.x

## Data
Text file of 50MB, 300MB, 2.5GB and 16GB.

## Solvers
|Solver name|Description|
|-----------|-----------|
|`single_module.py`    |single process solver|
|`multi_module.py`     |multi process solver with optimized memory allocation|
|`multi_module_unoptimized.py`|multi process solver without optimized memory allocation|

> **Warning**
>
>Please pay attention to your swap memory or virtual memory if you are using win machine. Although theoretically,
>the program will allocate memory, once swap memory is high and changing for a long time, it may shorten the disk life for your machine!


## Note!
There are Hindi words in the test files, which will provoke encoding error for `multi_module.py` and `multi_module_unoptimized.py` to some probability.
For example:

```python
cat test_read.txt
य शिकार की भूमिका निभाने से इंकार करते हैं।

In [14]: with open('test_read.txt', 'r') as f:
    ...:     print(list[f.read(12)])
    ...:
list['य शिकार की भ']

In [15]: with open('test_read.txt', 'r') as f:
    ...:     f.seek(1)
    ...:     print(list[f.read(12)])
    ...:
----------------------------------------------------------------
UnicodeDecodeError             Traceback (most recent call last)
Cell In[15], line 3
      1 with open('test_read.txt', 'r') as f:
      2     f.seek(1)
----> 3     print(list[f.read(12)])

File /opt/homebrew/anaconda3/lib/python3.9/codecs.py:322, in BufferedIncrementalDecoder.decode(self, input, final)
    319 def decode(self, input, final=False):
    320     # decode input (taking the buffer into account)
    321     data = self.buffer + input
--> 322     (result, consumed) = self._buffer_decode(data, self.errors, final)
    323     # keep undecoded input until the next call
    324     self.buffer = data[consumed:]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa4 in position 0: invalid start byte

```
However this has been taken care of, by using try except.

## Results

<img src="Process Time by File Size and Solver.png" width="70%">

|File Size|Solver Name|Time Cost(seconds)
|---------|-----------|-----------|
|50MB|single_module    |5.651s|
|50MB|multi_module     |about 1.8s*|
|50MB|multi_module_unoptimized_320|1.889s|
|50MB|multi_module_unoptimized_32|1.546s**|
|300MB|single_module    |38.124s|
|300MB|multi_module     |11.809s|
|300MB|multi_module_unoptimized_320|8.655s|
|300MB|multi_module_unoptimized_32|8.067s|
|2.5GB|single_module    |11m28.02s|
|2.5GB|multi_module     |1m31.21s|
|2.5GB|multi_module_unoptimized_320|1m32.35s|
|2.5GB|multi_module_unoptimized_16|3m22.14s|
|16GB|single_module    |36m58.02s|
|16GB|multi_module     |12m40.20s|
|16GB|multi_module_unoptimized_320|14m11.21s|

\* about means it can't be calculated practically as the file size is too small to be sliced.

** multi_module_unoptimized_32 32 means the file is divided into 32 parts to process. 320 mean 320 parts.

## Conclusion

1. Multi-processing is significantly faster than single process. The gap will increase as the file size increase.
2. For memory allocation of each process, there is an optimized spot, calculated by `spared_ram/num_cpu/inflate_rate*file_process_mem_rate`.
If the chunk size being too big, system will activate swap memory, which is very slow. You can see this by comparing `multi_module_unoptimized_16` and `multi_module_unoptimized_320`.
If the chunk size being too small, i/o time will increase. You can see this by comparing `multi_module` and `multi_module_unoptimized_320` 2.5GB.


