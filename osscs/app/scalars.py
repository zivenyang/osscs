import datetime

from graphene import Scalar
from graphql.language import ast


class CustomDateTime(Scalar):
    """
    自定义时间， 解决时间格式适配问题
    如：'2022-02-01T07:56:23.000Z'
    """

    @staticmethod
    def serialize(dt):
        assert isinstance(
            dt, (datetime.datetime, datetime.date, str)
        ), 'Received not compatible datetime "{}"'.format(repr(dt))
        if isinstance(dt, str):
            return datetime.datetime.strptime(
                dt, "%Y-%m-%dT%H:%M:%S.%fZ").isoformat()
        else:
            return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def parse_value(value):
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
