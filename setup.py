import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="provisioning",
    version="0.1",
    url='http://github.com/maduck/provisioning',
    license='GPL',
    description="A provisioning server for VoIP phones",
    long_description=read('README'),

    author='Matthias Utke',
    author_email=None,

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['setuptools'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
