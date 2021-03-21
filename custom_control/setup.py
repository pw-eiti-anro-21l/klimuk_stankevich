from setuptools import setup
import os
from glob import glob

package_name = 'custom_control'

setup(
    name=package_name,
    version='0.1.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py')),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pklimuk',
    maintainer_email='pavelklimuk@yahoo.com',
    description='Turtlesim custom control',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'custom_controller = custom_control.custom_control_node:main',
        ],
    },
)
