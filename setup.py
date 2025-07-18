import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Text-Summarization"
AUTHOR_USER_NAME = "LeonardoCheng"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "leonardoc1118@outlook.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github,com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)