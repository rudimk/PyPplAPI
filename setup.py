from setuptools import setup

setup(name='pypplapi',    
    version='0.1',
    description="A Python wrapper around pplapi.",
    url='https://github.com/rudimk/pypplapi',
    author='Rudraksh MK',
    author_email='rudraksh.mk@gmail.com',
    license='MIT',
    packages=['pypplapi'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)