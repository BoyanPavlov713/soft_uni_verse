employees_by_company = {}

while True:
    data = input()
    if data == 'End':
        break
    args = data.split(' -> ')
    company_name = args[0]
    id_number = args[1]

    if company_name not in employees_by_company:
        employees_by_company[company_name] = []

    if id_number not in employees_by_company[company_name]:
        employees_by_company[company_name].append(id_number)

for company_name, id in employees_by_company.items():
    print(f'{company_name}')
    for employee in id:
        print(f'-- {employee}')
