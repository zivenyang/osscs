# Create your models here.


# 由于直接使用的接口，这里直接返回对应的对象
class PackageListObject(object):
    def __init__(self):
        self.package_list = []
        self.meta = {}


class MetaObject(object):
    def __init__(self):
        self.page = 1
        self.per_page = 20
        self.has_next_page = False
        self.is_no_result = False


class PackageObject(object):

    def __init__(self, obj):
        self.name = obj["name"]
        self.description = obj["description"]
        self.keywords = obj["keywords"]
        self.latest_release_number = obj["latest_release_number"]
        self.latest_stable_release_number = obj["latest_stable_release_number"]
        self.latest_stable_release_published_at = obj["latest_stable_release_published_at"]
        self.licenses = obj["licenses"].split(" ")[0].strip() if obj["licenses"] else "UNKNOWN"
        self.stars = obj["stars"]
        self.status = obj["status"]
        self.dependent_repos_count = obj["dependent_repos_count"]


class PackageDetailObject(object):

    def __init__(self, obj):
        self.dependent_repos_count = obj["dependent_repos_count"]
        self.dependents_count = obj["dependents_count"]
        self.deprecation_reason = obj["deprecation_reason"]
        self.description = obj["description"]
        self.forks = obj["forks"]
        self.homepage = obj["homepage"]
        self.keywords = obj["keywords"]
        self.language = obj["language"]
        self.latest_download_url = obj["latest_download_url"]
        self.latest_release_number = obj["latest_release_number"]
        self.latest_release_published_at = obj["latest_release_published_at"]
        self.latest_stable_release_number = obj["latest_stable_release_number"]
        self.latest_stable_release_published_at = obj["latest_stable_release_published_at"]
        self.license_normalized = obj["license_normalized"]
        self.licenses = obj["licenses"].split(" ")[0].strip() if obj["licenses"] else "UNKNOWN"
        self.name = obj["name"]
        self.normalized_licenses = obj["normalized_licenses"]
        self.package_manager_url = obj["package_manager_url"]
        self.platform = obj["platform"]
        self.rank = obj["rank"]
        self.repository_license = obj["repository_license"]
        self.repository_url = obj["repository_url"]
        self.stars = obj["stars"]
        self.status = obj["status"]
        self.versions = [PackageVersionObject(i) for i in obj["versions"]]


class PackageVersionObject(object):
    def __init__(self, obj):
        self.number = obj["number"]
        self.published_at = obj["published_at"]
        self.spdx_expression = obj["spdx_expression"]
        self.original_license = obj["original_license"]
        self.researched_at = obj["researched_at"]
        self.repository_sources = obj["repository_sources"]
