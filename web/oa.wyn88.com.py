import urllib2


url ="http://www.huaqin.com"

#body = urllib2.urlopen(url)
#print body.read()



headers = {}
headers['User-Agent'] = "Googlebot"
print headers

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()
