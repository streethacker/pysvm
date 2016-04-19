from setuptools import setup, find_packages


requires = []

setup(
    name='pysvm',
    version='0.1',
    description='Simple Verify Code Manager',
    author='YUCHI',
    author_email='wei.chensh@ele.me',
    packages=find_packages(),
    url='https://github.com/streethacker/pysvm',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
