from setuptools import setup, find_packages

setup(
    name='healthcare_chatbot',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            # Add your command line scripts here
        ],
    },
)