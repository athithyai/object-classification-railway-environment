from setuptools import setup, find_packages

setup(name='resnet-yolo',
      version=open("yolo/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      description='object detection algorithm',
      author='Athithya',
      author_email='greatathithya@gmail.com',
      packages=find_packages(),
     )
