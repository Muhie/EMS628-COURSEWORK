### EMS628U COURSEWORK - Muhie Al Haimus

File directory structure
ar_test:
  ├── ar_test
  │   ├── compute_cubic_coeffs.py
  │   ├── cubic_traj_planner.py
  │   ├── __init__.py
  │   ├── plot_cubic_traj.py
  │   └── points_generator.py
  ├── build
  │   ├── ar_test
  │   │   ├── ar_test.egg-info
  │   │   │   ├── dependency_links.txt
  │   │   │   ├── entry_points.txt
  │   │   │   ├── PKG-INFO
  │   │   │   ├── requires.txt
  │   │   │   ├── SOURCES.txt
  │   │   │   ├── top_level.txt
  │   │   │   └── zip-safe
  │   │   ├── build
  │   │   │   └── lib
  │   │   │       └── ar_test
  │   │   │           └── __init__.py
  │   │   ├── colcon_build.rc
  │   │   ├── colcon_command_prefix_setup_py.sh
  │   │   ├── colcon_command_prefix_setup_py.sh.env
  │   │   ├── install.log
  │   │   └── prefix_override
  │   │       ├── __pycache__
  │   │       │   └── sitecustomize.cpython-310.pyc
  │   │       └── sitecustomize.py
  │   └── COLCON_IGNORE
  ├── install
  │   ├── ar_test
  │   │   ├── lib
  │   │   │   ├── ar_test
  │   │   │   │   └── points_generator
  │   │   │   └── python3.10
  │   │   │       └── site-packages
  │   │   │           ├── ar_test
  │   │   │           │   ├── __init__.py
  │   │   │           │   └── __pycache__
  │   │   │           │       └── __init__.cpython-310.pyc
  │   │   │           └── ar_test-0.0.0-py3.10.egg-info
  │   │   │               ├── dependency_links.txt
  │   │   │               ├── entry_points.txt
  │   │   │               ├── PKG-INFO
  │   │   │               ├── requires.txt
  │   │   │               ├── SOURCES.txt
  │   │   │               ├── top_level.txt
  │   │   │               └── zip-safe
  │   │   └── share
  │   │       ├── ament_index
  │   │       │   └── resource_index
  │   │       │       └── packages
  │   │       │           └── ar_test
  │   │       ├── ar_test
  │   │       │   ├── hook
  │   │       │   │   ├── ament_prefix_path.dsv
  │   │       │   │   ├── ament_prefix_path.ps1
  │   │       │   │   ├── ament_prefix_path.sh
  │   │       │   │   ├── pythonpath.dsv
  │   │       │   │   ├── pythonpath.ps1
  │   │       │   │   └── pythonpath.sh
  │   │       │   ├── package.bash
  │   │       │   ├── package.dsv
  │   │       │   ├── package.ps1
  │   │       │   ├── package.sh
  │   │       │   ├── package.xml
  │   │       │   └── package.zsh
  │   │       └── colcon-core
  │   │           └── packages
  │   │               └── ar_test
  │   ├── COLCON_IGNORE
  │   ├── local_setup.bash
  │   ├── local_setup.ps1
  │   ├── local_setup.sh
  │   ├── _local_setup_util_ps1.py
  │   ├── _local_setup_util_sh.py
  │   ├── local_setup.zsh
  │   ├── setup.bash
  │   ├── setup.ps1
  │   ├── setup.sh
  │   └── setup.zsh
  ├── launch
  │   └── cubic_traj_gen.launch.py
  ├── log
  │   ├── build_2026-03-08_17-38-08
  │   │   ├── ar_test
  │   │   │   ├── command.log
  │   │   │   ├── stderr.log
  │   │   │   ├── stdout.log
  │   │   │   ├── stdout_stderr.log
  │   │   │   └── streams.log
  │   │   ├── events.log
  │   │   └── logger_all.log
  │   ├── COLCON_IGNORE
  │   ├── latest -> latest_build
  │   └── latest_build -> build_2026-03-08_17-38-08
  ├── package.xml
  ├── resource
  │   └── ar_test
  ├── setup.cfg
  ├── setup.py
  └── test
      ├── test_copyright.py
      ├── test_flake8.py
      └── test_pep257.py

ar_interface:
  ├── CMakeLists.txt
  ├── include
  │   └── ar_interface
  ├── LICENSE
  ├── msg
  │   ├── CubicTrajCoeffs.msg
  │   └── CubicTrajParams.msg
  ├── package.xml
  ├── src
  └── srv
      └── ComputeCubicTraj.srv
