from datetime import datetime
from urllib import parse

import requests
from bs4 import BeautifulSoup

from app.serializers import PypiPackageSerializer, BasePackageListSerializer
from const.const import MVN_REPOSITORY_PACKAGE_SEARCH_URL, MAVEN, PYPI, \
    PYPI_REPOSITORY_PACKAGE_SEARCH_URL, PYPI_REPOSITORY_URL


class Spider:
    def __init__(self, oss_type, q=None, url=None):
        self.oss_type = oss_type
        self.q = q
        self.url = url


class PackageSpider(Spider):
    def __init__(self, oss_type, q=None, url=None):
        super().__init__(oss_type, q, url)
        self.url = url if url else self.get_url()
        self.response = self.request_page()

    def get_url(self):
        if self.oss_type == MAVEN:
            url = MVN_REPOSITORY_PACKAGE_SEARCH_URL
        elif self.oss_type == PYPI:
            url = PYPI_REPOSITORY_PACKAGE_SEARCH_URL
        else:
            raise ValueError("oss_type not true!")
        return url

    def request_page(self):
        if self.oss_type == MAVEN:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'Cookie': '__cfduid=db73a1a3b63a54e86f435f615f5ec37791562300679; _ga=GA1.2.1048718546.1562300686; _gid=GA1.2.312498482.1562300686',
                'Accept': '*/*', 'Accept-Encoding': 'gzip',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,mt;q=0.6'
            }

            if self.q:
                params = {
                    "q": self.q
                }
                resp = requests.get(self.url, params=params, headers=headers, verify=False)
            else:
                resp = requests.get(self.url, headers=headers, verify=False)
        elif self.oss_type == PYPI:
            if self.q:
                params = {
                    "q": self.q
                }
                resp = requests.get(self.url, params=params, verify=False)
            else:
                resp = requests.get(self.url, verify=False)
        else:
            raise
        return resp.text

    def parse_response(self):
        package_list_obj = BasePackageListSerializer()

        if self.oss_type == PYPI:
            return pypi_response_parser(self.response, package_list_obj)
        else:
            raise


def pypi_response_parser(resp, package_list_obj: BasePackageListSerializer()):
    package_obj = PypiPackageSerializer()
    soup = BeautifulSoup(resp, 'lxml')

    # 获取搜索结果中的li标签列表
    search_results_list = soup.select('ul[aria-label="Search results"] li a')
    for item in search_results_list:
        # 遍历每个li标签中子元素，获得需要的包信息
        """
        <a class="package-snippet" href="/project/django/">
        <h3 class="package-snippet__title">
        <span class="package-snippet__name">Django</span>
        <span class="package-snippet__version">4.0.2</span>
        <span class="package-snippet__released"><time data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" datetime="2022-02-01T07:56:23+0000">
          Feb 1, 2022
        </time></span>
        </h3>
        <p class="package-snippet__description">A high-level Python web framework that encourages rapid development and clean, pragmatic design.</p>
        </a>
        """
        package_obj.package_url = parse.urljoin(PYPI_REPOSITORY_URL, item.attrs["href"])
        package_obj.package_name = item.select('h3 .package-snippet__name')[0].get_text()
        package_obj.package_description = item.select('p.package-snippet__description')[0].get_text()
        package_obj.package_version = item.select('h3 .package-snippet__version')[0].get_text()
        package_obj.package_released = datetime.strptime(
            item.select('h3 .package-snippet__released time')[0].attrs["datetime"], "%Y-%m-%dT%H:%M:%S+%f")
        package_list_obj.package_list.append(package_obj.to_dict())

    # 获取下一页的url
    next_page_tag = soup.select('.button-group--pagination a:last-child')
    if len(next_page_tag) != 0 and next_page_tag[0].get_text() == "Next" and "button--disabled" not in \
            next_page_tag[0].attrs["class"]:
        next_page_url = next_page_tag[0].get("href")
        package_list_obj.next_page = parse.urljoin(PYPI_REPOSITORY_URL, next_page_url)
    return package_list_obj.to_dict()


if __name__ == '__main__':
    spider = PackageSpider("pypi", url="https://pypi.org/search/?o=&q=django&page=500")
    print(spider.parse_response())
