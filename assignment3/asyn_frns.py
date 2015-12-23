import MapReduce
import sys

"""
Asym frndship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    person1 = record[0]
    person2 = record[1]
    
    t_list = []
    t_list.append(person1)
    t_list.append(person2)
    t_list.sort()
    mr.emit_intermediate(str(t_list[0]+'_'+str(t_list[1])), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) != 2:
	rlshp = key.split('_')
        print len(rlshp) 
	mr.emit((rlshp[0], rlshp[1]))
	mr.emit((rlshp[1], rlshp[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
