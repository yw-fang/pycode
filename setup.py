from setuptools import setup

def readme():
    with open('README.rst') as f:
        return(f.read())
    

setup(name='pycode',
      version='2.0',
      description='A repo for testing the source code magnagement',
      long_description=readme(),
      classifiers=[
          'Development Status :: v2.0',
          'License:: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Pthon package',
          ],
      keywords='python code package tutorial',
      url='https://github.com/yw-fang/pycode',
      author='Yue-Wen FANG',
      author_email='fyuewen@gmail.com',
      license='MIT',
      packages=['pycode'],
      install_requires=[
         'markdown', 
          ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)


