from setuptools import setup


setup(
    name='cldfbench_bouckaert_et_al2018',
    py_modules=['cldfbench_bouckaert_et_al2018'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bouckaert_et_al2018=cldfbench_bouckaert_et_al2018:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
