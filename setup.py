from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python wrapper for PICam'
LONG_DESCRIPTION = 'Python wrapper for Teledyne Princeton Instruments PICam'

# Setting up
setup(
        name="PICamPy", 
        version=VERSION,
        author="Oskari Timgren",
        author_email="<oskari.timgren@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(where = 'src'),
        package_dir = {'':"src"},
        install_requires=['pythonnet'],    
        keywords=['python', ],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)