from setuptools import setup
setup(app=["main.py"],options={"py2app":{"argv_emulation":True}},setup_requires=["py2app"])