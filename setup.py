import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylss",
    version="0.1.1",
    author="Saptarshi Basu",
    author_email="123saptarshi.basu@gmail.com",
    description="Python implementation of the common unix `ls` command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saptarshibasu15/py-ls.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)