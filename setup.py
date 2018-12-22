from setuptools import setup
import io
import os

here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
with io.open(readme_path, encoding='utf-8') as readme_file:
    long_description = readme_file.read()

def readme():
    with open('README.rst') as f:
        return(f.read())
    

setup(name='pyplayground',
      version='4.0',
      description='A repo for testing the source code magnagement',
      long_description=long_description,
      classifiers=[
          'Development Status :: v4.0',
          'License:: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Pthon package',
          ],
      keywords='python code package tutorial',
      url='https://github.com/yw-fang/pyplayground',
      author='Yue-Wen FANG',
      author_email='fyuewen@gmail.com',
      license='MIT',
      packages=['pyplayground'],
      install_requires=[
         'markdown', 
          ],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=['scripts/print_greetings.py'],
      entry_points = {
          'console_scripts': ['print_greetings_entry=pyplayground.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
