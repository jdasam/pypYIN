from setuptools import setup

if __name__ == '__main__':
    with open('README.md') as fh:
        readme_contents = fh.read()

    setup(name='pypyin',
          version='1.0',
          author='Rong GONG',
          url='https://github.com/stefansjs/pypYIN',

          description='pYIN algorithm implemented in python. https://code.soundsoftware.ac.uk/projects/pyin',
          long_description=readme_contents,
          long_description_content_type='text/markdown',

          # Get all the packages from the src directory and remap them to root packages
          packages=['pypyin'],
          package_dir={'': 'src'},
          scripts=['demo.py'],

          install_requires=['numpy',
                            'scipy',
                            'librosa'],
          )
