# Unitree Go1

## Useful links

- [Unofficial documentation](https://github.com/MAVProxyUser/YushuTechUnitreeGo1)
- [Control SDK](https://github.com/unitreerobotics/unitree_legged_sdk/tree/v3.8.0)
- [Camera SDK](https://github.com/unitreerobotics/UnitreecameraSDK)
- [ROS package](https://github.com/unitreerobotics/unitree_ros_to_real)
- [Gazebo simulation](https://github.com/unitreerobotics/unitree_ros)

## Control SDK

### With Docker

Docker image with SDK:\
`carbon225/unitree-py`

[Example code](examples/control_sdk_docker)

### Without Docker

Requirements:
- Python 3.8

Get the SDK:

```bash
git clone -b v3.8.0 https://github.com/unitreerobotics/unitree_legged_sdk.git
```

Run the example:

```bash
cd unitree_legged_sdk/example_py
python example_walk.py
```
