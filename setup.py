from setuptools import setup, find_packages

setup(
    name="UPS Display Server",
    version="1.0.0",
    description="Display server for monitoring current,voltage, power and capacity left of the UPS."
                "With auto power off at low capacity",
    packages=find_packages(),
    install_requires=[
        "Adafruit_SSD1306"
    ],
)
