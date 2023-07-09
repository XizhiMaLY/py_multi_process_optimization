from single_module import *
import time
singler_solver0 = SingleSolver()
# print(singler_solver0.__dir__())
word_count = singler_solver0.get_topK(1, '../data_2.5GB.txt', "../NLTK's list of english stopwords")
a = time.time()
word_count_s = sorted(word_count.keys(), key=lambda x: word_count[x], reverse=True)
b = time.time()
print(b-a)
word_count_ss = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
c = time.time()
print(c-b)

