import re

class StrUtility:
	bracket_reg = re.compile(r'[\[【\(（].*[\]】\)）]')

	@staticmethod
	def remove_str_bracket(str):
		return StrUtility.bracket_reg.sub('', str)
	


