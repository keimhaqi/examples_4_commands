import urllib2

url = "http://www.saksfifthavenue.com/main/ProductDetail.jsp?PRODUCT%3C%3Eprd_id=845524447058525"

req = urllib2.Request(url)

response = urllib2.urlopen(req)

print(response)