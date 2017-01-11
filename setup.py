from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='pynsga2',
      version='1.0',
      description='Libraries for performing nsga2 calibration.',
      long_description=readme(),
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: Beta"
        "Intended Audience :: Science/Research",
        "Natural Language :: English",     
      ],
      url='https://github.com/mehmetbercan/pynsga2',
      author='Mehmet B. Ercan',
      author_email='mehmetbercan@gmail.com',
      license='MIT',
      packages=['pynsga2'],
      install_requires=['pynsga2','numpy'],
      include_package_data=True
      )
