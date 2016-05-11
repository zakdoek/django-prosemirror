"""
Install script
"""

import codecs
import os
import re

from setuptools import setup, find_packages

import versioneer


###############################################################################

NAME = "django-prosemirror"
AUTHOR = "Tom Van Damme"
EMAIL = "t_o_mvandamme@hotmail.com"
URL = "https://github.com/zakdoek/django-prosemirror/"
LICENSE = "MIT"
DESCRIPTION = "Prosemirror field for django"
PACKAGES = find_packages()
CLASSIFIERS = [
    "Framework :: Django",
]
INSTALL_REQUIRES = []

###############################################################################

README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()


if __name__ == "__main__":
    print(PACKAGES)
    setup(
        name=NAME,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=README,
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=PACKAGES,
        include_package_data=True,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )
