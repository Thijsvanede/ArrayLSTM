import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="array-lstm",
    version="0.0.1",
    author="Thijs van Ede",
    author_email="t.s.vanede@utwente.nl",
    description="Pytorch implementation of Recurrent Memory Array Structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thijsvanede/ArrayLSTM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
