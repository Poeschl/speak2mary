from setuptools import setup

setup(name='speak2mary',
      version='1.5.0',
      description='A Python wrapper for Mary TTS',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='Poeschl',
      url='https://github.com/Poeschl/speak2mary',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      license='Apache License - Version 2.0',
      package_dir={'speak2mary': 'speak2mary'},
      packages=['speak2mary'],
      python_requires='>=3',
      )
