from setuptools import setup

setup(name='mdutils',
      version='1.6.0',
      license='MIT',
      author='Didac Coll',
      author_email='didaccoll_93@hotmail.com',
      maintainer='Didac Coll',
      maintainer_email='didaccoll_93@hotmail.com',
      description='Useful package for creating Markdown files while executing python code.',
      long_description=open('./doc/source/README.rst').read(),
      platforms=['Python 3.6', 'Python 3.7', 'Python 3.8'],
      packages=['mdutils', 'mdutils.tools', 'mdutils.fileutils'],
      include_package_data=True,
      zip_safe=False,
      url='https://github.com/didix21/mdutils',
      project_urls={
        'Documentation': 'http://mdutils.readthedocs.io',
        'Say Thanks!': 'https://github.com/didix21/',
        'Source': 'https://github.com/didix21/mdutils',
      },
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Utilities',
                   'Topic :: Software Development :: Documentation',
                   'Topic :: Text Processing :: Markup',
                   'License :: OSI Approved :: MIT License'])
