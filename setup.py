from setuptools import setup, find_packages

requires=[
	'tensorflow==2.10.0',
	'Pillow'
    ]



setup(
    name='gender_classifier',
    version='1.0.0',
    author='Maksym Remezovskyi',
    author_email='maks.remezovskij1@gmail.com',
    url='https://github.com/maksr137/gender_classifier',
    packages=find_packages(),
    install_requires=requires,
    entry_points = {
       'console_scripts': [
           'gender-classifier=api.main:predict'
       ]
    },
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)