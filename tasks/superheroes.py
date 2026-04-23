
#Younes Bendani

class Superhero:
    def __init__(self, name, powers, origin, friends, age, is_good=True):
        self.name = name
        self.powers = list(powers)
        self.origin = origin
        self.friends = friends
        self.age = age
        self.is_good = is_good
        self.energy = 100

    def print_name(self):
        alignment = "Gentil" if self.is_good else "Méchant"
        print(f"Nom: {self.name} [{alignment}]")

    def print_attributes(self):
        alignment = "Gentil" if self.is_good else "Méchant"
        print(f"\n--- Fiche de {self.name} ---")
        print(f"Alignement : {alignment}")
        print(f"Pouvoirs   : {', '.join(self.powers)}")
        print(f"Origine    : {self.origin}")
        print(f"Amis       : {self.friends}")
        print(f"Âge        : {self.age}")
        print(f"Énergie    : {self.energy}/100")

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def control_gravity(self):
        if self.energy >= 30:
            self.add_power("Contrôle Gravitationnel")
            self.energy -= 30
            print(f"{self.name} manipule la gravité !")
        else:
            print(f"{self.name} manque d'énergie.")

    def time_travel(self):
        if self.energy >= 80:
            self.add_power("Voyage Temporel")
            self.energy -= 80
            print(f"{self.name} voyage dans le temps !")
        else:
            print(f"{self.name} n'a pas assez d'énergie.")

    def control_spiders(self):
        if self.energy >= 15:
            self.add_power("Contrôle des araignées")
            self.energy -= 15
            print(f"{self.name} commande aux araignées !")

    def symbiote_morph(self):
        if self.energy >= 25:
            self.add_power("Métamorphose Symbiotique")
            self.energy -= 25
            print(f"Le symbiote de {self.name} change de forme !")


if __name__ == "__main__":
    scarlet_spider = Superhero("Scarlet Spider", ["Agilité"], "Clone", "Peter Parker", 25, True)
    agent_venom = Superhero("Agent Venom", ["Force"], "Militaire", "Flash Thompson", 30, True)

    scarlet_spider.control_spiders()
    scarlet_spider.control_gravity()
    
    agent_venom.symbiote_morph()
    agent_venom.time_travel()

    scarlet_spider.print_attributes()
    agent_venom.print_attributes()