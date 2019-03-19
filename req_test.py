from lxml import etree


# import requests
#
#
# url = "https://www.amocrm.ru/"
#
# page = requests.get(url)


with open(r"D:\temp\content.html", "rb") as f:
    content = f.read()

parser = etree.HTMLParser()
tree = etree.fromstring(content.decode("utf-8"), parser)

for a in tree.findall('.//a[@href]'):
    print(a.attrib["href"], a.text)
