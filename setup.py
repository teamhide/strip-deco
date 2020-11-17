# encoding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strip-deco",
    version="0.0.6",
    author="Hide",
    author_email="padocon@naver.com",
    description="Easily strip decorator from function or class method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/teamhide/strip-deco",
    packages=setuptools.find_packages(),
    tests_require=["pytest"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
)
