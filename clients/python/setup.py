from setuptools import find_packages, setup

setup(
    name="scale-llm-engine",
    python_requires=">=3.7",
    version="0.0.0.beta32",
    packages=find_packages(),
    package_data={"scale_llm_engine": ["py.typed"]},
)
