#!/usr/bin/env python

from distutils.core import setup

setup(name='django-userauthcode',
      version='0.1',
      description='Generate Django user authentication codes to verify email addresses and activate user accounts.',
      author='Manuel Badzong',
      author_email='manuel@andev.ch',
      url='https://github.com/badzong/django-userauthcode',
      py_modules=['userauthcode',],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
     )
