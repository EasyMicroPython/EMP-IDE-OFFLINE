import os
from setuptools import find_packages, setup


setup(
    name='emp-offline',
    version='0.1.6',
    # py_modules=['empide_offline'],
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='emp ide offline version',
    url='http://emp.1zlab.com/',
    author='Fuermohao',
    author_email='Fuermohao@outlook.com',
    platforms='Linux,Unix',
    keywords='MicroPython,1ZLAB,EMP,ESP',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    entry_points={
        'console_scripts': [
            'empide = emp_offline.ide:runserver',
        ],
    },
    install_requires=[
        'flask',
        'flask-script'
    ],
)
