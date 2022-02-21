from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.serializers import PackageListSerializer, PackageDetailSerializer
from app.spiders import LibrariesProjectSearchAPI, LibrariesProjectAPI
from utils.filters import is_valid_param


class PackageList(GenericAPIView):
    serializer_class = PackageListSerializer

    def get_queryset(self):
        q = self.request.query_params.get('q')
        platforms = self.request.query_params.get('platforms').lower()
        page = int(self.request.query_params.get('page'))
        per_page = int(self.request.query_params.get('perPage'))
        return LibrariesProjectSearchAPI(platforms=platforms, q=q, page=page, per_page=per_page).get_query_object()

    @extend_schema(
        summary='包查询接口',
        description="接收前端查询页面发送的GET请求，通过platforms选择仓库类型，\
        然后发送到libraries.io的查询接口，解析页面数据后响应给前台页面，产生查询列表和页面元数据",
        parameters=[
            OpenApiParameter(name='q',
                             location=OpenApiParameter.QUERY,
                             description='搜索内容',
                             required=True,
                             type=str,
                             examples=[
                                 OpenApiExample(
                                     'Example 1',
                                     summary='django',
                                     description='查询所有与django相关的包',
                                     value='django'
                                 ),
                             ],
                             ),
            OpenApiParameter(
                name='platforms',
                location=OpenApiParameter.QUERY,
                description='包管理平台名称',
                required=True,
                type=str,
                examples=[
                    OpenApiExample(
                        'Example 1',
                        summary='pypi',
                        description='python的包管理平台',
                        value='pypi'
                    ),
                ],
            ),
            OpenApiParameter(
                name='page',
                location=OpenApiParameter.QUERY,
                description='当前页码',
                required=True,
                type=int,
                default=1
            ),
            OpenApiParameter(
                name='perPage',
                location=OpenApiParameter.QUERY,
                description='每页条数',
                required=True,
                type=int,
                default=20,
            ),
        ],
    )
    def get(self, request):
        # 1.查询数据
        queryset = self.get_queryset()
        # 2.创建序列化器，并传递查询结果集
        serializer = self.get_serializer(queryset)
        # 3.返回响应 serializer.data
        return Response(serializer.data)


class PackageDetail(GenericAPIView):
    serializer_class = PackageDetailSerializer

    def get_queryset(self):
        platform = ''.join(filter(str.isalpha, self.kwargs.get('platform')))
        name = ''.join(filter(is_valid_param, self.kwargs.get('name')))
        return LibrariesProjectAPI(platform=platform, name=name).get_query_object()

    @extend_schema(
        summary='包详情接口',
        description='返回具体包的详情信息',
        parameters=[
            OpenApiParameter(name='platform',
                             location=OpenApiParameter.PATH,
                             description='包管理平台名称',
                             required=True,
                             type=str,
                             examples=[
                                 OpenApiExample(
                                     'Example 1',
                                     summary='pypi',
                                     description='python的包管理平台',
                                     value='pypi'
                                 ),
                             ],
                             ),
            OpenApiParameter(
                name='name',
                location=OpenApiParameter.PATH,
                description='包名称',
                required=True,
                type=str,
                examples=[
                    OpenApiExample(
                        'Example 1',
                        summary='django',
                        description='查询django的详情',
                        value='django'
                    ),
                ],
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        # 1.查询数据
        queryset = self.get_queryset()
        # 2.创建序列化器，并传递查询结果集
        serializer = self.get_serializer(queryset)
        # 3.返回响应 serializer.data
        return Response(serializer.data)
