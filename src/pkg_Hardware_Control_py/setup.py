from setuptools import find_packages, setup

package_name = 'pkg_Hardware_Control_py'

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
            'node_Hardware_Drive = pkg_Hardware_Control_py.node_Hardware_Drive:main',
            'node_State_Publisher = pkg_Hardware_Control_py.node_State_Publisher:main'
        ],
    },
)
