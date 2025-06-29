from setuptools import setup, find_packages

setup(
    name="ghosttrack",
    version="1.0.0",
    author="MohammadHossein",
    description="Advanced System Tracker and Pentesting Toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "ghosttrack": ["data/icons/*", "data/templates/*"]
    },
    install_requires=[
        "requests>=2.31.0",
        "colorama>=0.4.6",
        "pyinstaller>=5.13.0"
    ],
    entry_points={
        "console_scripts": [
            "ghosttrack = ghosttrack.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)