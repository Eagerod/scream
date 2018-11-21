import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='scream',
    description='An opinionated CLI tool for Python monorepo MGMT.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/r-kells/scream",
    version='0.0.1',
    packages=setuptools.find_packages(exclude=["venv"]),
    install_requires=[
        "flake8==3.5.0",
        "pep8-naming==0.7.0",
        "coverage",
        "tox==3.5.3",
        "wheel"
    ],
    entry_points={
        'console_scripts': (
            'scream = scream.cli.main:Scream',
        )},
    scripts=['bin/detect_parent_branch.sh'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
