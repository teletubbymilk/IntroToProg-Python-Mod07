# ------------------------------------------------- #
# Title: <Type the name of the script here>
# Description: <Type a description of the script>
# ChangeLog: (Who, When, What)
# <Example Dev,01/01/2030,Created Script>
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

'''pickling'''
customer_id = int(input("Enter an Id: "))
customer_name = str(input("Enter an name: "))
customer_list = [customer_id, customer_name]
print(customer_list)

#now we store the data with the dump
objFile = open("AppData.dat", "ab")
pickle.dump(customer_list, objFile)
objFile.close()

#read the data back with the load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)

'''error handling'''
try:
    file = open("AppData.dap","rb")
    print(file)
except:
    print("whooops something went wrong :/")

try:
    file = open("AppData.dap", "rb")
    print(file)
except Exception as e:
    print("whooops something went wrong :/")
    print("Built-In pythons error info: ")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())

try:
    file = open("AppData.dap", "rb")
    print(file)
except FileNotFoundError as e:
    print("Please enter an existing file")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("whooops something went wrong :/")
    print(e, e.__doc__, type(e), sep='\n')