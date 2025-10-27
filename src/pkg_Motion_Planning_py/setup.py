from setuptools import find_packages, setup

package_name = 'pkg_Motion_Planning_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rz',
    maintainer_email='rz@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node_Motion_Planning = pkg_Motion_Planning_py.node_Motion_Planning:main',
            'node_Path_Correction = pkg_Motion_Planning_py.node_Path_Correction:main'
        ],
    },
)
