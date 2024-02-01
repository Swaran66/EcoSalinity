from setuptools import setup, find_packages

setup(
    name='ecosalinity',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'seaborn',
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'ecosalinity=EcoSalinity.ecosalinity:main',
            'ecosalinity2=EcoSalinity.ecosalinity2:main',
        ],
    },
)
