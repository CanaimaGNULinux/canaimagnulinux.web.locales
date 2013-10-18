# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'
long_description = open("README.txt").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='canaimagnulinux.web.locales',
      version=version,
      description="Localizaciones para sitio web de Proyecto Canaima GNU/Linux",
      long_description=long_description,
      classifiers=[
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Groupware",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='l10n i18n locale translation',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/CanaimaGNULinux/canaimagnulinux.web.locales',
      license='GPLv2',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['canaimagnulinux', 'canaimagnulinux.web'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      )
