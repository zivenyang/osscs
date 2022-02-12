from django.http import JsonResponse
from django.shortcuts import render, redirect
from app.form import SearchForm


# Create your views here.
from app.spiders import PackageSpider


def search(request):
    """
    接收前端查询页面发送的GET请求，通过ossType选择仓库类型，
    然后发送到对应仓库的查询页，通过爬虫解析页面数据后响应给前台页面，产生查询列表
    """
    q = request.GET.get('q')
    oss_type = request.GET.get('ossType')

    # 爬取官网的爬虫页面
    data = PackageSpider(oss_type=oss_type, q=q).parse_response()

    return JsonResponse(data)

