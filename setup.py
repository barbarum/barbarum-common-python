import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barbarum-common", # Replace with your own username
    version="0.0.2",
    author="Ding Wei",
    author_email="noreply@barbarum.com",
    description="Common extensions of Python standard library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barbarum/barbarum-common-python.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)