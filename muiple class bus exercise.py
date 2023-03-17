class bus:
    bus_list = []
    def __init__(self, number, route_keyy, driver):
        self.number = number
        self.route_key = route_keyy
        self.driver = driver
        Bus.bus_list.append(self)

    def display_info(self):
        for bus in Bus.bus_list:
            if bus == self:
                print(f"Bus number = {bus.bus.number}"
                      f"with driver {bus.driver}"
                      f"on route {bus.route_key}")




bus1 = bus("2010", "y", "Greg")
bus2 = bus('2011', "p", "Julie")
bus3 = bus("2012", '130', 'bob')




