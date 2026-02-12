from glob import glob
import os

from setuptools import find_packages
from setuptools import setup

package_name = "autoware_carla_interface_ub"

setup(
    name=package_name,
    version="0.43.0",
    packages=find_packages(where="src"),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (os.path.join("share", package_name), ["package.xml"]),
        (os.path.join("share", package_name), glob("config/*")),
        (os.path.join("share", package_name), glob("calibration_maps/*.csv")),
        (os.path.join("share", package_name), glob("launch/*.launch.xml")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Anurag Hruday",
    maintainer_email="anurag.hruday@gmail.com",
    description="CARLA ROS 2 bridge for AUTOWARE (University at Buffalo, CAVAS Lab - Digital Twin)",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "autoware_carla_interface_ub = autoware_carla_interface_ub.carla_autoware:main"
        ],
    },
    package_dir={"": "src"},
)
