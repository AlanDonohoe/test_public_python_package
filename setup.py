import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_public_python_package",
    version="1.0.0",
    author="Alan Donohoe",
    author_email="alandonohoe@hotmail.com",
    description="test_public_python_package",
    license="Proprietary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlanDonohoe/test_public_python_package",
    project_urls={
        "Bug Tracker": "https://github.com/AlanDonohoe/test_public_python_package/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)
