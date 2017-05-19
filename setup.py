"""Douban Album Downloader"""


from setuptools import setup, find_packages

setup(
    name = "douban album downloader",
    version = "0.0.1",
    description = "douban album downloader",
    long_description = "douban album downloader",
    url = "https://github.com/delta4d/douban-album-dl",
    author = "delta",
    email = "delta4d@gmail.com",
    license = "MIT",
    scripts = ["bin/douban-album-dl"],
    keywords = "douban dl",
    packages = find_packages(exclude = ["tests"])
)
