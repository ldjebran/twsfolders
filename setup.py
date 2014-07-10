
from setuptools import setup, find_packages

import unittest


def all_tests():
    test_loader = unittest.TestLoader()
    return test_loader.loadTestsFromNames(['twsfolders.tests.test_rootfolders',
                                           'twsfolders.tests.test_folder'
                                           ]
                                          )

setup(name='twsfolders',
      version='0.1.0',
      platforms=['any'],
      packages=find_packages(),
      zip_safe=True,
      url='https://github.com/ldjebran/twsfolders',
      license='Apache 2.0',
      author='Djebran Lezzoum',
      author_email='ldjebran@gmail.com',
      description='TeamWorks Folders',
      test_suite="__main__.all_tests",
      keywords='ZODDB persistent folders folder item url rootfolders',
      install_requires=['zope.interface', 'persistent', 'ZODB'],
      classifiers=["Programming Language :: Python :: 2.7",
                   ],
      )
