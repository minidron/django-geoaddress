# --coding: utf8--
from setuptools import setup, find_packages


setup(
    name='django-geoaddress',
    version='0.1.10',
    description=('Address field with GEO coordinates'),
    long_description=open('README.md').read(),
    author='Pavel ALekin',
    maintainer='Pavel Alekin',
    maintainer_email='pavel.alekin@gmail.com',
    url='https://github.com/minidron/django-geoaddress',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        'Framework :: Django',
        "Topic :: Database :: Front-Ends",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Operating System :: OS Independent",
    ]
)
