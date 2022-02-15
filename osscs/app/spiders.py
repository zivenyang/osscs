from urllib import parse

import requests

from app.serializers import PackageListSerializer, MetaSerializer, PackageSerializer, PackageDetailSerializer
from const.const import LIBRARIES_IO_PROJECT_SEARCH_API_URL, LIBRARIES_IO_API_URL
from const.security import LIBRARIES_IO_API_KEY


class LibrariesAPI(object):
    """
    使用https://libraries.io/api提供的接口获取包数据
    """

    def __init__(self, api_key=None, page=1, per_page=20):
        self.api_key = api_key if api_key else LIBRARIES_IO_API_KEY
        self.page = page
        self.per_page = per_page


class LibrariesProjectSearchAPI(LibrariesAPI):
    """
    Project Search API
    用于搜索相关软件包
    """

    def __init__(self, q, platforms, languages=None, licenses=None, keywords=None, sort=None, page=1, per_page=20):
        super().__init__(page=page, per_page=per_page)
        # self.page = page if page else self.page
        # self.per_page = per_page if per_page else self.per_page
        self.api = LIBRARIES_IO_PROJECT_SEARCH_API_URL
        self.params = {
            "api_key": self.api_key,
            "q": q,
            "platforms": platforms,
            "languages": languages,
            "licenses": licenses,
            "keywords": keywords,
            "sort": sort,
            "page": self.page,
            "per_page": self.per_page
        }

    def get_response(self):
        try:
            resp = requests.get(self.api, params=self.params, verify=False)
            return resp.json()
        except requests.exceptions.RequestException as e:
            raise e

    def parse_response(self):
        resp_json = self.get_response()
        data = PackageListSerializer()
        meta = MetaSerializer()

        # 结果列表为空时下一页标记为False，返回结果为空
        if len(resp_json) == 0:
            meta.is_no_result = True

        # 结果列表长度等于分页长度时，说明有下一页
        if len(resp_json) == self.per_page:
            meta.has_next_page = True
        meta.page = self.page
        meta.per_page = self.per_page
        data.meta = meta.to_dict()

        for item in resp_json:
            data.package_list.append(PackageSerializer(item).to_dict())

        return data.to_dict()


class LibrariesProjectAPI(LibrariesAPI):
    def __init__(self, platform, name, page=1, per_page=20):
        super().__init__(page=page, per_page=per_page)
        self.platform = platform
        self.name = name
        self.api = parse.urljoin(LIBRARIES_IO_API_URL, platform+'/'+name)
        self.params = {
            "api_key": self.api_key
        }

    def get_response(self):
        try:
            resp = requests.get(self.api, params=self.params, verify=False)
            return resp.json()
        except requests.exceptions.RequestException as e:
            raise e

    def parse_response(self):
        resp_json = self.get_response()
        return PackageDetailSerializer(resp_json).to_dict()


if __name__ == '__main__':
    spider = LibrariesProjectAPI(platform="npm", name="base62")
    print(spider.parse_response())
