a="house"
b=33
c=0.345

#tuple
my_tuple1 = (1, 2 ,3 ,a ,b ,c)
#alternative tuple
my_tuple2 = 1, 2, 3, a, b, c

#list
my_list = [1, 2, 3, "a", 'b', c]

#dictionary
my_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}

#set
my_set = {"apple", "banana", 1323}

#dataframe
my_df = {
  "brand": ["Ford", "Porche", "BMW"],
  "model": ["mustang", "carrera", 320]
}

print ("TUPLE: \n",  my_tuple1, "\n")
print ("LIST: \n", my_list, "\n")
print ("DICTIONARY: \n", my_dictionary, "\n")
print ("SET: \n", my_set, "\n")
print ("DATAFRAME: \n", my_df, "\n")