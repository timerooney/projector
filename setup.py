import setuptools

requirements = [
    'networkx',
    'pygraphviz'
]

dev_requirements = [
    'pytest'
]

setuptools.setup(
    name='projector',
    version='0.0.1',
    author='Tim Rooney',
    author_email='timothyrooney93@gmail.com',
    packages=requirements,
    extras_require = {
        'dev': dev_requirements
    }
)
