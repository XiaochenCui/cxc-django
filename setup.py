from setuptools import setup, find_packages

setup(
    name='cxc-django',
    version='0.0.1',
    description='A django wrapper made by Xiaochen Cui',
    url='https://github.com/XiaochenCui/cxc-django',
    auther='Xiaochen Cui',
    auther_email='jcnlcxc.new@gmail.com',
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
