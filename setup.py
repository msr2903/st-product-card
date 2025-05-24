import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-product-card",
    version="0.1.2",
    author="msr2903",
    author_email="michaelpersonal67@gmail.com",
    description="An e-commerce product card component for Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msr2903/st-productcard",
    packages=setuptools.find_packages(where="."),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        # "Framework :: Streamlit",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=["streamlit>=1.0"],
)