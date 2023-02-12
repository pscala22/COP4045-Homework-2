#Python Program for given problem
#Imported some common librabries
import sys
import re
import os

#Parse Function which takes an file as parameter
def parse_functions(file_name):
    result_tuple = ()
    func_code = ''
    flag=0
    file = open(file_name,'r')
    lines = file.readlines() #read file line by line
    line_num = 0
    for line in lines:
        line_num+=1
        if line == '\n': #next line if the line is blank
            continue

        comment = re.search('(^#)\w*',line) #Checks that the line is comment
        if comment:
            continue    

        match = re.search('(^def)\s+([_a-zA-Z]+\w*)',line) # function definiton check
        if match:
            func_code = line.split("#")[0].strip()
            func_name = (match.groups()[1])
            func_line = (line_num)
            flag = 1
            continue
        else:
            func_code = func_code + line.split("#")[0].strip() #function code

        if flag ==1:
            res_tuple = (func_name,func_line,func_code)
            result_tuple = result_tuple+(res_tuple,) #append each function in tuple of tuples
            code_line = ""
            flag =0


    return result_tuple # return tuple
results = parse_functions("funs.py") #Call function
print(results) #Print result tuple