

'''

     Each table row contains result of one team (lexicografy sorted). First column has number of the team.
     Second colum contains the name of team, Then there are as many columns as teams. 
     These columns have further information: 
     if the team won, then cell has "W" letter.
     If the team loose, then cell has "L" letter.
     If teams played on draw, then cell has "D" letter
     If teams didn't play each other, then cell has a space.
     If the cell belong the same team, then cell has a "X" letter. 
    
    Next column is for team's points. The team is awarded for 3 poins For each victory. 
    The team is awarded for 1 point for each draw. Otherwise - 0 point.
    
    The last column is for place. 
    A team "A" wins higher placce then team "B" if team "A" has more points or team "A" and team "B" have the same points but team "A" has more victories then team "B".
    

    +-+----------+-+-+-+-+-+-+-+-+
   |1|C         |X|L| |D| | |1|3|
   +-+----------+-+-+-+-+-+-+-+-+
   |2|Cplusplus |W|X| | | |W|6|1|
   +-+----------+-+-+-+-+-+-+-+-+
   |3|Haskell   | | |X|D| | |1|3|
   +-+----------+-+-+-+-+-+-+-+-+
   |4|Java      |D| |D|X|D|W|6|2|
   +-+----------+-+-+-+-+-+-+-+-+
   |5|Perl      | | | |D|X| |1|3|
   +-+----------+-+-+-+-+-+-+-+-+
   |6|Php       | |L| |L| |X|0| |
   +-+----------+-+-+-+-+-+-+-+-+
    '''


class YandexTest():
    games = list()
    teams = dict()
    tournament_table = dict()
    places = {0: [999, 999], 1: [0, 0], 2: [0, 0], 3: [0, 0]}

    def perform_source(self, source):
        for game in source:
            c1 = game[:game.find('-')]
            c2 = game[len(c1)+1:game.find('-', len(c1)+1)]
            r1 = game[len(c1)+len(c2)+2:game.find(':')]
            r2 = game[len(c1)+len(c2)+len(r1)+3:]
            self.games.append({"c1": c1.strip(), "c2": c2.strip(
            ), "r1": int(r1.strip()), "r2": int(r2.strip())})

        teams = set()
        for games in self.games:
            teams.add(games["c1"])
            teams.add(games["c2"])
        teams = sorted(teams)
        for x in range(len(teams)):
            c = {'c'+str(z+1): ' ' for z in range(len(teams))}
            c['n'] = x+1
            c['total'] = 0
            c['place'] = " "
            c['victories'] = 0
            c["c"+str(c["n"])] = "X"
            self.tournament_table[teams[x]] = c

        return

    def get_place(self, current_step: int, max_step: int):
        if current_step > max_step:
            return
        prevoius_step = current_step - 1
        place_count = 0
        place_vict = 0
        for tt in self.tournament_table:
            cur_count = self.tournament_table[tt]['total']
            cur_vict = self.tournament_table[tt]['victories']
            prev_count = self.places[prevoius_step][0]
            prev_vict = self.places[prevoius_step][1]

            if (place_count < cur_count <= prev_count and cur_vict < prev_vict) or \
                    (place_count == cur_count <= prev_count and cur_vict < prev_vict and cur_vict > place_vict):
                place_count = cur_count
                place_vict = cur_vict
        if place_count == 0:
            return
        self.places[current_step] = [place_count, place_vict]
        self.get_place(current_step + 1, max_step)

    def print_tournament_table(self):
        num_commands = len(self.tournament_table)
        string_out = "-+--+" + \
            "-".rjust(29, "-") + "+-"*num_commands + "+--+-"
        print(string_out)
        for c in self.tournament_table:
            string_out = "|" + str(self.tournament_table[c]["n"]).rjust(2, " ") + "|" \
                + c.ljust(30, " ")
            for x in range(num_commands):
                string_out += "|" + self.tournament_table[c]["c" + str(x+1)]

            string_out += "|" + \
                str(self.tournament_table[c]["total"]).rjust(2, " ")
            string_out += "|" + str(self.tournament_table[c]["place"]) + "|"
            print(string_out)
        string_out = "-+--+" + \
            "-".rjust(29, "-") + "+-"*num_commands + "+--+-"
        print(string_out)

    def show_tournament_table(self, source):
        self.perform_source(source)
        for game in self.games:
            if game["r1"] > game["r2"]:
                self.tournament_table[game["c1"]]["total"] += 3
                self.tournament_table[game["c1"]]["victories"] += 1
                self.tournament_table[game["c1"]]["c" +
                                                  str(self.tournament_table[game["c2"]]["n"])] = "W"
                self.tournament_table[game["c2"]]["c" +
                                                  str(self.tournament_table[game["c1"]]["n"])] = "L"
            elif game["r2"] > game["r1"]:
                self.tournament_table[game["c2"]]["total"] += 3
                self.tournament_table[game["c2"]]["victories"] += 1
                self.tournament_table[game["c2"]]["c" +
                                                  str(self.tournament_table[game["c1"]]["n"])] = "W"
                self.tournament_table[game["c1"]]["c" +
                                                  str(self.tournament_table[game["c2"]]["n"])] = "L"
            else:
                self.tournament_table[game["c1"]]["total"] += 1
                self.tournament_table[game["c2"]]["total"] += 1
                self.tournament_table[game["c1"]]["c" +
                                                  str(self.tournament_table[game["c2"]]["n"])] = "D"
                self.tournament_table[game["c2"]]["c" +
                                                  str(self.tournament_table[game["c1"]]["n"])] = "D"
        self.get_place(1, 3)
        for c in self.tournament_table:
            for place in range(len(self.places)):
                if self.tournament_table[c]["total"] == self.places[place][0] and \
                        self.tournament_table[c]["victories"] == self.places[place][1]:
                    self.tournament_table[c]["place"] = place

        self.print_tournament_table()


source = ['Cplusplus - C - 1:0',
          'Cplusplus - Php - 2:0',
          'Java - Php - 1:0',
          'Java - C - 2:2',
          'Java - Perl - 1:1',
          'Java - Haskell - 1:1']
yandex_test = YandexTest()
yandex_test.show_tournament_table(source)
