import os
import sys

from setuptools import setup, find_packages

sys.path.append('.')
from gitconfig_parser import metadata


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.authors[0],
    author_email=metadata.emails[0],
    maintainer=metadata.authors[0],
    maintainer_email=metadata.emails[0],
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    download_url=metadata.url,
    # Find a list of classifiers here:
    # <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,  # don't use eggs
    entry_points={
        'console_scripts': [
            'gitconfig_parser_cli = gitconfig_parser.main:main'
        ],
        # if you have a gui, use this
        # 'gui_scripts': [
        #     'gitconfig_parser_gui = gitconfig_parser.gui:main'
        # ]
    }
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
