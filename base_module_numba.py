from numba import jit

class BaseSolver:
    
    @staticmethod
    def split_into_words(content: str) -> list:
        content = content.replace('\n', ' ')
        content = content.lower()
        words = content.split()
        
        return words
    
    @staticmethod
    @jit(nopython=True)
    def get_word_count(words: list[str], stop_words: list[str]) -> dict:
        word_count = {}
        for word in words:
            if word in stop_words:
                continue
            else:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1


        return word_count
