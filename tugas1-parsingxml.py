import xml.dom.minidom
import urllib
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
