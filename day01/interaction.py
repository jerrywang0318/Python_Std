#Author Jerry

name = input( "Name:" )
age = input( "Age:")
job = input("Job:")
salary = input("Salary:")

info = ''' -------Info of %s------
Name:%s
Age:%s
Job:%s
Salary:%s
---------------------------------
'''%(name,name,age,job,salary)
print(info)