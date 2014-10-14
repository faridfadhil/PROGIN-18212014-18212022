import xml.dom.minidom
import urllib
import time
usock = urllib.urlopen('http://rss.detik.com/')
dom = xml.dom.minidom.parse(usock)
Item = dom.getElementsByTagName('item')
usock.close()
i = 0
for node in Item:
    alist=node.getElementsByTagName('title')
    for a in alist:
        Title= a.firstChild.data
        print Title
        
    alist=node.getElementsByTagName('pubDate')
    for a in alist:
        pubDate = a.firstChild.data
        print 'Publish On : '+pubDate
        
    alist=node.getElementsByTagName('description')
    for a in alist:
        des = a.firstChild.data
        print des
        
    alist=node.getElementsByTagName('link')
    for a in alist:
        Link= a.firstChild.data
        print 'Link Berita : '+Link
        print ''
        


## 24 hour format ##
hour=time.strftime("%H:%M:%S")
print ''
print ''
print '============== Menampilkan Berita 1 Jam Terakhir ============'

for node in Item:
	alist = node.getElementsByTagName('pubDate')
	for a in alist:
		Date = a.firstChild.data[0:25]
		pubTime = time.strptime(Date, '%a, %d %b %Y %H:%M:%S')
		nowTime = time.localtime(time.time())
		pubTime = time.mktime(pubTime)
		nowTime = time.mktime(nowTime)
		diffTime = (nowTime - pubTime)
		print diffTime
		if (diffTime <= 3600):	 
			alist=node.getElementsByTagName('title')
			for a in alist:
				Title= a.firstChild.data
				print Title
				
			alist=node.getElementsByTagName('pubDate')
			for a in alist:
				pubDate = a.firstChild.data
				print 'Publish On : '+pubDate
				
			alist=node.getElementsByTagName('description')
			for a in alist:
				des = a.firstChild.data
				print des
				
			alist=node.getElementsByTagName('link')
			for a in alist:
				Link= a.firstChild.data
				print 'Link Berita : '+Link
				print ''
		
	
	
	
