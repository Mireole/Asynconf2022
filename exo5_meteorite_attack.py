# Mireole#8364
# Exercice 5 : Attaque de météorite

# Quick explanation of the algorithm:
# It works with steps.
# At each step, the algorithm will try to move the spaceship in every direction.
# Each direction is a new map, and we get rid of the old map.
# Once every solution is found, we stop and return the fastest one.
# It is really not optimized, but I did it all by myself so I am proud of it.

import copy


class Map:
    def __init__(self, rows):
        self.row_length = len(rows[0])
        # Assert that all rows have the same length
        assert all(len(row) == self.row_length for row in rows)
        # 1D map (easier to process)
        self.map = ''.join(rows)
        self.spaceship_pos = self.map.find('X')
        self.destination_pos = self.map.find('V')
        self.steps = []
        self.steps.append(self.pos_to_coords(self.spaceship_pos))

    def pos_to_coords(self, pos):
        """Converts the 1D pos to 2D coords"""
        return chr(ord('A') + (pos % self.row_length)) + str(pos // self.row_length + 1)

    def _can_move(self, amount):
        """Internal method, returns True if the spaceship can move by the given amount (more of a teleportation)"""
        if self.spaceship_pos + amount < 0 or self.spaceship_pos + amount >= len(self.map):
            return False
        return self.map[self.spaceship_pos + amount] == '_' or self.map[self.spaceship_pos + amount] == 'V'

    def _move(self, amount):
        """Internal method, teleports the spaceship by the given amount"""
        new_spaceship_pos = self.spaceship_pos + amount
        self.map = self.map[:self.spaceship_pos] + '/' + self.map[self.spaceship_pos + 1:]  # Prevent going back
        self.spaceship_pos = new_spaceship_pos
        self.steps.append(self.pos_to_coords(self.spaceship_pos))

    def clone_up(self):
        """Create a copy of itself if it can move up, and return it"""
        if self._can_move(-self.row_length):
            new_map = copy.deepcopy(self)
            new_map._move(-self.row_length)
            return new_map
        return False

    def clone_down(self):
        """Create a copy of itself if it can move down, and return it"""
        if self._can_move(self.row_length):
            new_map = copy.deepcopy(self)
            new_map._move(self.row_length)
            return new_map
        return False

    def clone_left(self):
        """Create a copy of itself if it can move left, and return it"""
        if self._can_move(-1):
            new_map = copy.deepcopy(self)
            new_map._move(-1)
            return new_map
        return False

    def clone_right(self):
        """Create a copy of itself if it can move right, and return it"""
        if self._can_move(1):
            new_map = copy.deepcopy(self)
            new_map._move(1)
            return new_map
        return False

    def is_finished(self):
        """Returns True if the spaceship is on the destination"""
        return self.spaceship_pos == self.destination_pos


def main():
    rows = []
    print('Entrez la carte (vide pour terminer) :')
    while True:
        row = input("> ")
        if row == '':
            break
        rows.append(row)
    base_map = Map(rows)

    maps = [base_map]
    finished_maps = []
    while True:
        new_maps = []
        for map in maps:
            if map.is_finished():
                # We found a solution. Yay!
                finished_maps.append(map)
            else:
                # Continue exploring
                up = map.clone_up()
                if up:
                    new_maps.append(up)

                down = map.clone_down()
                if down:
                    new_maps.append(down)

                left = map.clone_left()
                if left:
                    new_maps.append(left)

                right = map.clone_right()
                if right:
                    new_maps.append(right)

        maps = new_maps
        if len(maps) == 0:
            break
    # Get the fastest solution
    fastest_map = min(finished_maps, key=lambda space_map: len(map.steps))
    # Print the steps of the fastest solution
    print("Positions successives :")
    print(';'.join(fastest_map.steps))


if __name__ == '__main__':
    main()
