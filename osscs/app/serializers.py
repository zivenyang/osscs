class PackageListSerializer(object):
    def __init__(self):
        self.package_list = []
        self.meta = {}

    def to_dict(self):
        return {
            "package_list": self.package_list,
            "meta": self.meta
        }


class MetaSerializer(object):
    def __init__(self):
        self.page = 1
        self.per_page = 20
        self.has_next_page = False
        self.is_no_result = False

    def to_dict(self):
        return {
            "page": self.page,
            "per_page": self.per_page,
            "has_next_page": self.has_next_page,
            "is_no_result": self.is_no_result
        }


class PackageSerializer(object):

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

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "keywords": self.keywords,
            "latest_release_number": self.latest_release_number,
            "latest_stable_release_number": self.latest_stable_release_number,
            "latest_stable_release_published_at": self.latest_stable_release_published_at,
            "licenses": self.licenses,
            "stars": self.stars,
            "status": self.status,
            "dependent_repos_count": self.dependent_repos_count,
        }


class PackageDetailSerializer(object):

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
        self.versions = [PackageVersionSerializer(i).to_dict() for i in obj["versions"]]

    def to_dict(self):
        return {
            "dependent_repos_count": self.dependent_repos_count,
            "dependents_count": self.dependents_count,
            "deprecation_reason": self.deprecation_reason,
            "description": self.description,
            "forks": self.forks,
            "homepage": self.homepage,
            "keywords": self.keywords,
            "language": self.language,
            "latest_download_url": self.latest_download_url,
            "latest_release_number": self.latest_release_number,
            "latest_release_published_at": self.latest_release_published_at,
            "latest_stable_release_number": self.latest_stable_release_number,
            "latest_stable_release_published_at": self.latest_stable_release_published_at,
            "license_normalized": self.license_normalized,
            "licenses": self.licenses,
            "name": self.name,
            "normalized_licenses": self.normalized_licenses,
            "package_manager_url": self.package_manager_url,
            "platform": self.platform,
            "rank": self.rank,
            "repository_license": self.repository_license,
            "repository_url": self.repository_url,
            "stars": self.stars,
            "status": self.status,
            "versions": self.versions,
        }


class PackageVersionSerializer(object):
    def __init__(self, obj):
        self.number = obj["number"]
        self.published_at = obj["published_at"]
        self.spdx_expression = obj["spdx_expression"]
        self.original_license = obj["original_license"]
        self.researched_at = obj["researched_at"]
        self.repository_sources = obj["repository_sources"]

    def to_dict(self):
        return {
            "number": self.number,
            "published_at": self.published_at,
            "spdx_expression": self.spdx_expression,
            "original_license": self.original_license,
            "researched_at": self.researched_at,
            "repository_sources": self.repository_sources,
            "vulnerabilities": "2 vulnerabilities",
            "usages": 100,
        }
