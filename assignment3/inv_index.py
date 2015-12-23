import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: book
    # value:text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in set(words):
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence books
    '''
    total = 0
    for v in list_of_values:
      total += v
    '''
    mr.emit((key, list_of_values))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
