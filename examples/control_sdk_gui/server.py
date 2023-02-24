import socket
import json
import robot_interface as sdk


def main():
    udp = sdk.UDP(0xee, 8080, "192.168.123.161", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 8000))

    while True:
        data, addr = sock.recvfrom(1024)
        data = json.loads(data.decode('utf-8'))

        udp.Recv()
        udp.GetRecv(state)

        cmd.mode = 0
        cmd.gaitType = 0
        cmd.speedLevel = 0
        cmd.footRaiseHeight = 0
        cmd.bodyHeight = 0
        cmd.euler = [0, 0, 0]
        cmd.velocity = [0, 0]
        cmd.yawSpeed = 0.0
        cmd.reserve = 0

        for k, v in data.items():
            setattr(cmd, k, v)

        udp.SetSend(cmd)
        udp.Send()


if __name__ == '__main__':
    main()
