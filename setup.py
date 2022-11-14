from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="mydemo",
    version="0.0.1",
    description="Demo project",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/devanand1978",
    author="Devanand Kumar",
    author_email="devrishi.dk@gmail.com",
    keywords="My Demo package",
    license="MIT",
    packages=["foo"],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
