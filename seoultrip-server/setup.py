from setuptools import find_packages, setup

install_requires = [
    'flask == 0.10.1',
    'sqlalchemy >= 1.0.0, < 1.1',
    'requests == 2.8.0',
    'alembic >= 0.7.4, < 0.9.0',
]


tests_require = [
]


docs_require = [
]


extras_require = {
}


setup(
    name='seoultrip',
    version='0.0.1',
    author='team-seoultrip',
    author_email='noblea1117@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'extras': extras_require,
        'tests': tests_require,
    },
    entry_points='''
        [console_scripts]
        soran = soran.cli:main
    '''
)
