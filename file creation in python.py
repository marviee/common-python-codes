

employee= open("employee.txt", "r")
'''for ee in employee.readlines()[5:]:
 #   employee=open("employee.txt","a")

  #  employee.write("\ni really love ife")
  #  #print(ee)
'''
print(employee.readable())
employee=open("employee.txt", "r")
if employee.readable():
    print("its now readable")
else:
    print("not readable")

print(employee.readlines())

employee.close()

