from urllib.request import urlopen
from urllib.request import Request 


def get_response_content_for_url(url, decode='utf8'):
	"""return value (succeed(boolean), contnet(string))"""
	hdr = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive'}

	request = Request(url, headers=hdr)
	try:
		resp = urlopen(request)
		content = resp.read().decode(decode)
	except:
		return False, ''

	return True, content


