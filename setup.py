#!/usr/bin/env python3
#
# MIT License
#
# s3-restore, a point in time restore tool for Amazon S3
#
# Copyright (c) [2020] [Emir Amanbekov]
#
# Author: Emir Amanbekov <amanbekoff@gmail.com>
#
# This software is forked from angeloc/s3-pit-restore released with MIT license.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='s3-restore',
      version='0.1.2',
      description='s3-restore, a point in time restore tool for Amazon S3',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Emir Amanbekov',
      author_email='amanbekoff@gmail.com',
      url='https://github.com/progremir/s3-restore/',
      keywords = ['amazon', 's3', 'restore', 'point', 'time', 'timestamp'],
      scripts=['s3-restore'],
      install_requires=['boto3', 'python-dateutil'],
     )
