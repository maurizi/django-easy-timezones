import os
from setuptools import setup

# Set external files
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    README = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-easy-timezones-redux',
    version='1.0.3',
    packages=['easy_timezones'],
    install_requires=required,
    include_package_data=True,
    license='Apache License',
    description='Easy timezones for Django (>=1.11) based on MaxMind GeoIP2.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/maurizi/django-easy-timezones',
    author='Rich Jones',
    maintainer='Michael Maurizi',
    maintainer_email='michael@maurizi.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
