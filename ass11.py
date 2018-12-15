# assignment 11

from ass10 import Employee


class Owner(Employee):
	def __init__(self, name, id, emps=[], percent=0.01):
		Employee.__init__(self, name, id)
		self.emps = emps
		self.percent = str(percent)

	def add_to_payroll(self, emp):
		self.emps.append(emp)

	def remove_from_payroll(self, emp):
		self.emps.remove(emp)

	def is_on_payroll(self, emp):
		return emp in self.emps

	def get_payroll(self):
		return self.emps

	def set_tax_rate(self, percent):
		self.percent = percent

	def get_tax_rate(self):
		return self.percent

	def __str__(self):
		payroll = ""
		for emp in self.emps:
			payroll += emp.get_name()+ ' '+ emp.get_id_num() + '\n'
		return "Owner: " + self.get_name()+" " + self.get_id_num()+'\n' + "payroll: \n" + payroll + "tax rate: " + self.percent


def main():
	sam = Employee("Sam", "2")
	me = Owner("Lee", "1", [sam, Employee("Tom", "3")], "0.03")
	me.add_to_payroll(Employee("Mary", '4'))
	print(me.get_payroll())
	print(me.get_tax_rate())
	me.set_tax_rate(input("tax rate: "))
	print("Sam is on the payroll: " + str(me.is_on_payroll(sam)))

	# test str function:
	print(me)


if __name__ == "__main__":
	main()