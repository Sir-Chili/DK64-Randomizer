"""Select CB Location selection."""
from select import select
import randomizer.Lists.CBLocations.JungleJapesCBLocations
import randomizer.Lists.CBLocations.AngryAztecCBLocations
import randomizer.Lists.CBLocations.FranticFactoryCBLocations
import randomizer.Lists.CBLocations.GloomyGalleonCBLocations
import randomizer.Lists.CBLocations.FungiForestCBLocations
import randomizer.Lists.CBLocations.CrystalCavesCBLocations
import randomizer.Lists.CBLocations.CreepyCastleCBLocations

from randomizer.Enums.Levels import Levels
from randomizer.Spoiler import Spoiler
from randomizer.Enums.Kongs import Kongs
import random

max_balloons = 105
max_bunches = 400 # 334 bunches in vanilla, biasing this for now to help with calculation formula
max_singles = 1127 - max_bunches  # 793 Singles in Vanilla, under-representing this to help with the calculation formula

level_data = {
    Levels.JungleJapes: {
        "cb": randomizer.Lists.CBLocations.JungleJapesCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.JungleJapesCBLocations.BalloonList,
    },
    Levels.AngryAztec: {
        "cb": randomizer.Lists.CBLocations.AngryAztecCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.AngryAztecCBLocations.BalloonList,
    },
    Levels.FranticFactory: {
        "cb": randomizer.Lists.CBLocations.FranticFactoryCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.FranticFactoryCBLocations.BalloonList,
    },
    Levels.GloomyGalleon: {
        "cb": randomizer.Lists.CBLocations.GloomyGalleonCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.GloomyGalleonCBLocations.BalloonList,
    },
    Levels.FungiForest: {
        "cb": randomizer.Lists.CBLocations.FungiForestCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.FungiForestCBLocations.BalloonList,
    },
    Levels.CrystalCaves: {
        "cb": randomizer.Lists.CBLocations.CrystalCavesCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.CrystalCavesCBLocations.BalloonList,
    },
    Levels.CreepyCastle: {
        "cb": randomizer.Lists.CBLocations.CreepyCastleCBLocations.ColoredBananaGroupList,
        "balloons": randomizer.Lists.CBLocations.CreepyCastleCBLocations.BalloonList,
    },
}


def ShuffleCBs(spoiler: Spoiler):
    """Shuffle CBs selected from location files."""
    total_balloons = 0
    total_singles = 0
    total_bunches = 0
    cb_data = {}
    for level_index, level in enumerate(level_data):
        level_placement = []
        global_divisor = 6 - level_index
        kong_specific_left = {
            Kongs.donkey: 100,
            Kongs.diddy: 100,
            Kongs.lanky: 100,
            Kongs.tiny: 100,
            Kongs.chunky: 100,
        }
        # Balloons        
        # Pick random amount of balloons assigned to level
        balloons_left = max_balloons - total_balloons
        balloon_lower = max(int(balloons_left / (7 - level_index)) - 3, 0)  # Select lower bound for randomization as max between 0, and balloons left distributed amongst the remaining levels minus 3
        if global_divisor == 0:
            # Last Level
            balloon_upper = balloons_left
        else:
            balloon_upper = min(int(balloons_left / (7 - level_index)) + 3, int(balloons_left / global_divisor))
        balloon_lst = level_data[level]["balloons"].copy()
        selected_balloon_count = min(random.randint(min(balloon_lower, balloon_upper), max(balloon_lower, balloon_upper)),len(balloon_lst))
        random.shuffle(balloon_lst) # TODO: Maybe make this more advanced?
        # selects all balloons
        placed_balloons = 0
        for balloon in balloon_lst:
            if placed_balloons < selected_balloon_count:
                balloon_kongs = balloon.kongs.copy()
                for kong in kong_specific_left:
                    if kong_specific_left[kong] < 10 and kong in balloon_kongs: # Not enough Colored Bananas to place a balloon:
                        balloon_kongs.remove(kong) # Remove kong from permitted list
                if len(balloon_kongs) > 0: # Has a kong who can be assigned to this balloon
                    selected_kong = random.choice(balloon_kongs)
                    kong_specific_left[selected_kong] -= 10 # Remove CBs for Balloon
                    level_placement.append({
                        "name": balloon.name,
                        "kong": selected_kong,
                        "level": level,
                        "type": "balloon"
                    })
                    placed_balloons += 1
        # Model Two CBs
        bunches_left = max_bunches - total_bunches
        singles_left = max_singles - total_singles
        bunches_lower = max(int(bunches_left / (7 - level_index))-5,0)
        singles_lower = max(int(singles_left / (7 - level_index))-10,0)
        if global_divisor == 0:
            bunches_upper = bunches_left
            singles_upper = singles_left
        else:
            bunches_upper = min(int(bunches_left / (7 - level_index))+15, int(bunches_left/global_divisor))
            singles_upper = min(int(singles_left / (7 - level_index))+10, int(singles_left/global_divisor))
        modeltwo_cb_lst = level_data[level]["cb"].copy()
        random.shuffle(modeltwo_cb_lst)
        selected_bunch_count = min(random.randint(min(bunches_lower,bunches_upper), max(bunches_lower,bunches_upper)),len(modeltwo_cb_lst))
        selected_single_count = min(random.randint(min(singles_lower,singles_upper), max(singles_lower,singles_upper)),len(modeltwo_cb_lst))
        placed_bunches = 0
        placed_singles = 0
        for item in modeltwo_cb_lst:
            cb_kongs = item.kongs.copy()
            group_weight = 0
            bunches_in_group = 0
            singles_in_group = 0
            for loc in item.locations:
                group_weight += loc[0]
                bunches_in_group += int(loc[0] == 5)
                singles_in_group += int(loc[0] == 1)
            for kong in kong_specific_left:
                if kong in cb_kongs:
                    if kong_specific_left[kong] < group_weight or (kong_specific_left[kong] <= 10 and ((kong_specific_left[kong] - group_weight) % 5) != 0):
                        cb_kongs.remove(kong)
            if len(cb_kongs) > 0 and selected_single_count >= placed_singles + singles_in_group:
                selected_kong = random.choice(cb_kongs)
                kong_specific_left[selected_kong] -= group_weight # Remove CBs for kong
                level_placement.append({
                    "name": item.name,
                    "kong": selected_kong,
                    "level": level,
                    "type": "modeltwo"
                })
                placed_bunches += bunches_in_group
                placed_singles += singles_in_group

        # Placement is valid
        total_balloons += placed_balloons
        total_bunches += selected_bunch_count # Using the projected count rather than placed to see whether problems are caused
        total_singles += placed_singles
        cb_data[level] = level_placement.copy()
        print(kong_specific_left)

    spoiler.cb_placements = cb_data
