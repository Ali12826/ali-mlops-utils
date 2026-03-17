from pathlib import Path

import setuptools  # type: ignore

here = Path(__file__).resolve().parent

long_description = ""
readme_path = here / "README.md"
if readme_path.is_file():
    long_description = readme_path.read_text(encoding="utf-8")

setuptools.setup(
    name="ali-mlops-utils",  # Must be unique on PyPI!
    version="0.0.1",
    description="A simple MLOps utility package for my course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ali Hamza",
    author_email="your.email@example.com",
    url="https://github.com/Ali12826/ali-mlops-utils",
    packages=setuptools.find_packages(where="src")
    if (here / "src").is_dir()
    else setuptools.find_packages(),
    package_dir={"": "src"} if (here / "src").is_dir() else {},
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    license="MIT",
    install_requires=[
        # Add your dependencies here, e.g., "numpy", "pandas"
    ],
)
