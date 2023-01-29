from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'gpt-developer-tools',
    version = '0.0.1',
    author = 'Avnish Pal',
    author_email = 'avnishnish07@gmail.com',
    license = 'MIT',
    description = 'A CLI tool that could debug, explain and create scripts using ChatGPT',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/bovem/gpt-developer-tools',
    py_modules = ['gpt_developer_tools', 'src'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        gdt=gpt_developer_tools:cli
    '''
)