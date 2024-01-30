from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')
# long_description = ''


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='imi-plot',
    version='0.0.1',
    url='https://github.com/MyNameIsFu/scikit-plot',
    license='MIT License',
    author='Michael Fujarski',
    tests_require=['pytest'],
    install_requires=[
        'matplotlib>=1.4.0',
        'scikit-learn>=0.18',
        'scipy>=0.9',
        'joblib>=0.10'
    ],
    cmdclass={'test': PyTest},
    author_email='michael.fujarski@uni-muenster.de',
    description='Fork of the scikit-plot library. Adapted for medical research questions. Original author: Reiichiro Nakano. An intuitive library to add plotting functionality to scikit-learn objects. Original URL: https://github.com/reiinakano/scikit-plot',
    long_description=long_description,
    packages=['imiplot'],
    include_package_data=True,
    platforms='any',
    test_suite='imiplot.tests.test_scikitplot',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Visualization',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
