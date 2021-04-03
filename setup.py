import setuptools

def readme():
    with open('readme.md') as f:
        return f.read()
    
setuptools.setup(
    name="FNNH", # Replace with your own username
    version="0.0.5",
    author="Apratim Ray",
    author_email="apratimr55@gmail.com",
    description="A flexible CNN based Hash Function",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/apratimr/fnn-hash",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="FNNH"),
    py_modules=["FNNH"],
    install_requires = ["numpy"],
    python_requires=">=3.6",
)