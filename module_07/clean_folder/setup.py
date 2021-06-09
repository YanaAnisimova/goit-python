from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clears the folder script',
    author='Yana',
    author_email='begemotvot2@gmail.com',
    packages=find_packages(where="src"),
    entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main'],
    },
)
