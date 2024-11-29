# Another Example of Abstraction: Vehicle Service System
# Consider a vehicle service system where different types of services (oil change, tire rotation) are offered.
# Users of the service system only need to know about the service type, not the internal process.
from abc import ABC, abstractmethod

class Service(ABC):  # Abstract class for service types
    @abstractmethod
    def perform_service(self):
        # Abstract method to be implemented by subclasses
        pass

class OilChange(Service):
    def perform_service(self):
        # Specific implementation for oil change service
        print("Performing oil change...")

class TireRotation(Service):
    def perform_service(self):
        # Specific implementation for tire rotation service
        print("Performing tire rotation...")

# Usage example
service1 = OilChange()
service1.perform_service()  # Output -> Performing oil change...

service2 = TireRotation()
service2.perform_service()  # Output -> Performing tire rotation...