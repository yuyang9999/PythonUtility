import re




class StrUtility:
	bracket_pattern = re.compile(r'[\[【\(（].*[\]】\)）]')

	emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

	start_puncation_pattern = re.compile(r'^[.]')
	
	@staticmethod
	def remove_str_bracket(str):
		return bracket_pattern.sub('', str)
	

	@staticmethod
	def strQ2B(ustring):
	    rstring = ""
	    for uchar in ustring:
	        inside_code=ord(uchar)
	        if inside_code==0x3000:
	            inside_code=0x0020
	        else:
	            inside_code-=0xfee0
	        if inside_code<0x0020 or inside_code>0x7e:      #转完之后不是半角字符返回原来的字符
	            rstring += uchar
	        rstring += unichr(inside_code)
	    return rstring


	@staticmethod
	def strB2Q(ustring):
	    rstring = ""
	    for uchar in ustring:
	        inside_code=ord(uchar)
	        if inside_code<0x0020 or inside_code>0x7e:      #不是半角字符就返回原来的字符
	            rstring += uchar
	        if inside_code==0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0
	            inside_code=0x3000
	        else:
	            inside_code+=0xfee0
	        rstring += unichr(inside_code)
	    return rstring