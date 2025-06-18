from setuptools import setup

__version__ = '1.0.0'
__title__ = 'hpa'
__author__ = 'Taskevich'
__license__ = 'Apache License 2.0'
__url__ = 'https://developer.huawei.com/consumer/cn/'

install_requires = ['requests>=2.20.1']

long_description = ('The Huawei Admin Python SDK enables server-side (backend) Python developers '
                    'to integrate Huawei into their services and applications.')

setup(
    name=__title__,
    version=__version__,
    description='Huawei Push Admin',
    long_description=long_description,
    url='https://developer.huawei.com/consumer/cn/',
    author='Huawei',
    license='Apache License 2.0',
    install_requires=install_requires,
    packages=['hpa'],
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: Apache Software License',
    ],
)
