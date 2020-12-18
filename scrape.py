from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd

source = requests.get('http://blooddonors.in/').text
soup = BeautifulSoup(source,'lxml')
#print(soup)
table = soup.find('div',class_='panel panel-success')
bloodgroup = [ x.get_text() for x in table.find_all('div', class_='col-md-1')]
del bloodgroup[0]
#print(bloodgroup)
data = [ x.get_text() for x in table.find_all('div', class_='col-md-3')]
del data[0]
del data[0]
names = data[::2]
#print(names)
cities = data[1::2]
#print(cities)
df = pd.DataFrame(list(zip(names, bloodgroup,cities)), columns =['Name', 'Blood_Group','City'])
print(len(df)) 
df.to_csv(r'C:\xampp\htdocs\blooddonation\data.csv', index=False, header=False) 
#div = soup.find('table', class_='w3-table w3-bordered w3-striped w3-card-4').text
#cities = div.split('\n')[1:-1]
#print(cities)
#bg = soup.find('select', {'name':'bloodgroup'}).text
#BloodGroup = bg.split('\n')[1:-1]
#print(BloodGroup)
#for i in BloodGroup:
#	for j in cities:
#		url = 'http://blooddonors.in/search.php?city='+j+'bloodgroup='+i+'pageno=1'
#		req = urllib.request.Request(url)
#		response = urllib.request.urlopen(req)
#		html = response.read()
#		soup1 = BeautifulSoup(html, 'html.parser')
#		resultStats = soup1.find_all('div', class_='col-md-3')
#		print(resultStats)
#print(div)