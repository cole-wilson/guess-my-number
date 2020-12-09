#!/usr/bin/env python3

# +------------------------+                       
# | Created with ShipSnake |                       
# |                        |                       
# | Do not edit this file  |                       
# | directly. Insead       |                       
# | you should edit the    |                       
# | `shipsnake.toml` file. |                       
# +------------------------+    

import setuptools

try:
  with open("README.md", "r") as fh:
      long_description = fh.read()
except:
	long_description = "# Guess My Number\nA guess my number game.\n### Contributors\n- Cole Wilson\n### Contact\n<cole@colewilson.xyz> "

setuptools.setup(
    name="guess-my-number",
    version="0.0.2",
		scripts=['bin/guess-my-number'],
#		entry_points={
#			'console_scripts': ['guess-my-number=guess-my-number.__main__'],
#		},
    author="Cole Wilson",
    author_email="cole@colewilson.xyz",
    description="A guess my number game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
		install_requires=[''],
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.6',
		package_data={"": [''],},
		license="",
		keywords='',
)