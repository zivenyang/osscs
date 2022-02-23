import graphene

from .spiders import LibrariesProjectAPI, LibrariesProjectSearchAPI
from .types import PackageType, PackagesType


class Query(graphene.ObjectType):
    """
    {
  packages(q: "lessc", platforms: "pypi", page: 1) {
    hasNextPage
    page
    perPage
    platforms
    packages {
      dependentReposCount
      dependentsCount
      deprecationReason
      description
      forks
      homepage
      keywords
      language
      latestDownloadUrl
      latestReleaseNumber
      latestReleasePublishedAt
      latestStableReleaseNumber
      latestStableReleasePublishedAt
      licenseNormalized
      licenses
      name
      normalizedLicenses
      packageManagerUrl
      platform
      rank
      repositoryLicense
      repositoryUrl
      stars
      status
      versions {
        number
        publishedAt
        spdxExpression
        originalLicense
        researchedAt
        repositorySources
      }
    }
  }
}

    """
    package = graphene.Field(PackageType,
                             platform=graphene.String(required=True),
                             name=graphene.String(required=True))
    packages = graphene.Field(PackagesType,
                              q=graphene.String(required=True),
                              platforms=graphene.String(required=True),
                              page=graphene.Int(default_value=1),
                              per_page=graphene.Int(default_value=20))

    def resolve_package(self, info, platform, name):
        return LibrariesProjectAPI(platform=platform, name=name).get_response().json()

    def resolve_packages(self, info, q, platforms, page, per_page):
        packages = LibrariesProjectSearchAPI(q=q, platforms=platforms, page=page,
                                             per_page=per_page).get_response().json()
        data = {
            'q': q,
            'platforms': platforms,
            'page': page,
            'per_page': per_page,
            'packages': packages
        }
        return data


schema = graphene.Schema(query=Query)
