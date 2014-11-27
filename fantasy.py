
class fantasy_league(object):

    def __init__(self,coaches_file, players_file):
        coaches = Set()
        forwards = Set()
        guards = Set()
        centers = Set()
        person_to_value = {}
        person_to_price = {}
        
        coaches_reader = open(coaches_file,"w")
        for line in coaches_reader:
            line.split(',')
            coaches.add(line[4])
            person_to_value[line[4]] = float(line[1])
            person_to_price[line[4]] = float(line[0])

        players_reader = open(players_file,"w")
        for line in players_reader:
            line.split(',')
            player = line[4]
            person_to_value[player]] = float(1)
            person_to_price[player] = float(0)
            
            if line[2] = 'guard':
                guards.add(player)
            if line[2] = 'center':
                centers.add(player)
            if line[2] = 'forward':
                forwards.add(player)

        def find_value(self):    
            for coach in coaches:
                for forward_one in forwards:
                    for forward_two in forwards:
                        for forward_three in forwards:
                            for guard_one in guards:
                                for guard_two in guards:                    
                                    for guard_three in guards:
                                        for center_one in centers:
                                            for center_two in centers:
                                                price = calculate_price(self,coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)
                                                value = calculate_value(self,coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)
                                                if price < 450:
                                                    if value > cur_value:
                                                        cur_value = value
                                                        cur_list = []
                                                        cur_list.add(coach)
                                                        cur_list.add(forward_one)
                                                        cur_list.add(forward_two)
                                                        cur_list.add(forward_three)
                                                        cur_list.add(guard_one)
                                                        cur_list.add(guard_two)
                                                        cur_list.add(guard_three)
                                                        cur_list.add(center_one)
                                                        cur_list.add(center_two)
    print cur_list


    def calculate_price(self,one,two,three,four,five,six,seven,eight,nine):
        return self.person_to_price[one] + self.person_to_price[two] + self.person_to_price[three] + self.person_to_price[four] + self.person_to_price[five] + self.person_to_price[six] + self.person_to_price[seven] + self.person_to_price[eight] + self.person_to_price[nine]

    def calculate_value(self,one,two,three,four,five,six,seven,eight,nine):
        return self.person_to_value[one] + self.person_to_value[two] + self.person_to_value[three] + self.person_to_value[four] + self.person_to_value[five] + self.person_to_value[six] + self.person_to_value[seven] + self.person_to_value[eight] + self.person_to_value[nine]



cur_fantasy = fantasy_league()

fantasy_league.find_value()

