import os

# 从环境变量中获取配置的libraries.io的api_key
# 该值在项目根目录docker-compose.yml文件中的LIBRARIES_IO_API_KEY中配置
# 该值为敏感详细，请妥善保管
LIBRARIES_IO_API_KEY = os.getenv('LIBRARIES_IO_API_KEY')
