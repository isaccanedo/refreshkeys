from setuptools import setup

setup(
    name='refreshkeys',
    version='1.0.0',
    url='https://github.com/isaccanedo/refreshkeys',
    author='Isac Canedo',
    description='Script to automatically refresh ssh/gpg key passphrases in keychain using 1password',
    license='MIT',
    packages=['refreshkeys'],
    install_requires=[
        'pexpect'
    ],
    entry_points={
        'console_scripts': [
            'refreshkeys=refreshkeys:main'
        ]
    }
)
