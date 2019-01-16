# Program that takes chemical equations and balances them

class Formula():
	"""Class that manipulates input chemical formulas"""
	
	def __init__(self, formula):
		"""initializes formula and blank coefficient"""
		self.formula = formula
		self.coeff = ''
		
	def increase_coeff(self):
		"""increases coefficient by 1"""
		self.coeff += 1
		
	def formula_dict(self):
		"""takes the formula and creates a dictionary of elements a values
		input: string of each formula
		output: dictionary """
		
		
	
		
	

def balance():
	"""Takes chemical formulas of molecules from the user,
	balances the equation, and returns the balanced chemical equation
	
	Input: molecule strings in the format H2O or Al2O3
	"""
	
	print("Reactants and products need to be entered in the following format:")
	print("Water is H2O. Aluminum oxide is Al2O3\n")
	
	
	# ~ #User provides reactants
	# ~ reactants, products = [], []
	# ~ while True:
		# ~ reactant = input("Please input reactant. Input 'n' when finished. ")
		# ~ if reactant == 'n':
			# ~ break
		# ~ reactants.append(reactant)
	# ~ #User provides products
	# ~ while True:
		# ~ product = input("Please input product. Input 'n' when finished. ")
		# ~ if product == 'n':
			# ~ break
		# ~ products.append(product)
	
	reactants = ['Mg', 'O2']
	products = ['MgO']
	
	for item in reactants:
		reactants.append(Formula(item))
		
	


if __name__ == '__main__':
	balance()
