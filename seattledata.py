# Python 3

import urllib.request, json
url = 'https://data.seattle.gov/resource/tmmm-ytt6.json'
response = urllib.request.urlopen(url)
rawcheckout = json.loads(response.read())
print(json.dumps(rawcheckout, indent=4, sort_keys=True))
print(rawcheckout[1])

sx=[]
sy=[]
books = []
for book in rawcheckout:
    sx.append(int(book['checkoutmonth']))
    sy.append(int(book['checkouts']))
    books.append(book['title'])


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(sx,sy,  c='r', marker="o", label='Month of checkout vs Number of checkouts')
plt.legend(loc='upper left');
plt.show()
