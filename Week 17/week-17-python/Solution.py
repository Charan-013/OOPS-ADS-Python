import sys
import itertools


def to_read_file(file_path):
    """
    Read a file and return all whitespace-separated tokens as a list of strings.
    """
    with open(file_path, "r") as f:
        return f.read().split()


def load_dictionary(file_path):
    """
    Build a frequency dictionary from the words in the given file. Make sure to lower the words
    Returns a dict mapping word -> count.
    """
    s = to_read_file(file_path)
    d = {}
    for word in s:
        word = word.lower()
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


class T9:
    """
    Basic T9 predictive text implementation.
    """

    def __init__(self, dictionary):
        """
        Initialize with a word-frequency dict (word -> frequency).
        """
        self.dictionary = dictionary

    def get_all_words(self, prefix):
        """
        Return all dictionary words that start with the given prefix, sorted lexicographically.
        """

        l = []
        for k in self.dictionary:
            if k.startswith(prefix):
                l.append(k)
        return sorted(l)

    def potential_words(self, signature):
        """
        Enumerate all valid dictionary words matching the T9 numeric signature.
        """
        d = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        l = []
        tones = [int(x) for x in list(signature)]
        t = [d[i] for i in tones]
        t9l = list("".join(x) for x in itertools.product(*(t)))
        new = []
        for ele in t9l:
            if ele in self.dictionary:
                new.append(ele)

        return new

    def get_suggestions(self, words, k):
        """
        From an iterable of words, return the top-k suggestions by frequency (desc),
        then by word length (asc), then lex order.
        """
        count = 0
        l = []
        for word in words:
            if word in self.dictionary:
                l.append((self.dictionary[word], word))
        l.sort(key=lambda x:((-x[0]),len(x[1])))
        
        new = []
        for ele in l:
            if count < k:
                new.append(ele[1])
                count += 1  
    
        return new

    def t9(self, signature, k):
        """
        Combined method: get top-k suggestions for the given numeric signature.
        """
        l = self.potential_words(signature)
        g = self.get_suggestions(l, k)

        return g


def main():
    dict_path = "./Files/t9.csv"
    # Read operation
    case = sys.stdin.readline().strip()
    if not case:
        return

    if case == "loadDictionary":
        st = load_dictionary(dict_path)
        # For each key in remaining input, print frequency
        for line in sys.stdin:
            key = line.strip()
            if key:
                print(st.get(key))

    elif case == "getAllPrefixes":
        t9 = T9(load_dictionary(dict_path))
        # For each prefix, list all matching words
        for line in sys.stdin:
            prefix = line.strip()
            if prefix:
                for word in t9.get_all_words(prefix):
                    print(word)

    elif case == "potentialWords":
        t9 = T9(load_dictionary(dict_path))
        count = 0
        # For each numeric signature, list all potential words
        for line in sys.stdin:
            signature = line.strip()
            if signature:
                for word in t9.potential_words(signature):
                    count += 1
                    print(word)
        if count == 0:
            print("No valid words found.")

    elif case == "topK":
        t9 = T9(load_dictionary(dict_path))
        # First line is k
        k_line = sys.stdin.readline().strip()
        if not k_line:
            return
        k = int(k_line)
        # Remaining lines are words to consider
        words = [line.strip() for line in sys.stdin if line.strip()]
        for word in t9.get_suggestions(words, k):
            print(word)

    elif case == "t9Signature":
        t9 = T9(load_dictionary(dict_path))
        # First line is k
        k_line = sys.stdin.readline().strip()
        if not k_line:
            return
        k = int(k_line)
        # Remaining lines are numeric signatures
        for line in sys.stdin:
            signature = line.strip()
            if signature:
                for word in t9.t9(signature, k):
                    print(word)


if __name__ == "__main__":
    main()
