from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django-inlinetrans',
      version=version,
      description="Is a django application that allows the translation of django templtes from the rendered html in the browser",
      long_description="""\
long description""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='django translation',
      author='Antonio P\xc3\xa9rez-Aranda Alcaide',
      author_email='ant30tx@gmail.com',
      url='http://code.google.com/p/django-inlinetrans/',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )