#Test for urllib with python


import urllib2

response = urllib2.urlopen('http://pdupc-codereview.mo.sw.ericsson.se:9988/')
html = response.read()
print html
