from setuptools import setup, find_packages

setup(
    name="codebase",
    version="0.1",
    packages=find_packages(include=["codebase", "codebase.*"]),  # Explicitly include only your package
    install_requires=[
        "numpy"
    ],
)