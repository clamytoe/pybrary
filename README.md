# eBook Library Parser (*pybrary*)

> *Little script I wrote to parse through my Springer Nature ebook collection*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]
[![Twitter][twitter-image]][twitter-url]

NOTE: This project was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

## Initial setup

```zsh
cd Projects
git clone https://github.com/clamytoe/pybrary.git
cd pybrary
```

### Anaconda setup

If you are an Anaconda user, this command will get you up to speed with the base installation.

```zsh
conda env create
conda activate pybrary
```

### Regular Python setup

If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment. There are many ways to do this, the simplest using *venv*.

```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Final setup

```zsh
pip install -e .
```

## Usage

```zsh
pybrary
```

The output should be: `Successfully installed your project file: pybrary`

## Contributing

Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:

* black
* flake8
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.
If you plan to contribute, make sure that you install the packages listed in the requirements-dev.txt. 

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "pybrary" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.8-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.1.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/pybrary.svg
[issues-url]:https://github.com/clamytoe/pybrary/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/pybrary.svg
[fork-url]:https://github.com/clamytoe/pybrary/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/pybrary.svg
[stars-url]:https://github.com/clamytoe/pybrary/stargazers
[license-image]:https://img.shields.io/badge/license-MIT-blue.svg
[license-url]:https://github.com/clamytoe/pybrary/blob/master/LICENSE
[twitter-image]:https://img.shields.io/twitter/url/https/github.com/clamytoe/pybrary.svg?style=social
[twitter-url]:https://twitter.com/intent/tweet?text=Wow:&url=%5Bobject%20Object%5D
