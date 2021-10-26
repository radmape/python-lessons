from distutils.core import setup

with open('README') as file:
    readme = file.read()

"""https://testpypi.python.org/pypi/unbelievable_nice_game"""

setup(
    name='try-local-repo-wargame',
    version='2.0.0',
    packages=['wargame'],
    url='http://localhost:8081/simple',
    license='LICENSE.TXT',
    description='my first game in python',
    long_description=readme,
    author='Vasilev Nikita',
    author_email='radmape@gmail.com',
)