from models import Player, Labyrinthe, Case

from sys import exit

def resolve(player: Player, lab: Labyrinthe):
    player.can_travel_fast = True
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            actual_coordinates = player.get_coordinates()
            if actual_coordinates not in player.visited:
                player.visited.append(actual_coordinates)

            for case in player.adjacent_cases(lab):
                if case['case'].status != Case.STATUS_WALL and case['coordinates'] not in player.visited and case['coordinates'] not in player.path:
                    player.path.append(case['coordinates'])
                if case['case'].status == Case.STATUS_GOAL:
                    player.path[-1] = case['coordinates']
                    break
                    
            lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
            player.move_to(player.path.pop(0))
                
        except KeyboardInterrupt:
            exit()
            
    lab.show(player)
    print('Finished!')
    input('Press Enter to continue...\n')