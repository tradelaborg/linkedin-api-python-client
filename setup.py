from setuptools import find_packages, setup

setup(
  name='linkedin-api-client',
  packages=find_packages(include=['linkedin_api_client']),
  version='0.0.1',
  description='LinkedIn API Python client library',
  author='LinkedIn',
  install_requires=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  test_suite='tests'
)