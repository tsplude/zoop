from setuptools import setup

setup(
    name="zoop",
    version=0.1,
    description="This is zoop",
    entry_points={
        'console_scripts': [
            'zoop = zoop.__main__:main'
        ]
    }
)
