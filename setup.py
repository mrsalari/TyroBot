from setuptools import setup, find_packages

setup(
    name = 'TyroBot',
    version = '2.0.3',
    author='mohammad saeed salari',
    author_email = 'salari601601@gmail.com',
    description = 'This is a powerful library for building self robots in Rubika',
    keywords = ['rubika', 'rubino', 'tyrobot', 'pyrubika', 'rubika bot', 'rubika library', 'rubx', 'rubika-bot', 'rubika-lib', 'bot', 'self bot', 'rubika.ir', 'asyncio'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/mrsalari/TyroBot',
    packages = find_packages(),
    install_requires = ['pycryptodome', 'websocket-client', 'websockets', 'requests', 'aiohttp', 'pillow', 'mutagen', 'tinytag'],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ]
)