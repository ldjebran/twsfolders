
from setuptools import setup, find_packages


setup(name='twsfolders',
      version='0.1.2',
      platforms=['any'],
      packages=find_packages(),
      zip_safe=True,
      url='https://github.com/ldjebran/twsfolders',
      license='Apache 2.0',
      author='Djebran Lezzoum',
      author_email='ldjebran@gmail.com',
      description='TeamWorks Folders',
      test_suite="test.all_tests",
      keywords='ZODDB persistent folders folder item url rootfolders',
      install_requires=['zope.interface', 'persistent', 'ZODB'],
      classifiers=["Programming Language :: Python :: 2.7",
                   ],
      )
