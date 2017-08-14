import re

class StrUtility:
	bracket_pattern = re.compile(r'[\[【\(（].*[\]】\)）]')

	emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

	start_puncation_pattern = re.compile(r'^[\.,?"`~\'。，？]+')
	end_puncation_pattern = re.compile(r'[\.?"`~\'。，？]+$')

	@staticmethod
	def remove_str_bracket(str):
		return bracket_pattern.sub('', str)
	
