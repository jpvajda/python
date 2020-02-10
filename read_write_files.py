# r = read
# w = write  (overwrites file)
# a = append (adds to file)
# r+ = read & write

# reading a file 

employee_file = open('python/python/employees.txt', 'r')

for employee in employee_file.readlines(): 
    print(employee)

employee_file.close()

# writing (overwrite) to an existing file 

employee_file = open('python/python/employees.txt', 'w')

employee_file.write('\nKelly = Support')

# read write function 

employee_file.close()

# appending (adding) an existing file 

employee_file = open('python/python/employees.txt', 'a')

employee_file.write('\nKelly = Support')

employee_file.close()

# create a new file 

employee_file = open('python/python/newfile.txt', 'w')

employee_file.write('\nthis is a new file!')

employee_file.close()