import requests
import re

to_crawl = ['http://solyd.com.br']
crawled = set()
emails_found = set()

for i in range(15):

    url = to_crawl[0]
    try:
        req = requests.get(to_crawl[0])
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\']*)', html)
    print('Crawling: ', url)

    emails = re.findall(r'[\w\._-]+@[\w_-]+\.[\w\._-]+\w', html)

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)

    for email in emails:
        emails_found.add(email)
        print(f'Email Found: {email}')

print(crawled)
print(emails_found)