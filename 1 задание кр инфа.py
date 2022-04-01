import csv


class Inside_the_magazine:
    head = None

    class Node:
        element = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node


class Type_of_ammo:

    def __init__(self, caliber, weight):
        self.caliber = caliber
        self.weight = weight
        self.power = self.caliber * self.weight
        self.count = 1
        self.a = [self.caliber, self.weight, self.power]

    def __repr__(self):
        return self.a

    def __iter__(self):
        yield self.a


class Magazine(Inside_the_magazine):

    def __init__(self):
        self.count = 0

    def load_the_magazine(self, type_of_ammo):

        caliber = list(type_of_ammo)[0][0]
        weight = list(type_of_ammo)[0][1]
        power = round(caliber * weight)

        if not self.head:
            self.head = self.Node([caliber, weight, power])
            self.count += 1
            return caliber, weight, power
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node([caliber, weight, power])
        self.count += 1

    def send_txt(self):
        with open('Bullets.txt', 'a') as file:
            writer = csv.writer(file)
            node = self.head
            c = 1

            while node.next_node:
                writer.writerow(['Bullet ' + str(c) + str(' :') + ' ' + str(node.element[0]) + ', ' +
                                 str(node.element[1]) + ', ' + str(node.element[2])])
                node = node.next_node
                c += 1
            writer.writerow(['Bullet ' + str(c) + str(' :') + ' ' + str(node.element[0]) + ', ' +
                             str(node.element[1]) + ', ' + str(node.element[2])])

    def amount(self):
        with open('Bullets.txt', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(['The number of bullets in the magazine - ' + str(self.count)])


H2 = Magazine()  # можно программу не запускать, тк в txt файле уже есть данные 'пули'

H1 = Type_of_ammo(6.65, 12)
H11 = Type_of_ammo(5.56, 10)
H111 = Type_of_ammo(40, 3)

H2.load_the_magazine(H1)
H2.load_the_magazine(H11)
H2.load_the_magazine(H111)

H2.send_txt()
H2.amount()
