# ass 10
import pickle


class Employee():
	def __init__(self, name, id):
		self.name = name
		self.id = id
		self.department = "N.A."
		self.job_title = "N.A."

	def set_department(self, dep):
		self.department = dep

	def set_job_title(self, job_title):
		self.job_title = job_title

	def get_name(self):
		return self.name

	def get_id_num(self):
		return self.id

	def get_department(self):
		return self.department

	def get_job_title(self):
		return self.job_title


def set_employee():
	employees = []
	outfile = open("data.dat", 'wb')
	while True:
		print("Please add info for one employee:")
		name = input("Name: ")
		id = input("ID: ")
		employees.append(Employee(name, id))
		employees[-1].set_department(input("Department: "))
		employees[-1].set_job_title(input("Job Title: "))
		pickle.dump(employees[-1], outfile)
		more_to_add = input("Do you want to add more? Enter Yes or No: ")
		if more_to_add.lower().startswith("n"):
			break
	outfile.close()

	# unpickle and display
	# print the table head first
	print("Name\tID Number\tDepartment\tJob Title\t")

	# load the file and display
	infile = open("data.dat", 'rb')
	end_of_file = False  # To indicate end of file
	while not end_of_file:
		try:
			# Unpickle the next object.
			e = pickle.load(infile)
			print(e.get_name() + '\t' + e.get_id_num() + '\t' + e.get_department() + '\t' + e.get_job_title() + '\t')
		except EOFError:
			# of the file has been reached.
			end_of_file = True

	# Close the file.
	infile.close()


if __name__ == "__main__":
	set_employee()
