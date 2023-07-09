"""
This is the base class for single_solver and multi_solver.
"""
class BaseSolver:

    def split_into_words(self, content: str) -> list:
        """
        Accept a filestring and return a list of words.
        """      
        # processing
        content = content.replace('\n', ' ')
        content = content.lower()
        words = content.split()
        
        return words
    
    def get_word_count(self, words: list[str], stop_words: list[str]) -> dict:
        """
        Accept words and stop_words, delete stop_words from words,
        return the word count dict. 
        """
        # Create a dictionary to count the number of each word
        word_count = {}
        for word in words:
            if word in stop_words:
                continue
            else:
                word_count[word] = word_count.get(word, 0) + 1
        """
        In python, why would 
        `sorted(word_count.keys(), key=lambda x: word_count[x], reverse=True)' 
        be thousands times faster than 
        'sorted(word_count.items(), key=x:x[1], reverse=True)'?
        """
        return word_count

