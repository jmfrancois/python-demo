from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='talend.demo',
      version=version,
      description="Demo",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='demo',
      author='JeanMichel FRANCOIS',
      author_email='jmfrancois@talend.com',
      url='https://github.com/talend/demo',
      license='Apache-2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['talend'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      )