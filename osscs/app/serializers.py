class BasePackageListSerializer(object):
    def __init__(self):
        self.package_list = []
        self.next_page = ""

    def to_dict(self):
        return {
            "package_list": self.package_list,
            "next_page": self.next_page
        }


class PypiPackageSerializer(object):
    def __init__(self):
        self.package_url = ""
        self.package_name = ""
        self.package_description = ""
        self.package_version = ""
        self.package_released = ""

    def to_dict(self):
        return {
            "package_url": self.package_url,
            "package_name": self.package_name,
            "package_description": self.package_description,
            "package_version": self.package_version,
            "package_released": self.package_released
        }
