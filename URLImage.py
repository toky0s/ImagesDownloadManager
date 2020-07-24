from XImage import XImage
import requests
import json
from bs4 import BeautifulSoup
from XImage import XImage, UnsplashXImage
from urllib.request import urlretrieve
import re


class URLImage:
    """Abstract class này đại diện là một trình tìm kiếm URL của ảnh.
    Class kế thừa class này buộc phải triển khai phương thức getURLs trả về một list các XImage Object"""

    def __init__(self):
        json_info = ''

    def getXImages(self) -> list:
        """Class implement method này phải trả về một list các XImage tìm thấy dựa trên query đưa vào."""
        pass

    def list2XImage(self, item) -> XImage :
        """Method này trả về một XImage Object, bạn có thể implement hoặc không."""
        pass


class UnsplashURLImage(URLImage):

    SEARCH = 'https://unsplash.com/napi/search/photos'

    RAW = 'raw'
    FULL = 'full'
    REGULAR = 'regular'
    SMALL = 'small'
    THUMB = 'thumb'

    def __init__(self, query, perpage, page, quality='regular', order='latest'):
        super().__init__()
        self.query = query
        self.perpage= perpage
        self.page = page
        self.quality = quality
        self.order = order

    def getXImages(self):
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
        params = {'query': self.query, 'page': self.page, 'per_page': self.perpage}
        r = requests.get(UnsplashURLImage.SEARCH, params=params)
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
                id_ = i['id']
                url = i['urls'][self.quality]
                created_at = i['created_at']
                updated_at = i['updated_at']
                promoted_at = i['promoted_at']
                width = i['width']
                height = i['height']
                description = i['description']

                ximage = UnsplashXImage(url, id_, created_at, updated_at, promoted_at, width, height, description)
                results.append(ximage)
        return results


class GratisographyURlImage(URLImage):

    def __init__(self, query, page):
        super().__init__()
        self.query = query
        self.page = page

    
    def matchSinglePhoto(self, tag):
        return tag.has_attr('class') and tag.has_attr('id') and tag.name == u'article'
    
    def getXImages(self):
        """
        Hàm này nhận vào một `query` và trả về một list các XImage dựa theo query đầu vào. Tham số  `page`
        là tùy chọn hàm sẽ get tới page nào. Mặc định get page đầu tiên (page=1). Nếu tham số này vượt quá số page hiện có, mặc định lấy tối đa.

        :pattern: https://gratisography.com/page/1/?s=cat
        """
        result = []

        params = {'s': self.query}
        for i in range(1, self.page+1):
            r = requests.get('https://gratisography.com/page/1', params=params)
            soup = BeautifulSoup(r.text, 'lxml')
            list_imgs = soup.find_all('img')
            result = [i['src'] for i in list_imgs if '.jpg' in i['src']]
                
        return result


a = GratisographyURlImage('cat',5)
b = a.getXImages()
print(b)
