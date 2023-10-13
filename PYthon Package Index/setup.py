from setuptools import setup

setup(
    name = 'VicksTor', # while installing pacakge
    version = '0.1.2',
    description = 'Hosting Flask on Tor Browser.',
    long_description = open('Readme.txt').read(),
    url = 'https://github.com/imvickykumar999/Flask-XAMPP-Onion-Host',
    author = 'Vicky Kumar',
    keywords = ['Hosting', 'Flask', 'XAMPP', 'Tor Browser', 'Onion'],
    license = 'MIT',
    packages = ['HostTor'], # while importing package
)
