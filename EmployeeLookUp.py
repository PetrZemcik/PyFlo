employees = [
  {'name':'Samantha Oxford', 'title':'Sr Attorney', 'salary':200000},
  {'name':'Jim Doyle', 'title': 'Jr Engineer', 'salary':85000, 'office':'Atlanta'},
  {'name':'Rebecca Jameson', 'title': 'Sales', 'commision': 2},
  {'name':'Stanley Reed'},
]

def lookup_employee(employees):
    name = input('Employee name: ')
    for employee in employees:
        if 'name' in employee and employee['name'] == name:
            print('Information for ' + name + ':')
            for key in employee:
                print('  ' + key + ': ' + str(employee[key]))
            return
    print('Employee not found')

lookup_employee(employees)