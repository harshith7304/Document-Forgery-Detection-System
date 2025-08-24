"""
Setup configuration for Indian Document Forgery Detection System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="indian-document-forgery-detection",
    version="1.0.0",
    author="Document Security Research Team",
    author_email="contact@example.com",
    description="Advanced deep learning system for detecting forgeries in Indian identity documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshith7304/proj",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="document-security, forgery-detection, deep-learning, computer-vision, indian-documents",
    project_urls={
        "Bug Reports": "https://github.com/harshith7304/proj/issues",
        "Source": "https://github.com/harshith7304/proj",
    },
)