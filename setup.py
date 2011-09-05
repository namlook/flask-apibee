"""
Flask-API
--------------

Flask-API allow to easily publish an API for you web application
"""
from setuptools import setup


setup(
    name='Flask-API',
    version='0.1',
    url = 'http://github.com/namlook/Flask-API',
    license='BSD',
    author='Nicolas Clairon',
    description='A Flask extension simplifies to build and publish an API for a web application',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'apibee',
        'decorator',
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
