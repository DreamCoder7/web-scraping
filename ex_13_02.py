from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import urllib.request, urllib.parse, urllib.error
import ssl
import copy

# Ignore the ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url: ")
position = int(input("Enter position: "))
url_list = list()
count = int(input("Enter count: "))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    url_list.append(tag['href'])

print(url)
print(url_list[position - 1])

rep = 1
while rep < count :
    html2 = urllib.request.urlopen(url_list[position - 1], context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')

    url_list = list()

    tags = soup2('a')
    for tag in tags :
        url_list.append(tag['href'])

    print(url_list[position - 1])
    rep = rep + 1

print('Done')


# html = "<a href='link_1'>some other<span>data</span></a>" \
#        "<a href='link_2'>and or</a>" \
#        "<a href='link_3'>some just</a>"
# soup = BeautifulSoup(html, 'html.parser')
#
#
# tags = soup("a")
# for tag in tags :
# print(tag.contents[0])
# print(tag.prettify())
# print(tag.string)
# print('---')


# html_2 = f"""
#     <html>
#         <head>
#             <meta name="description" content="some content" />
#             <title>Test html</title>
#         <head>
#         <body>
#             <header>
#                 <nav>
#                     <ul>
#                         <li>
#                             Home
#                             <a href="link_1">inside link</a>
#                         </li>
#                         <li class="item">
#                             About
#                             <a href="link_2">inside link2</a>
#                         </li>
#                         <li>Contact</li>
#                         <li class="item">Blog</li>
#                     </ul>
#                 </nav>
#
#                 <div>
#                     <a href="link_1">outside link</a>
#                 </div>
#             </header>
#             <main>
#                 <h1>Welcome</>
#                 <p>{soup}</p>
#             </main>
#         </body>
#     </html>
# """
#
# soup_2 = BeautifulSoup(html_2, 'html.parser')
# print(soup_2.head)
# print(soup_2.body)
# print(soup_2.find_all("li"))
# print(soup_2.find_all(href="link_1"))
# print(soup_2.find_all("li", class_="item"))
# print(soup_2.find_all("li", limit=2))
# print(soup_2.select('title'))

# Diagnosing the beautiful file
# print(diagnose(soup_2))

# copying
# c_soup = copy.copy(soup_2)
# print(c_soup.prettify())

# listItemsEl = soup_2("li")
# for item in listItemsEl :
# print(item.contents)
# print(item.parent)
# item.name = "a"
# item['class'] = "link"
# item.append("-items ")
# print(item.name)
# print(item)
# print(item.extract())
# print(item.get_text())
