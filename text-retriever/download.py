import requests
import sys

from bs4 import BeautifulSoup, NavigableString


def unstyle_html(html):
    soup = BeautifulSoup(html, features='html.parser')

    for tag in soup.descendants:
        keys = []
        if not isinstance(tag, NavigableString):
            for k in tag.attrs.keys():
                if k not in ['src', 'href']:
                    keys.append(k)
            for k in keys:
                del tag[k]

    for tag in soup.find_all(['script', 'style']):
        tag.decompose()

    return soup.prettify()

#url = "https://ai.googleblog.com/2022/03/multimodal-bottleneck-transformer-mbt.html"

url = sys.argv[1]
response = requests.get(url)
clean = unstyle_html(response.text)
print(clean)
