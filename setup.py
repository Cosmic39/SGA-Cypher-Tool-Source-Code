from setuptools import setup, find_packages

setup(
    name="minecraft-sga-cipher",
    version="1.0.0",
    description="Encrypt and decrypt messages using Caesar + Minecraft SGA cipher with a seed",
    author="Cosmic",
    packages=find_packages(include=["backend", "gui", "backend.*", "gui.*"]),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "sga-cipher=gui.app:main",  # runs the GUI
        ],
    },
)
