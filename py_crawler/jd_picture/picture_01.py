import re
import urllib.request as request
import urllib.error as error


def craw(url, page):
    html_1 = request.urlopen(url).read()
    html_1 = str(html_1)
    pat_1 = '<div id="plist" .+? <div class="page clearfix">'
    result_1 = re.compile(pat_1).findall(html_1)
    # print(len(result_1))
    result_2 = result_1[0]
    pat_2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    image_list = re.compile(pat_2).findall(result_2)
    print(len(image_list))
    x = 1
    for image_url in image_list:
        image_name = "D:/ren/mypython/web/picture/" + str(page) + str(x) + ".jpg"
        image_url = "http://" + image_url
        try:
            request.urlretrieve(image_url, filename=image_name)
        except error.URLError as e:
            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1
        x += 1


for i in range(1, 79):
    url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
    craw(url, i)
