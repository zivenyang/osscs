from rest_framework import serializers


class MetaSerializer(serializers.Serializer):
    page = serializers.IntegerField(default=1)
    per_page = serializers.IntegerField(default=20)
    has_next_page = serializers.BooleanField(default=False)
    is_no_result = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return instance


class PackageSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True, allow_blank=True, allow_null=True)
    keywords = serializers.ListField(allow_empty=True, allow_null=True)
    latest_release_number = serializers.CharField(required=True)
    latest_stable_release_number = serializers.CharField(required=True)
    latest_stable_release_published_at = serializers.DateTimeField(input_formats="%Y-%m-%dT%H:%M:%F.%fZ")
    licenses = serializers.CharField(allow_null=True, allow_blank=True)
    stars = serializers.IntegerField()
    status = serializers.CharField(allow_null=True)
    dependent_repos_count = serializers.IntegerField()

    # def get_licenses(self, obj):
    #     if obj.licenses:
    #         return obj.licenses.split(" ")[0].strip()
    #     else:
    #         return "UNKNOWN"

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return instance


class PackageListSerializer(serializers.Serializer):
    package_list = PackageSerializer(required=False, many=True, allow_null=True)
    meta = MetaSerializer(required=True)

    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return validated_data


class PackageVersionSerializer(serializers.Serializer):
    number = serializers.CharField(required=True)
    published_at = serializers.DateTimeField(input_formats="%Y-%m-%dT%H:%M:%F.%fZ")
    spdx_expression = serializers.CharField(allow_null=True)
    original_license = serializers.CharField(allow_null=True)
    researched_at = serializers.DateTimeField(input_formats="%Y-%m-%dT%H:%M:%F.%fZ", allow_null=True)
    repository_sources = serializers.ListField(allow_null=True, allow_empty=True)

    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return validated_data


class PackageDetailSerializer(serializers.Serializer):

    dependent_repos_count = serializers.IntegerField()
    dependents_count = serializers.IntegerField()
    deprecation_reason = serializers.CharField(allow_null=True, allow_blank=True)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    forks = serializers.IntegerField()
    homepage = serializers.URLField(allow_blank=True, allow_null=True)
    keywords = serializers.ListField(allow_null=True, allow_empty=True)
    language = serializers.CharField()
    latest_download_url = serializers.URLField(allow_null=True, allow_blank=True)
    latest_release_number = serializers.CharField(allow_null=True)
    latest_release_published_at = serializers.DateTimeField(input_formats="%Y-%m-%dT%H:%M:%F.%fZ", allow_null=True)
    latest_stable_release_number = serializers.CharField(allow_null=True)
    latest_stable_release_published_at = serializers.DateTimeField(input_formats="%Y-%m-%dT%H:%M:%F.%fZ", allow_null=True)
    license_normalized = serializers.BooleanField()
    licenses = serializers.CharField(allow_null=True, allow_blank=True)
    name = serializers.CharField()
    normalized_licenses = serializers.ListField(allow_null=True, allow_empty=True)
    package_manager_url = serializers.URLField(allow_null=True, allow_blank=True)
    platform = serializers.CharField()
    rank = serializers.IntegerField()
    repository_license = serializers.CharField()
    repository_url = serializers.URLField(allow_blank=True, allow_null=True)
    stars = serializers.IntegerField()
    status = serializers.CharField(allow_null=True, allow_blank=True)
    versions = PackageVersionSerializer(many=True, allow_null=False)

    # def get_licenses(self, obj):
    #     if obj.licenses:
    #         return obj.licenses.split(" ")[0].strip()
    #     else:
    #         return "UNKNOWN"

    def update(self, instance, validated_data):
        return instance

    def create(self, validated_data):
        return validated_data


