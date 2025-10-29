from setuptools import find_packages, setup

package_name = 'pkg_pub_sub'

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
    maintainer_email='tobyzrf1997@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'wheels = pkg_pub_sub.wheels:main',
            'speed_controller = pkg_pub_sub.speed_controller:main',
            'speed_plotter = pkg_pub_sub.speed_plotter:main',
            'number_publisher = pkg_pub_sub.number_publisher:main',
            'number_counter = pkg_pub_sub.number_counter:main'
            
        ],
    },
)
