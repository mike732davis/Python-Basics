employees=[
    {'name':'Mike Davis', 'age':22, 'salary':20000},
    {'name':'John', 'age':21, 'salary':10000},
    {'name':'Syed Ahamed', 'age':25, 'salary':25000},
    {'name':'Joseph', 'age':19, 'salary':8000},
    {'name':'Micheal', 'age':30, 'salary':120000}
    ]
'''a=sorted(employees,key=lambda item:item['name'])
print("sorted by name:\n" +str(a))
print("\n")
b=sorted(employees,key=lambda item:item['age'])
print("sorted by age:\n" +str(b))
print("\n")'''
c=sorted(employees,key=lambda item:item['salary'],reverse=True)
print("sorted by salary:\n" +str(c))