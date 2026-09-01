from setuptools import find_packages, setup

package_name = 'jacobian_online_estimator'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/bringup.launch.py']),
        ('share/' + package_name + '/config', ['config/params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Online Jacobian estimation (Broyden / Kalman) for an uncalibrated robot arm using a fixed eye-to-hand camera.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_interface_node = jacobian_online_estimator.joint_interface_node:main',
            'aruco_pose_node = jacobian_online_estimator.aruco_pose_node:main',
            'jacobian_estimator_node = jacobian_online_estimator.jacobian_estimator_node:main',
            'visual_servo_controller_node = jacobian_online_estimator.visual_servo_controller_node:main',
        ],
    },
)
