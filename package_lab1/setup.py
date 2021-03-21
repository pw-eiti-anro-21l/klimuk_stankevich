from setuptools import setup

package_name = 'package_lab1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stanislau',
    maintainer_email='stankevich.slava@inbox.ru',
    description='Package to manipulate turtle',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sterowanie_zolwiem = package_lab1.sterowanie_zolwiem:main'
        ],
    },
)
