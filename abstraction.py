from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass

class Router(NetworkDevice):
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Router {self.ip_address} connected"
    
    def disconnect(self):
        self.connected = False
        return f"Router {self.ip_address} disconnected"
    
    def get_status(self):
        return "Active" if self.connected else "Inactive"

class Switch(NetworkDevice):
    def __init__(self, switch_id):
        self.switch_id = switch_id
        self.ports = {}
    
    def connect(self):
        return f"Switch {self.switch_id} initialized"
    
    def disconnect(self):
        return f"Switch {self.switch_id} powered down"
    
    def get_status(self):
        return f"Switch {self.switch_id} with {len(self.ports)} active ports"

# Usage
router = Router("192.168.1.1")
print(router.connect())  # Router 192.168.1.1 connected
print(router.get_status())  # Active

switch = Switch("SW-01")
print(switch.connect())  # Switch SW-01 initialized