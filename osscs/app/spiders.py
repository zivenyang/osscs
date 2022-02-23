from urllib import parse

import requests

from app.models import MetaObject, PackageListObject, PackageObject, PackageDetailObject
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

    def get_response(self):
        raise NotImplementedError

    def get_query_object(self):
        raise NotImplementedError


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
            return resp
        except requests.exceptions.RequestException as e:
            raise e

    def get_query_object(self):
        resp_json = self.get_response().json()
        meta = MetaObject()
        query_object = PackageListObject()

        # 结果列表为空时下一页标记为False，返回结果为空
        if len(resp_json) == 0:
            meta.is_no_result = True

        # 结果列表长度等于分页长度时，说明有下一页
        if len(resp_json) == self.per_page:
            meta.has_next_page = True
        meta.page = self.page
        meta.per_page = self.per_page
        query_object.meta = meta

        for item in resp_json:
            query_object.package_list.append(PackageObject(item))

        return query_object


class LibrariesProjectAPI(LibrariesAPI):
    def __init__(self, platform, name, page=1, per_page=20):
        super().__init__(page=page, per_page=per_page)
        self.platform = platform
        self.name = name
        self.api = parse.urljoin(LIBRARIES_IO_API_URL, platform + '/' + name)
        self.params = {
            "api_key": self.api_key
        }

    def get_response(self):
        try:
            resp = requests.get(self.api, params=self.params, verify=False)
            return resp
        except requests.exceptions.RequestException as e:
            raise e

    def get_query_object(self):
        resp_json = self.get_response().json()
        PackageDetailObject(resp_json)
        return PackageDetailObject(resp_json)


if __name__ == '__main__':
    spider = LibrariesProjectSearchAPI(q="django", platforms="pypi")
    print(spider.get_query_object())
