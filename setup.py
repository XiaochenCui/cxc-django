from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='cxc-django',
    version='0.0.3',
    description='A django wrapper made by Xiaochen Cui',
    long_description=long_description,
    url='https://github.com/XiaochenCui/cxc-django',
    author='Xiaochen Cui',
    author_email='jcnlcxc.new@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='django',
    packages=find_packages(),
    install_requires=['django', 'django-rest-framework', ],
)
