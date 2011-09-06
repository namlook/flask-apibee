"""
Flask-API
--------------

Flask-API allow you to easily build and publish an API for your Flask application
"""
from setuptools import setup


setup(
    name='Flask-API',
    version='0.2',
    url = 'http://github.com/namlook/Flask-API',
    license='BSD',
    author='Nicolas Clairon',
    description='A Flask extension which allow to build and publish an API for a Flask application',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'apibee',
    ],
    test_suite='tests.suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
