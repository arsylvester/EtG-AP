from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from .Names import RegionName

import typing

if TYPE_CHECKING:
    from .world import EnterTheGungeonWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: EnterTheGungeonWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: EnterTheGungeonWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    breach = Region(RegionName.Breach, world.player, world.multiworld)
    ox_and_cadence_1 = Region(RegionName.OxAndCadence1, world.player, world.multiworld)
    ox_and_cadence_2 = Region(RegionName.OxAndCadence2, world.player, world.multiworld)
    ox_and_cadence_3 = Region(RegionName.OxAndCadence3, world.player, world.multiworld)
    ox_and_cadence_4 = Region(RegionName.OxAndCadence4, world.player, world.multiworld)
    ox_and_cadence_5 = Region(RegionName.OxAndCadence5, world.player, world.multiworld)
    ox_and_cadence_6 = Region(RegionName.OxAndCadence6, world.player, world.multiworld)
    ox_and_cadence_7 = Region(RegionName.OxAndCadence7, world.player, world.multiworld)
    ox_and_cadence_8 = Region(RegionName.OxAndCadence8, world.player, world.multiworld)
    doug_1 = Region(RegionName.Doug1, world.player, world.multiworld)
    doug_2 = Region(RegionName.Doug2, world.player, world.multiworld)
    doug_3 = Region(RegionName.Doug3, world.player, world.multiworld)
    doug_4 = Region(RegionName.Doug4, world.player, world.multiworld)
    doug_5 = Region(RegionName.Doug5, world.player, world.multiworld)
    doug_6 = Region(RegionName.Doug6, world.player, world.multiworld)
    goopton_1 = Region(RegionName.Goopton1, world.player, world.multiworld)
    goopton_2 = Region(RegionName.Goopton2, world.player, world.multiworld)
    trorc_1 = Region(RegionName.Trorc1, world.player, world.multiworld)
    trorc_2 = Region(RegionName.Trorc2, world.player, world.multiworld)
    tinker = Region(RegionName.Tinker, world.player, world.multiworld)
    payday = Region(RegionName.Payday, world.player, world.multiworld)
    past_killable = Region(RegionName.PastKillable, world.player, world.multiworld)
    oubliette = Region(RegionName.Oubliette, world.player, world.multiworld)
    abbey = Region(RegionName.Abbey, world.player, world.multiworld)
    rat_lair = Region(RegionName.RatLair, world.player, world.multiworld)
    rat_maze = Region(RegionName.RatFight, world.player, world.multiworld)
    rng_department = Region(RegionName.RngDepartment, world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [breach, ox_and_cadence_1, ox_and_cadence_2, ox_and_cadence_3, ox_and_cadence_4, ox_and_cadence_5,
               ox_and_cadence_6, ox_and_cadence_7, ox_and_cadence_8, doug_1, doug_2, doug_3, doug_4, doug_5, doug_6,
               goopton_1, goopton_2, trorc_1, trorc_2, tinker, payday, past_killable, oubliette, abbey, rat_lair,
               rat_maze, rng_department]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    #if world.options.hammer:
    #    top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
    #    regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: EnterTheGungeonWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    #breach = world.get_region(RegionName.Breach)
    #ox_and_cadence = world.get_region(RegionName.OxAndCadence)
    #bottom_right_room = world.get_region("Bottom Right Room")
    #right_room = world.get_region("Right Room")
    #final_boss_room = world.get_region("Final Boss Room")

    # noinspection bad-assignment
    EtGRegionConnections: typing.Dict[str, typing.Tuple[str]] = {
        RegionName.Breach: (RegionName.OxAndCadence1,
                            RegionName.Doug1,
                            RegionName.Goopton1,
                            RegionName.Trorc1,
                            RegionName.Tinker,
                            RegionName.Payday,
                            RegionName.PastKillable,
                            RegionName.Oubliette,
                            RegionName.Abbey,
                            RegionName.RatLair,
                            RegionName.RngDepartment),
        RegionName.OxAndCadence1: (RegionName.OxAndCadence2,),
        RegionName.OxAndCadence2: (RegionName.OxAndCadence3,),
        RegionName.OxAndCadence3: (RegionName.OxAndCadence4,),
        RegionName.OxAndCadence4: (RegionName.OxAndCadence5,),
        RegionName.OxAndCadence5: (RegionName.OxAndCadence6,),
        RegionName.OxAndCadence6: (RegionName.OxAndCadence7,),
        RegionName.OxAndCadence7: (RegionName.OxAndCadence8,),
        RegionName.Doug1: (RegionName.Doug2,),
        RegionName.Doug2: (RegionName.Doug3,),
        RegionName.Doug3: (RegionName.Doug4,),
        RegionName.Doug4: (RegionName.Doug5,),
        RegionName.Doug5: (RegionName.Doug6,),
        RegionName.Goopton1: (RegionName.Goopton2,),
        RegionName.Trorc1: (RegionName.Trorc2,),
        RegionName.RatLair: (RegionName.RatFight,),
    }

    for source, targets in EtGRegionConnections.items():
        source_region = world.get_region(source)
        for target in targets:
            target_region = world.get_region(target)
            connectionName = get_connection_name(source, target)
            source_region.connect(target_region, connectionName)

def get_connection_name (source:str, target:str) -> str:
    return source + " to " + target

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    #overworld_to_bottom_right_room = Entrance(world.player, "Overworld to Bottom Right Room", parent=overworld)
    #overworld.exits.append(overworld_to_bottom_right_room)

    # You can then connect the Entrance to the target region.
    #overworld_to_bottom_right_room.connect(bottom_right_room)

    # An even easier way is to use the region.connect helper.
    #breach.connect(ox_and_cadence, "Overworld to Right Room")
    #right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    #if world.options.hammer:
    #    top_middle_room = world.get_region("Top Middle Room")
    #    overworld.connect(top_middle_room, "Overworld to Top Middle Room")
