from sets import Set

class fantasy_league(object):

    def __init__(self,coaches_file, players_file):
        self.coaches = Set()
        self.forwards = Set()
        self.guards = Set()
        self.centers = Set()
        self.person_to_value = {}
        self.person_to_price = {}
        
        coaches_reader = open(coaches_file,"r")
        for line in coaches_reader:
            split_line = line.split(',')
            person = int(split_line[3])
            self.coaches.add(person)
            self.person_to_value[person] = float(split_line[1])
            self.person_to_price[person] = float(split_line[0])

        players_reader = open(players_file,"r")
        for line in players_reader:
            split_line = line.split(',')
            player = int(split_line[3])
            self.person_to_value[player] = float(split_line[1])
            self.person_to_price[player] = float(split_line[0])
            
            if split_line[2] == 'guard':
                self.guards.add(player)
            if split_line[2] == 'center':
                self.centers.add(player)
            if split_line[2] == 'forward':
                self.forwards.add(player)

    def find_value(self):    
        cur_set = Set()
        cur_value = 0 
        for coach in self.coaches:
            for forward_one in self.forwards:
                for forward_two in self.forwards:
                    for forward_three in self.forwards:
                        for guard_one in self.guards:
                            for guard_two in self.guards:                    
                                for guard_three in self.guards:
                                    for center_one in self.centers:
                                        for center_two in self.centers:
                                            price = self.calculate_price(coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)
                                            value = self.calculate_value(coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)
                                            if price < 451:
                                                if value > cur_value:
                                                    cur_value = value
                                                    cur_list = Set()
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



cur_fantasy = fantasy_league('f_coaches_analyzed.csv','f_players_processed.csv')

cur_fantasy.find_value()

