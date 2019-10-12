from io import open  # required for Python 2
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

this_directory = dirname(abspath(__file__))

with open(join(this_directory, "README.md"), encoding='utf-8') as f:
    long_description = f.read()

with open(join(this_directory, "src", "Tokenkeycloak", "version.py"), encoding='utf-8') as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip(" '\"")
            break
        else:
            version = "0.0.1"
            break

setup(
    name="robotframework-tokenkeycloak",
    version=version,
    description="A Robot Framework library for manage keycloak token",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Grazia D'Amico",
    author_email="graziagdamico@gmail.com",
    url="",
    license="MIT",
    keywords="robotframework library token keycloak",
    classifiers=[        
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    package_dir={'':'src'},   # tell distutils packages are under src
    packages=find_packages('src'),  # include all packages under src
    python_requires='>=2.7',
)
