from setuptools import setup

setup(
    name='yaksok',
    packages=['yaksok'],
    entry_points = {
        'console_scripts': [
            'yaksok = yaksok.yaksok:main',
        ],
    },
)
