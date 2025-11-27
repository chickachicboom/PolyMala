from prettytable import PrettyTable

class PolymerInformation:
    def __init__(self,polymers_list):
        self.polymers_list = polymers_list
        self.list = 0

    def still_has_polymer(self):
        return self.list < len(self.polymers_list)
    
    def polymer_table(self):
        table = PrettyTable()

        for i in range(len(self.polymers_list)):
            polymer = self.polymers_list[i]
            print(f"{i+1} - {polymer.name}")
        print("\n\nJust press the number of the polymer you'd like to taste--uh,view.")

        order = int(input("-"))
        ordered_polymer = self.polymers_list[order-1]
        table.field_names = [order,ordered_polymer.name]
        table.add_row(['abbreviation',ordered_polymer.abbreviation])
        table.add_row(['monomer',ordered_polymer.monomer])
        table.add_row(['type',ordered_polymer.type])
        table.add_row(['property',ordered_polymer.property])
        table.add_row(['use',ordered_polymer.use])
        table.align = 'l'
        print(table)
    
    def polymer_table_all(self):
        table = PrettyTable()

        current_polymer = self.polymers_list[self.list]
        self.list += 1
        table.field_names = [self.list,current_polymer.name]
        table.add_row(['abbreviation',current_polymer.abbreviation])
        table.add_row(['monomer',current_polymer.monomer])
        table.add_row(['type',current_polymer.type])
        table.add_row(['property',current_polymer.property])
        table.add_row(['use',current_polymer.use])
        table.align = 'l'
        print(f"{table}\n")