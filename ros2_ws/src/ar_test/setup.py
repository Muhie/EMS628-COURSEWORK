import os
from setuptools import find_packages, setup

package_name = 'ar_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/cubic_traj_gen.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='muhie',
    maintainer_email='msalhaimus@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'points_generator = ar_test.points_generator:main',
            'compute_cubic_coeffs = ar_test.compute_cubic_coeffs:main',
            'cubic_traj_planner = ar_test.cubic_traj_planner:main',
            'plot_cubic_traj = ar_test.plot_cubic_traj:main',
        ],
    },
)
