def fuel_expense(self):
        fuel_ratio = sum(self.engine.fuel_cost_ratio.values())
        part_of_fuel = self.fuel / fuel_ratio

        total_fuel_price_in_dollars = 0
        for fuel, cost_per_kg in self.engine.fuel_cost_ratio.items():
            fuel_amount = part_of_fuel * (fuel_ratio - 1 if fuel == self.engine.fuel_type.split('/')[0] else 1)
            fuel_price = fuel_amount * cost_per_kg
            total_fuel_price_in_dollars += fuel_price
            print(f"Fuel: {fuel}, Amount: {fuel_amount} kg, Price: ${fuel_price}")

        print(f"Total Fuel Cost: ${round(total_fuel_price_in_dollars)}")