import setuptools

setuptools.setup(
    name='mfetch',
    version='0.0.1',
    author='michaelscripter',
    url="https://github.com/MichaelScripter/kfetch",
    project_urls={
        "Bug Tracker": "https://github.com/MichaelScripter/kfetch/issues",
    },
    description='Simple and minimalistic fetching software, requires python 3 and nerdfonts',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["colorama"],
    packages=setuptools.find_packages(),
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "fetch = fetcher.cli:main",
        ]
    }
)