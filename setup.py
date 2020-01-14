from setuptools import setup

setup(name='speak2mary',
      version='1.2.0',
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
      ],
      license='Apache License - Version 2.0',
      package_dir={'marytts': 'marytts'},
      packages=['marytts'],
      python_requires='>=3',
      )
