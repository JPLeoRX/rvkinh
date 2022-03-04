from setuptools import setup, find_packages


setup_args = dict(
    name='rvkinh-proxy-utils',
    version='0.1',
    description='',
    keywords=[],
    long_description='',
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    author="rvkinh",
    author_email="rvkinh@mail.com",
    url="https://github.com/jpleorx/rvkinh",
)


install_requires = [
    'injectable',
    'pika',
    'rvkinh-proxy-message-protocol'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
