from setuptools import setup, find_packages

setup(name='gym_game_nim',
      version='0.0.1',
      install_requires=['gym'],
      packages=find_packages(),
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      )
