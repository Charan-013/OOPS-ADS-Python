import sys
import io
from functools import cmp_to_key
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Term:
    def __init__(self,query,weight):
        self.weight = weight
        self.query = query
    
    def __str__(self):
        return f"{self.weight}\t{self.query}"
    
    def compare_by_weight_desc(t1, t2):
        if t1.weight > t2.weight:
            return -1
        elif t1.weight < t2.weight:
            return 1
        else:
            return 0

    def compare_by_prefix_length(t1, t2, prefix_len):
        p1 = t1.query[:prefix_len]
        p2 = t2.query[:prefix_len]
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
        else:
            return 0
    
class BinarySearchDeluxe:

    def first_index_of(terms, key, cmp_func):
        left, right = 0, len(terms) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            cmp_result = cmp_func(terms[mid], key)
            if cmp_result < 0:
                left = mid + 1
            elif cmp_result > 0:
                right = mid - 1
            else:
                result = mid
                right = mid - 1
        return result

    def last_index_of(terms, key, cmp_func):
        left, right = 0, len(terms) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            cmp_result = cmp_func(terms[mid], key)
            if cmp_result < 0:
                left = mid + 1
            elif cmp_result > 0:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
        return result

class Autocomplete:
    def __init__(self,terms):
        self.terms = sorted(terms, key=lambda t: t.query)

    def all_matches(self,prefix):
        prefix_len = len(prefix)
        def prefix_comparator(t1, t2):
            return Term.compare_by_prefix_length(t1, t2, prefix_len)

        key_term = Term(prefix, 0)

        first = BinarySearchDeluxe.first_index_of(self.terms, key_term, prefix_comparator)
        last = BinarySearchDeluxe.last_index_of(self.terms, key_term, prefix_comparator)


        if first == -1 or last == -1:
            return []

        matches = self.terms[first:last + 1]
        return sorted(matches, key=cmp_to_key(Term.compare_by_weight_desc))

    def number_of_matches(self, prefix):
        return len(self.all_matches(prefix))

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
        terms = []
        for _ in range(n):
            line = file.readline().strip().split('\t')
            weight = int(line[0])
            query = line[1]
            terms.append(Term(query, weight))
        return terms


def main():
    filename = input().strip()
    terms = read_file(filename)
    k = int(input().strip())
    autocomplete = Autocomplete(terms)

    while True:
        try:
            prefix = input().strip()
            results = autocomplete.all_matches(prefix)
            print(f"{autocomplete.number_of_matches(prefix)} matches")
            for i in range(min(k, len(results))):
                print(results[i])
        except EOFError:
            break


main()