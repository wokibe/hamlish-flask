import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hamlish_Flask",
    version="0.1.6",
    author="Wolfgang Kittenberger",
    author_email="wolfkibe@gmail.com",
    description="Enable HAML syntax in Flask application templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wokibe/hamlish-flask",
    py_modules=['hamlish_flask'],
    license="MIT",
    install_requires=['hamlish_jinja'],
    keywords = "flask jinja2 templates haml",
    platforms='any',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
