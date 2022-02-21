from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)


class PackagePlatforms(BaseEnum):
    pypi = 'pypi'
    maven = 'maven'
    go = 'go'
    npm = 'npm'
