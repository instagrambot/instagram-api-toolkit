# coding: utf-8

"""
    Instagram API

    The Instagram Private API in OpenAPI specs.v3.0  # noqa: E501

    OpenAPI spec version: 0.0.1
    GitHub repo: https://github.com/instagrambot/instagram-api-toolkit
"""

from __future__ import absolute_import

import unittest

import private_instagram_sdk
from AuthBody.clsAuthBody import AuthBody  # noqa: E501
from private_instagram_sdk.rest import ApiException


class TestAuthBody(unittest.TestCase):
    """AuthBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthBody(self):
        """Test AuthBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = private_instagram_sdk.models.clsAuthBody.AuthBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
