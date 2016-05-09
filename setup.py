# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "lookerpy"
VERSION = "1.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Looker API 3.0 Reference",
    author_email="",
    url="",
    keywords=["Swagger", "Looker API 3.0 Reference"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This document describes the Looker API.  Please note that this is the &#39;new&#39; Looker RESTful API. This API uses Looker &#39;API 3&#39; keys. Those keys can be created for Looker users by Looker admins on the admin/user edit page. Such keys will allow a user to autheticate to the API as that user; having that user&#39;s permissions. Admins can create &#39;dummy&#39; accounts specifically for API use, or add keys to real users&#39; accounts.  A Ruby SDK is available to integrate this API into applications. Standard RESTful practices are used by the API, so it should be callable by any RESTful client framework - or just using raw HTTP requests. Additionally, the &#39;api-docs&#39; page served by the Looker instance includes &#39;Try it out!&#39; buttons for each API method so that anyone logged in with an API3 key can call the API directly from the documentation page.  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications.  This document does not cover the old Looker Query API. The methods in the &#39;Query&#39; section below are intended to replace that old API. Nonetheless, information about the old API can be found at             [Query API](http://www.looker.com/docs/reference/api-and-integration/looker-api-reference) and             [Ruby SDK](http://www.looker.com/docs/reference/api-and-integration/looker-ruby-sdk).  
    """
)


