import tkinter as tk
import json
import socket
import time
import threading


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('App')
        self.geometry('400x500')
        self.resizable(False, False)

        self.create_widgets()

        self.data = {
            'mode': 0,
            'gaitType': 0,
            'footRaiseHeight': 0.0,
            'bodyHeight': 0.0,
            'euler': [0.0, 0.0, 0.0],
            'velocity': [0.0, 0.0],
            'yawSpeed': 0.0,
        }

        self.net_thread = threading.Thread(target=self.net_task)
        self.net_thread.start()

    def create_widgets(self):
        self.mode_switch_label = tk.Label(self, text='Mode')
        self.mode_switch_label.pack()
        self.mode_switch = tk.Scale(self, from_=0, to=2, orient=tk.HORIZONTAL, length=200, command=self.mode_switch_callback)
        self.mode_switch.pack()

        self.gait_switch_label = tk.Label(self, text='Gait')
        self.gait_switch_label.pack()
        self.gait_switch = tk.Scale(self, from_=0, to=2, orient=tk.HORIZONTAL, length=200, command=self.gait_switch_callback)
        self.gait_switch.pack()

        self.foot_raise_height_label = tk.Label(self, text='Foot Raise Height')
        self.foot_raise_height_label.pack()
        self.foot_raise_height = tk.Scale(self, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, length=200, command=self.foot_raise_height_callback)
        self.foot_raise_height.pack()

        self.body_height_label = tk.Label(self, text='Body Height')
        self.body_height_label.pack()
        self.body_height = tk.Scale(self, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, length=200, command=self.body_height_callback)
        self.body_height.pack()

        self.pitch_label = tk.Label(self, text='Pitch')
        self.pitch_label.pack()
        self.pitch = tk.Scale(self, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, length=200, command=self.pitch_callback)
        self.pitch.pack()

        self.forward_label = tk.Label(self, text='Forward')
        self.forward_label.pack()
        self.forward = tk.Scale(self, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, length=200, command=self.forward_callback)
        self.forward.pack()

        self.yaw_label = tk.Label(self, text='Yaw')
        self.yaw_label.pack()
        self.yaw = tk.Scale(self, from_=-1.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, length=200, command=self.yaw_callback)
        self.yaw.pack()

    def net_task(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('localhost', 8000))
        while True:
            s.sendall(json.dumps(self.data).encode('utf-8'))
            time.sleep(0.002)

    def mode_switch_callback(self, value):
        self.data['mode'] = int(value)

    def gait_switch_callback(self, value):
        self.data['gaitType'] = int(value)

    def foot_raise_height_callback(self, value):
        self.data['footRaiseHeight'] = float(value)

    def body_height_callback(self, value):
        self.data['bodyHeight'] = float(value)

    def pitch_callback(self, value):
        self.data['euler'][0] = float(value)

    def forward_callback(self, value):
        self.data['velocity'][0] = float(value)

    def yaw_callback(self, value):
        self.data['yawSpeed'] = float(value)


if __name__ == '__main__':
    app = App()
    app.mainloop()
