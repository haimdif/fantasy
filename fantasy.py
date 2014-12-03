from sets import Set

class fantasy_league(object):

    def __init__(self,coaches_file, players_file):
        self.coaches = Set()
        self.forwards = Set()
        self.guards = Set()
        self.centers = Set()
        self.person_to_value = {}
        self.person_to_price = {}
        self.items = [] 
        
        coaches_reader = open(coaches_file,"r")
        for line in coaches_reader:
            split_line = line.split(',')
            person = int(split_line[3])
            self.coaches.add(person)
            self.person_to_value[person] = float(split_line[1])
            self.person_to_price[person] = float(split_line[0])                                              # 1010101000
#            self.items.append( (person,int(self.person_to_price[person])+1000 , self.person_to_value[person] +1000000000) )
            
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
                
        guard_set = Set()        
        for guard_one in self.guards:
            for guard_two in self.guards:
                for guard_three in self.guards:
                        guard_set.add( (guard_one,guard_two,guard_three) )
                        
        centers_set = Set()
        for center_one in self.centers:
            for center_two in self.centers:
                centers_set.add( (center_one,center_two ) )
                
        forwards_set = Set()
        for forward_one in self.forwards:
            for forward_two in self.forwards:
                for forward_three in self.forwards:
                    forwards_set.add( (forward_one, forward_two, forward_three) )
        
        for guard in guard_set:                                                                                                                    # 1010101000     
            self.items.append( ( guard, int(self.person_to_price[guard[0]] + self.person_to_price[guard[1]]  + self.person_to_price[guard[2]])+1000, 
            1000  +self.person_to_value[guard[0]] + self.person_to_value[guard[1]]  + self.person_to_value[guard[2]] ))
            
        for forward in forwards_set:
            self.items.append( ( forward, int(self.person_to_price[forward[0]] + self.person_to_price[forward[1]]  + self.person_to_price[forward[2]])+1000, 1000  +self.person_to_value[forward[0]] + self.person_to_value[forward[1]] + self.person_to_value[forward[2]] ))

        for center in centers_set:                                                                                   # 1010101000
            self.items.append( ( center, int(self.person_to_price[center[0]] + self.person_to_price[center[1]])+1000, 1000  +self.person_to_value[center[0]] + self.person_to_value[center[1]] ))

#        self.items.append( (player,int(self.person_to_price[player])+1000 ,self.person_to_value[player] +1000) )
        
    def find_value(self):    
        cur_set = Set()
        cur_value = 0 
        index = 0 
        coach = 1002
        center_one = 2
        center_two = 3
        forward_one = 53
        if 1 == 1:
            for forward_two in self.forwards:
                for forward_three in self.forwards:
                    for guard_one in self.guards:
                        for guard_two in self.guards:                    
                            for guard_three in self.guards:
                                price = self.calculate_price(coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)
                                value = self.calculate_value(coach,forward_one, forward_two, forward_three, guard_one,guard_two, guard_three, center_one, center_two)

                                if index % 10000 == 0:
                                    print index, len(self.forwards)*len(self.forwards)*len(self.guards)*len(self.guards)*len(self.guards)
                                            
                                index = index + 1 

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

    def knapsack01_dp(self, limit):
        items = self.items
        table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
        for j in xrange(1, len(items) + 1):
            item, wt, val = items[j-1]
            for w in xrange(1, limit + 1):
                if wt > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w], table[j-1][w-wt] + val)
 
        result = []
        w = limit
        for j in range(len(items), 0, -1):
            was_added = table[j][w] != table[j-1][w]
 
            if was_added:
                item, wt, val = items[j-1]
                result.append(items[j-1])
                w -= wt
 
        return result
        
            
            
    


cur_fantasy = fantasy_league('f_coaches_analyzed.csv','f_players_processed.csv')

#cur_fantasy.find_value()
                              # 1010101000
print cur_fantasy.knapsack01_dp(8420)

