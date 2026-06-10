import setuptools

with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

_version_ = "0.0.0"
REPO_NAME = "AI-Kidney-Health-Assistant"
AUTHOR_USER_NAME = "DEEPAK yadav"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "updeepak222@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CNN Classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
