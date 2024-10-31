class Computer:
    name = "HP"

    def __init__(self, ram, processor):
        self.ram = ram
        self.processor = processor

    def info(self):
        print(f"{self.ram}-----{self.processor}")

comp1 = Computer("4G", "2")
comp2 = Computer("4gb", "8")

comp1.info()
comp2.info()
