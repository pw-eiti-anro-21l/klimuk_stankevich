import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
package_name = 'custom_urdf'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('rviz/*')),
        (os.path.join('share', package_name), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pklimuk',
    maintainer_email='pavelklimuk@yahoo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'calc_params = custom_urdf.calculate_params_node:main',
        	'calculate_joints_coordinates = custom_urdf.DHtoURDF:calculate_joints_coordinates',
        	'NONKDL_DKIN = custom_urdf.NONKDL_DKIN:main',
        	'quaternion = custom_urdf.quaternion.py',
        	'KDL_DKIN = custom_urdf.KDL_DKIN:main',
        	'service = custom_urdf.jint:main',
        	'client = custom_urdf.jint_control_srv:main',
        	'Trajectory_poster = custom_urdf.Trajectory_poster:main',
        	'service2 = custom_urdf.oint:main',
        	'client2 = custom_urdf.oint_control_srv:main',
        	'IKIN = custom_urdf.IKIN:main',
        ],
    },
)
