import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MediaComp-paulbuis", # Replace with your own username
    version="0.0.1",
    author="Paul Buis",
    author_email="00pebuis@bsu.edu",
    description="A package of Python 3 modules intended to mimic Guzdial & Ericson's JES Media Computation library in an IPython / Jupyter environment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulbuis/MediaComp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Framework :: IPython",
        "Framework :: Jupyter",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Video",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['Pillow', 'numpy', 'matplotlib', 'scipy', 'ipython'],
    python_requires='>=3.7',
)