from urllib import parse

MAVEN = 'maven'
PYPI = 'pypi'
MVN_REPOSITORY_URL = 'https://mvnrepository.com'
MVN_REPOSITORY_PACKAGE_SEARCH_URL = parse.urljoin(MVN_REPOSITORY_URL, '/search')
PYPI_REPOSITORY_URL = 'https://pypi.org'
PYPI_REPOSITORY_PACKAGE_SEARCH_URL = parse.urljoin(PYPI_REPOSITORY_URL, '/search')
