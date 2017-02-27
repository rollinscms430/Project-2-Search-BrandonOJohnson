def build_dict():
    # Load in word file and sort each line.
    alpha = {}
    f = open('words.txt', "r")
    for line in f.readlines():
        line = line.strip()
        key = sorted_line(line)

        # Add each line to a dictionary based on its sorted key.
        if key in alpha:
            alpha[key].append(line)
            
        else:
            alpha[key] = []
            alpha[key].append(line)
            
    return alpha

def sorted_line(line):
    # Sort the chars in this line and return a string.
   sortedlist = sorted(line)
   sortedtuple = tuple(sortedlist)
   return sortedtuple

def anagram(alpha):
   
   for key in alpha:

       if len(alpha[key]) > 1:
           print alpha[key]
  
     
     
dictionary = build_dict()   
anagram(dictionary)
       

       
       
   
   
   
   
   
   
   
   
   
   
   
   
