from setuptools import find_packages,setup

setup(
    name='mcq-generator',
    version='0.0.1',
    author='ragibmondal',
    author_email='ragib5303721@gmail.com',
    install_requires=['google-generativeai',
                      'langchain',
                      'streamlit',
                      'python-dotenv',
                      'PyPDF2'],
    packages=find_packages()
)
