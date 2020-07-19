#setup / configuracion

from setuptools import setup

setup(
    name = 'PyQuendo',
    packages = ['PyQuendo'],
    version = '1.0.0',
    description = (
        "Traduzca a voz todo el texto que escriba"),

    author = 'sn.Lionel90 aka Lionel Sanchez',
    url = 'https://github.com/snLionel90/',
    download_url = 'https://github.com/snLionel90/TTS-PyQuendo',

    keywords=['locuendo', 'snLionel90', 'voice', 'txt'],
    classifiers=[],
    install_requires=[
        'PyQt5',
        'pillow',
        'mpg123',
        'tts'
    ],
    include_package_data=True, 
)
