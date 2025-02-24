from setuptools import setup, find_packages

with open('README.md','r') as f:
    description = f.read()

setup(
    name = 'ching_chatgpt_utils',
    version = "0.1.5",
    packages = find_packages(),
    install_requires = [
        'regex',
        'openai',
        'PyYAML',
        'pydantic'
    ],
    long_description = description,
    long_description_content_type = "text/markdown",
    author = 'Ching Fhen',
    author_email = 'dsai.chingfhen@gmail.com'
)