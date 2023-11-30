from setuptools import setup
setup(
    name='sacumen',
    version='0.1',
    packages=['sacumen'],
    install_requires=[
        'google-cloud-storage',
        'boto3',
    ],
)