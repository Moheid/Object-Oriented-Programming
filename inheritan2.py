class TelecomService:
    def __init__(self, service_id, base_cost):
        self.service_id = service_id
        self.base_cost = base_cost
    
    def calculate_monthly_charge(self):
        return self.base_cost
    
    def __str__(self):
        return f"Service {self.service_id} (${self.base_cost}/month)"

class MobileDataPlan(TelecomService):
    def __init__(self, service_id, base_cost, data_limit):
        super().__init__(service_id, base_cost)
        self.data_limit = data_limit  # in GB
    
    def calculate_monthly_charge(self):
        return self.base_cost + (self.data_limit * 0.50)  # $0.50/GB
    
    def __str__(self):
        return f"{super().__str__()} - {self.data_limit}GB data"

class VoIPService(TelecomService):
    def __init__(self, service_id, base_cost, included_minutes):
        super().__init__(service_id, base_cost)
        self.included_minutes = included_minutes
    
    def calculate_monthly_charge(self, minutes_used):
        extra = max(0, minutes_used - self.included_minutes) * 0.10
        return self.base_cost + extra

# Usage
basic_plan = TelecomService("BASIC", 15.00)
print(basic_plan)  # Service BASIC ($15.00/month)

data_plan = MobileDataPlan("DATA5", 20.00, 5)
print(data_plan)  # Service DATA5 ($20.00/month) - 5GB data
print(data_plan.calculate_monthly_charge())  # 22.5

voip = VoIPService("VOIP20", 12.00, 200)
print(voip.calculate_monthly_charge(250))  # 12 + (50 * 0.10) = 17.0