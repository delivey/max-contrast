import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="max-contrast",
    version="0.0.2",
    url="https://github.com/delivey/max-contrast",
    license="MIT",
    author="delivey",
    description="Library which replicates the Paint.net contrast & brightness functionality in Python, allowing you to increase the contrast of an image until it turns B&W.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["max_contrast"],             # Name of the python package
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=["Pillow"]                     # Install other dependencies if any
)