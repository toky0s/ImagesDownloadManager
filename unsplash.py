"""
Unsplash API
~~~~~~~~~~~~
This module contains functions which can return a list contains urls which you can download.
"""

import requests
import json
from bs4 import BeautifulSoup
from XImage import XImage
from urllib.request import urlretrieve

SEARCH = 'https://unsplash.com/napi/search/photos'
RANDOM = 'https://unsplash.com/napi/photos/random'

RAW = 'raw'
FULL = 'full'
REGULAR = 'regular'
SMALL = 'small'
THUMB = 'thumb'


def UnsplashCheckQuery(query) -> list:
    """
    Hàm này trả về một list chưa hai giá trị là:

    `total`: Là số lượng ảnh có liên quan tới `query`.

    `total_pages`: Là số lượng trang chứa.
    """
    params = {'query': query}
    r = requests.get(SEARCH, params)
    j = json.loads(r.text)
    return [j['total'], j['total_pages']]


def UnsplashAPISearch(query, page, per_page, quality) -> list:
    """
    Hàm này trả về một list các XImage chứa thông tin cần thiết của một bức ảnh.
    Thứ mà sau đó có thể dùng để tải về. Tối đa 30 XImage.

    @param:

    `query`: str, chứa ảnh muốn tìm kiếm. Số lượng ảnh cho mỗi query là khác nhau. Khi query không tìm thấy, hàm trả về một list rỗng.

    `page`: int, số trang mà hàm sẽ bắt đầu get. Số lượng ảnh sẽ được phân bố trên các trang này. Đồng nghĩa với việc
    mỗi query sẽ tương ứng với một số lượng page cố định. Khi page vượt qua con số này, hàm trả về một list rỗng.

    `per_page`: int, số lượng ảnh mà bạn sẽ lấy về (tối đa 30).

    `quality`: str, chất lượng ảnh của một XImage, có năm tùy chọn là: raw, full, regular, small. thumb.

    @example:

    >>> ximages = UnsplashAPISearch('cat', 10, 12, REGULAR)
    >>> ximages[0].getName()
    >>> 'YifPTBCy-x8'
    >>> ximages[0].getUrl()
    >>> 'https://images.unsplash.com/photo-1496661269814-a841e78df103?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9'
    """
    results = []
    params = {'query': query, 'page': page, 'per_page': per_page}
    r = requests.get(SEARCH, params=params)
    if r.status_code == 200:
        # get urls based on quality
        j = json.loads(r.text)
        if j['total'] == 0:
            return results
        # get list images
        page_results = j['results']
        if page_results == []:
            return results
        for i in page_results:
            name = i['id']
            url = i['urls'][quality]
            ximage = XImage(name, url, i)
            results.append(ximage)
    return results


def UnsplashAPIRandom(amount, quality):
    """
    Hàm này trả về một list chứa các XImage được get ngẫu nhiên từ Unsplash. Tối đa 30 XImage.
    """
    results = []
    params = {'count': amount}
    r = requests.get(RANDOM, params=params)
    if r.status_code == 200:
        j = json.loads(r.text)
        for i in j:
            name = i['id']
            url = i['urls'][quality]
            ximage = XImage(name, url, i)
            results.append(ximage)
    return results


def GratisographyAPISearch(query, page):
    """
    Hàm này nhận vào một `query` và trả về một list các XImage dựa theo query đầu vào. Tham số  `page`
    là tùy chọn hàm sẽ get tới page nào. Mặc định get page đầu tiên (page=1). Nếu tham số này vượt quá số page hiện có, mặc định lấy tối đa.

    :pattern: https://gratisography.com/page/1/?s=cat
    """
    result = []

    def matchSinglePhoto(tag):
        return tag.has_attr('class') and tag.has_attr('id') and tag.name == u'article'

    params = {'s': query}
    for i in range(1, page+1):
        r = requests.get('https://gratisography.com/page/1', params=params)
        soup = BeautifulSoup(r.text, 'lxml')
        articles = soup.find_all(matchSinglePhoto)
        for tag in articles:
            url_iamge = tag.div.a['href']
            url_iamge_r = requests.get(url_iamge)
            soup_url_image = BeautifulSoup(url_iamge_r.text, 'lxml')
            download_buttons = soup_url_image.find(class_='download-buttons')
            url = download_buttons.a['href']

            name = url.split('/')[-1][0:-4]
            ximage = XImage(name, url)
            result.append(ximage)
    return result


def PixabayAPISearch(query, page):
    ENG = 'https://picjumbo.com/search/cat'
    r = requests.get(ENG)
    soup = BeautifulSoup(r.text,'lxml')
    thumb_urls = soup.find_all(class_='tri_img_one')
    for div in thumb_urls:

        if 'picjumbo.com' in div.a['href']:
            print(div.a['href'])
    return None


if __name__ == "__main__":
    # ximages = UnsplashAPIRandom(12, REGULAR)
    # print(ximages[0].getName())
    # print(ximages[0].getUrl())

    # print(GratisographyAPISearch('trees',1)[0].getName())
    PixabayAPISearch('cat', 'ok')
    # urlretrieve('https://picjumbo.com/download/?d=cow.jpg&n=cow&id=1','D:\ok.jpg')
