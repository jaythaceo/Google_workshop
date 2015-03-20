import urllib

u = urllib.urlopen("https://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&user_id=31065906@N08&api_key=143483c7577caf2ca98332d1f0ce4869")
data = u.read()
f = open('flicker.xml', 'wb')
f.write(data)
f.close()
print('Wrote flicker.xml')