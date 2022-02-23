import graphene
from graphene import ObjectType

from app.scalars import CustomDateTime


class VersionType(ObjectType):
    number = graphene.String(description="版本号")
    published_at = CustomDateTime(description="发布时间")
    spdx_expression = graphene.String()
    original_license = graphene.String()
    researched_at = CustomDateTime()
    repository_sources = graphene.List(graphene.String)

    class Meta:
        description = "版本信息类型，用于存储包的所有版本信息"


class PackageType(ObjectType):
    dependent_repos_count = graphene.Int(description="依赖该包的代码仓数量")
    dependents_count = graphene.Int(description="该包的依赖数量")
    deprecation_reason = graphene.String(description="版本弃用原因")
    description = graphene.String(description="描述信息")
    forks = graphene.Int(description="该包代码仓的fork数")
    homepage = graphene.String(description="该包的主页地址")
    keywords = graphene.List(graphene.String, description="关键词列表")
    language = graphene.String(description="开发语言")
    latest_download_url = graphene.String(description="最新版本下载链接")
    latest_release_number = graphene.String(description="最新发布版本")
    latest_release_published_at = CustomDateTime(description="最新版本发布时间")
    latest_stable_release_number = graphene.String(description="最新稳定版本")
    latest_stable_release_published_at = CustomDateTime(description="最新稳定版本发布时间")
    license_normalized = graphene.String(description="商用声明")
    licenses = graphene.String(description="声明")
    name = graphene.String(description="包名")
    normalized_licenses = graphene.List(graphene.String, description="商用声明")
    package_manager_url = graphene.String(description="包管理平台主页")
    platform = graphene.String(description="包管理平台")
    rank = graphene.Int(description="libraries.io的打分")
    repository_license = graphene.String(description="代码仓声明")
    repository_url = graphene.String(description="代码仓地址")
    stars = graphene.Int(description="该包的star数")
    status = graphene.String(description="该包的生命状态")
    versions = graphene.List(VersionType, description="版本列表")

    class Meta:
        description = "包详情查询，返回包的详细信息"

    def resolve_licenses(parent: dict, info):
        if parent['licenses']:
            return parent['licenses'].split(" ")[0].strip()
        else:
            return "UNKNOWN"


class PackagesType(ObjectType):
    packages = graphene.List(PackageType, description="所有包的列表")
    has_next_page = graphene.Boolean(default_value=False,
                                     description="是否有下一页，目前由于接口限制直接判断该页的总条数是否等于per_page，若相等则认为有下一页")
    page = graphene.Int(default_value=1, description="当前页码，libraries.io的接口参数，用于分页， 默认为1")
    per_page = graphene.Int(default_value=20, description="当前页条目数，libraries.io的接口参数，用于分页， 默认为20")
    platforms = graphene.String(description="包管理平台")

    class Meta:
        description = "包查询类型，返回包查询的信息和包列表"

    def resolve_has_next_page(parent: dict, info, **kwargs):
        if len(parent['packages']) == parent['per_page']:
            return True
        else:
            return False
