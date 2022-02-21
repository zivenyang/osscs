from urllib import parse

MVN_REPOSITORY_URL = 'https://mvnrepository.com'
MVN_REPOSITORY_PACKAGE_SEARCH_URL = parse.urljoin(MVN_REPOSITORY_URL, '/search')
PYPI_REPOSITORY_URL = 'https://pypi.org'
PYPI_REPOSITORY_PACKAGE_SEARCH_URL = parse.urljoin(PYPI_REPOSITORY_URL, '/search')

LIBRARIES_IO_URL = 'https://libraries.io'
LIBRARIES_IO_API_URL = parse.urljoin(LIBRARIES_IO_URL, '/api/')
LIBRARIES_IO_PROJECT_SEARCH_API_URL = parse.urljoin(LIBRARIES_IO_API_URL, 'search')
