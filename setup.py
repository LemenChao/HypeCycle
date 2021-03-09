from setuptools import setup

def readme_file():
    with open("README.rst", encoding="utf-8") as rf:
        return rf.read()


setup(
    name="hypecycle",
    version="0.5",
    author="Chaolemen Borjigin ,Sun Zhizhong ，zhang Chen",
    author_email="chaolemen@ruc.edu.cn",
    description="hypecycle is the fundamental package needed for creating, visualizing, and annotating Gartner Hype Cycle with Python",
    packages=["hypecycle"],
    py_modules=["HypeCycle"],
    long_description_content_type=readme_file(),
    url="https://github.com",
    license = "BSD 3",
    install_requires=["numpy>=1.18","matplotlib>=3.3"],
    classifiers=["Programming Language :: Python :: 3"]
)