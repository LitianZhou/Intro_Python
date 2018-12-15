# assignment 12

from ass10 import Employee
from ass11 import Owner

emps = []
owners = []


def set_payroll():
	employees = []
	while True:
		print("Payroll info: enter info of his employee:")
		name = input("Name: ")
		id = input("ID: ")
		employees.append(Employee(name, id))
		employees[-1].set_department(input("Department: "))
		employees[-1].set_job_title(input("Job Title: "))
		more_to_add = input("Does he have more employee in his payroll? Enter Yes or No: ")
		if more_to_add.lower().startswith("no"):
			break
		elif more_to_add.lower().startswith("y"):
			continue
		else:
			print("Unvalid input. Saving and exiting payroll...")
			break
	# append the employee to the main list, avoid repetitive entering
	emps.append(employees[-1])
	return employees


def enter_both():
	while True:
		obj_type = input("Owner or employee? ")
		if obj_type.lower().startswith("own"):
			name = input("Name: ")
			id = input("ID: ")
			dep = input("Department: ")
			job = input("Job Title: ")
			payroll = set_payroll()
			tax = input("Tax rate: ")
			temp_owner = Owner(name, id, payroll,tax)
			temp_owner.set_department(dep)
			temp_owner.set_job_title(job)
			# add to owner list
			owners.append(temp_owner)
		elif obj_type.lower().startswith("employee"):
			name = input("Name: ")
			id = input("ID: ")
			already_enter = False
			for registered_emp in emps:
				if registered_emp.get_id_num() == id:
					already_enter = True
					print("You have entered the info for this employee. Skipping...")
			if not already_enter:
				dep = input("Department: ")
				job = input("Job Title: ")
				temp_emp = Employee(name, id)
				temp_emp.set_department(dep)
				temp_emp.set_job_title(job)
				# add to employee list
				emps.append(temp_emp)
		else:
			print("invalid staff type, please enter again.")
			continue
		more_to_add = input("Do you want to add more staff? Enter Yes or No: ")
		if more_to_add.lower().startswith("n"):
			break


def display():
	for o in owners:
		print("\nOwner\n-----")
		print("Name: " + o.get_name())
		print("ID: " + o.get_id_num())
		print("Department: " + o.get_department())
		print("Job Title: " + o.get_job_title())
		paid_emp = ""
		for p in o.get_payroll():
			paid_emp += p.get_name() + " "
		print("Payroll: " + paid_emp)
		print("Tax: " + o.get_tax_rate())
	for e in emps:
		print("\nEmployee\n--------")
		print("Name: " + e.get_name())
		print("ID: " + e.get_id_num())
		print("Department: " + e.get_department())
		print("Job Title: " + e.get_job_title())


if __name__ == "__main__":
	enter_both()
	display()