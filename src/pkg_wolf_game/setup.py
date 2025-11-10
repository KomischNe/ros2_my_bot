from setuptools import find_packages, setup

package_name = 'pkg_wolf_game'

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
            'game_master = pkg_wolf_game.game_master:main',
            'player1 = pkg_wolf_game.player1:main',
            'player2 = pkg_wolf_game.player2:main',
            'player3 = pkg_wolf_game.player3:main',
            'player4 = pkg_wolf_game.player4:main',
            'player5 = pkg_wolf_game.player5:main',
            'player6 = pkg_wolf_game.player6:main'
        ],
    },
)
