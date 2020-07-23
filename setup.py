#setup / configuracion

import setuptools

with open ("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'PyQuendo',
    version = '1.0.0',
    author = 'sn.Lionel90 aka Lionel Sanchez',
    description = ("Traduzca a voz todo el texto que escriba"),
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url = 'https://github.com/snLionel90/TTS-PyQuendo',
    keywords=['locuendo', 'snLionel90', 'voice', 'txt'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: TTS text to speech :: snLionel90 ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True, 
)
