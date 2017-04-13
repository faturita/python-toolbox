import urllib, json
url = 'https://data.seattle.gov/api/views/jbb5-9wmt/rows.json?accessType=DOWNLOAD'
response = urllib.urlopen(url)
rawschools = json.loads(response.read())
print json.dumps(rawschools, indent=4, sort_keys=True)
rawschools['data'][1]

sx=[]
sy=[]
schools = []
for school in rawschools['data']:
    sx.append(float(school[11][2]))
    sy.append(float(school[11][1]))
    geo=[float(school[11][1]), float(school[11][2])]
    schools.append(geo)
    print geo

url2='https://data.seattle.gov/api/views/b9ut-byji/rows.json?accessType=DOWNLOAD'
response = urllib.urlopen(url2)
publictoilet = json.loads(response.read())
print json.dumps(publictoilet, indent=4, sort_keys=True)

toilets = []
x=[]
y=[]
for toilet in publictoilet['data']:
    x.append(float(toilet[12]))
    y.append(float(toilet[13]))
    geo=[float(toilet[12]), float(toilet[13])]
    toilets.append(geo)
    print geo

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, s=10, c='b', marker="x", label='Toilets')
ax1.scatter(sx,sy, s=10, c='r', marker="o", label='Schools!')
plt.legend(loc='upper left');
plt.show()
