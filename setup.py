import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitcoin_tools",
    version="0.0.1",
    author="Justin Moen",
    author_email="jamoen7@gmail.com",
    description="Python Bitcoin Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superquest/python-bitcoin-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

