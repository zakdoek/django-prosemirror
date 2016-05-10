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
PACKAGES = find_packages()
CLASSIFIERS = [
    "Private :: Do not upload",
]
INSTALL_REQUIRES = []

###############################################################################


if __name__ == "__main__":
    print(PACKAGES)
    setup(
        name=NAME,
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=PACKAGES,
        include_package_data=True,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )
