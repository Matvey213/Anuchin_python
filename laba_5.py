class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):               
        self.amount_of_fuel -= count           
        self.total_weight -= count             
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                      
        return f'Топливо: {self.amount_of_fuel}'
    def get_total_weight(self):                                     
        return f'Масса: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine_status}'

def main():
    Elon_Mask = Rocket(1500, 500, True)
    while Elon_Mask.amount_of_fuel > 0:
        Elon_Mask.spend_fuel(100)
        print(Elon_Mask.get_fuel_level(), end='; ')
        print(Elon_Mask.get_total_weight(), end='; ')
        print(Elon_Mask.get_is_engine_running())
main()
