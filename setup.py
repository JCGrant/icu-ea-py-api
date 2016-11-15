from setuptools import setup

setup(
    name='icu-ea-api',
    version='0.3',
    description='A Python API for Imperial College Union\'s eActivities',
    url='https://github.com/JCGrant/icu-ea-api',
    author='JCGrant',
    author_email='jamescolin.grant@gmail.com',
    license='MIT',
    packages=['icu_ea_api'],
    install_requires=[
        'requests'
    ],
    zip_safe=False
)
