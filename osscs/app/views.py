from django.http import JsonResponse

from app.spiders import LibrariesProjectSearchAPI, LibrariesProjectAPI


# Create your views here.


def search(request):
    """
    接收前端查询页面发送的GET请求，通过ossType选择仓库类型，
    然后发送到对应仓库的查询页，通过爬虫解析页面数据后响应给前台页面，产生查询列表
    """
    q = request.GET.get('q')
    platforms = request.GET.get('platforms').lower()
    page = int(request.GET.get('page'))
    per_page = int(request.GET.get('perPage'))

    # 爬取官网的爬虫页面
    data = LibrariesProjectSearchAPI(platforms=platforms, q=q, page=page, per_page=per_page).parse_response()

    return JsonResponse(data)


def detail(request, **kwargs):
    """
    包详情页面
    :param request:
    :return:
    """
    platform = kwargs.get("platform").lower()
    name = kwargs.get("name")
    data = LibrariesProjectAPI(platform=platform, name=name).parse_response()
    return JsonResponse(data)
