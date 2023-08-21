# Implementor
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Concrete Implementor


class TV(Device):
    def turn_on(self):
        print("TV is turned on")

    def turn_off(self):
        print("TV is turned off")


class Radio(Device):
    def turn_on(self):
        print("Radio is turned on")

    def turn_off(self):
        print("Radio is turned off")

# Abstraction


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

# Refined Abstraction


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Device is muted")


# Client code
if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote_tv = RemoteControl(tv)
    remote_radio = RemoteControl(radio)

    remote_tv.turn_on()  # Output: TV is turned on
    remote_tv.turn_off()  # Output: TV is turned off

    remote_radio.turn_on()  # Output: Radio is turned on
    remote_radio.turn_off()  # Output: Radio is turned off

    advanced_remote_tv = AdvancedRemoteControl(tv)
    advanced_remote_tv.turn_on()  # Output: TV is turned on
    advanced_remote_tv.turn_off()  # Output: TV is turned off
    advanced_remote_tv.mute()  # Output: Device is muted
