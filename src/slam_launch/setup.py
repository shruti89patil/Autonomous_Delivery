from setuptools import setup

package_name = 'slam_launch'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files=[
        ('share/' + package_name + '/launch', ['launch/slam_toolbox_launch.py']),
        ('share/' + package_name + '/config', ['config/slam_params.yaml']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@domain.com',
    description='SLAM Toolbox launcher',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
