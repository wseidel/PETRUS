from setuptools import setup, find_packages

setup(
    name="petrus_transcriber",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    author="Wesley Seidel Carvalho",
    author_email="wesley.seidel@gmail.com",
    description="""Pɛtɾʊs is a an online automatic phonetic transcription system for Brazilian Portuguese. 
    For example, Pɛtɾʊs automatically converts a sequence of letters like 
    "descrédito" into a sequence of phones [ʤiskɾɛʤɪtʊ].
    
    This package contains the source code of the Pɛtɾʊs algorithm.
    We create only for convenience and facility of use.

    The original credits of the Pɛtɾʊs algorithm are:
        https://github.com/alessandrobokan/PETRUS

    """,
    url="https://github.com/wseidel/PETRUS/",  # URL do repositório, se houver
)
