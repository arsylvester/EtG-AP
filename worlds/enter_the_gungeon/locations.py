from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from .Names import LocationName

from . import items

if TYPE_CHECKING:
    from .world import EnterTheGungeonWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "Top Left Room Chest": 1,
    "Top Middle Chest": 2,
    "Bottom Left Chest": 3,
    "Bottom Left Extra Chest": 4,
    "Bottom Right Room Left Chest": 5,
    "Bottom Right Room Right Chest": 6,
    # Location IDs don't need to be sequential, as long as they're unique and greater than 0.
    "Right Room Enemy Drop": 10,
}

OxAndCadenceLocations = {
    LocationName.BLUEPRINTMETA_THOMPSON: 200001,
	LocationName.BLUEPRINTMETA_HEARTBOTTLE: 200002,
	LocationName.BLUEPRINTMETA_GAMMARAY: 200003,
	LocationName.BLUEPRINTMETA_RPG: 200004,
	LocationName.BLUEPRINTMETA_ROCKETBULLETS: 200005,
	LocationName.BLUEPRINTMETA_HEGEMONYRIFLE: 200006,
	LocationName.BLUEPRINTMETA_HEARTLOCKET: 200007,
	LocationName.BLUEPRINTMETA_FIREBULLETS: 200008,
	LocationName.BLUEPRINTMETA_FREEZERAY: 200009,
	LocationName.BLUEPRINTMETA_HEARTLUNCHBOX: 200010,
	LocationName.BLUEPRINTMETA_BOX: 200011,
	LocationName.BLUEPRINTMETA_MAILBOX: 200012,
	LocationName.BLUEPRINTMETA_FATBULLETS: 200013,
	LocationName.BLUEPRINTMETA_BETTERBULLETS: 200014,
	LocationName.BLUEPRINTMETA_ANGRYBULLETS: 200015,
	LocationName.BLUEPRINTMETA_SIREN: 200016,
	LocationName.BLUEPRINTMETA_HEARTPURSE: 200017,
	LocationName.BLUEPRINTMETA_ORIGUNI: 200018,
	LocationName.BLUEPRINTMETA_EYEPATCH: 200019,
	LocationName.BLUEPRINTMETA_BLOODYEYE: 200020,
	LocationName.BLUEPRINTMETA_SPICE: 200021,
	LocationName.BLUEPRINTMETA_GRASSCHOPPER: 200022,
	LocationName.BLUEPRINTMETA_SUNGLASSES: 200023,
	LocationName.BLUEPRINTMETA_FLASHRAYGUN: 200024,
	LocationName.BLUEPRINTMETA_SINGULARITY: 200025,
	LocationName.BLUEPRINTMETA_SCIENCECANNON: 200026,
	LocationName.BLUEPRINTMETA_NANOMACHINES: 200027,
	LocationName.BLUEPRINTMETA_ICEBREAKER: 200028,
	LocationName.BLUEPRINTMETA_PORTABLETURRET: 200029,
	LocationName.BLUEPRINTMETA_DUCTTAPE: 200030,
	LocationName.BLUEPRINTMETA_TANGLER: 200031,
	LocationName.BLUEPRINTMETA_LAMP: 200032,
	LocationName.BLUEPRINTMETA_FACEMELTER: 200033,
	LocationName.BLUEPRINTMETA_HEROINE: 200034,
	LocationName.BLUEPRINTMETA_MASSSHOTGUN: 200035,
	LocationName.BLUEPRINTMETA_CEREBRALBORE: 200036,
	LocationName.BLUEPRINTMETA_RAIDENCOIL: 200037,
	LocationName.BLUEPRINTMETA_BLACKHOLEGUN: 200038,
	LocationName.BLUEPRINTMETA_SPACEFRIEND: 200039,
	LocationName.BLUEPRINTMETA_YARI: 200040,
	LocationName.BLUEPRINTMETA_RAILGUN: 200041,
	LocationName.BLUEPRINTMETA_BROCCOLI: 200042,
	#LocationName.BLUEPRINTMETA_MTXGUN: 200043,
	LocationName.BLUEPRINTMETA_PLATINUMBULLETS: 200100,
}

GooptonLocations = {
    LocationName.BLUEPRINTGOOP_BUGBOOTS: 220001,
	LocationName.BLUEPRINTGOOP_FOSSILIZEDGUN: 220002,
	LocationName.BLUEPRINTGOOP_MONSTERBLOOD: 220003,
	LocationName.BLUEPRINTGOOP_PLAGUEPISTOL: 220004,
	LocationName.BLUEPRINTGOOP_MEMBRANE: 220005,
	LocationName.BLUEPRINTGOOP_PLUNGER: 220006,
	LocationName.BLUEPRINTGOOP_SPONGE: 220007,
	LocationName.BLUEPRINTGOOP_TENTACLEARM: 220008,
	LocationName.BLUEPRINTGOOP_NAPALMSTRIKE: 220009,
	LocationName.BLUEPRINTGOOP_GUNDROMEDASTRAIN: 220010,
	LocationName.BLUEPRINTGOOP_EVOLVER: 220011,
}

TrorcLocations = {
    LocationName.BLUEPRINTTRUCK_CLUSTERMINE: 230001,
	LocationName.BLUEPRINTTRUCK_MSIXTEEN: 230002,
	LocationName.BLUEPRINTTRUCK_RATION: 230003,
	LocationName.BLUEPRINTTRUCK_AIRSTRIKE: 230004,
	LocationName.BLUEPRINTTRUCK_COMMANDO: 230005,
	LocationName.BLUEPRINTTRUCK_AWP: 230006,
	LocationName.BLUEPRINTTRUCK_NIKITA: 230007,
	LocationName.BLUEPRINTTRUCK_BIGBOY: 230008,
	LocationName.BLUEPRINTTRUCK_CHAFFGRENADE: 230009,
	LocationName.BLUEPRINTTRUCK_PATRIOT: 230010,
	LocationName.BLUEPRINTTRUCK_MAGAZINERACK: 230011,
}

DougLocations = {
    LocationName.BLUEPRINTBEETLE_DEVOLVER: 240001,
	LocationName.BLUEPRINTBEETLE_BASEBALLBAT: 240002,
	LocationName.BLUEPRINTBEETLE_DAWNHAMMER: 240003,
	LocationName.BLUEPRINTBEETLE_STRAFEGUN: 240004,
	LocationName.BLUEPRINTBEETLE_HYPERLIGHT: 240005,
	LocationName.BLUEPRINTBEETLE_STARPEW: 240006,
	LocationName.BLUEPRINTBEETLE_DUELINGLASER: 240007,
	LocationName.BLUEPRINTBEETLE_TELEPORTERPROTOTYPE: 240008,
	LocationName.BLUEPRINTBEETLE_VORPALGUN: 240009,
	LocationName.BLUEPRINTBEETLE_STOUTIES: 240010,
	LocationName.BLUEPRINTBEETLE_CHARMERS: 240011,
	LocationName.BLUEPRINTBEETLE_FLAKTUALLY: 240012,
	LocationName.BLUEPRINTBEETLE_MAGICITES: 240013,
	LocationName.BLUEPRINTBEETLE_METROIDBOMBS: 240014,
	LocationName.BLUEPRINTBEETLE_SILVALLIES: 240015,
	LocationName.BLUEPRINTBEETLE_HELIX: 240016,
	LocationName.BLUEPRINTBEETLE_GOLDIES: 240017,
	LocationName.BLUEPRINTBEETLE_BEEBULLETS: 240101,
	LocationName.BLUEPRINTBEETLE_DEVOLVERBULLETS: 240102,
	LocationName.BLUEPRINTBEETLE_CRITICALBULLETS: 240103,
	LocationName.BLUEPRINTBEETLE_SNOWBALLETS: 240104,
	LocationName.BLUEPRINTBEETLE_BIGGIANTHEAD: 240105,
	LocationName.BLUEPRINTBEETLE_COMBINERIFLE: 240106,
	LocationName.BLUEPRINTBEETLE_EXOTICGUN: 240107,
	LocationName.BLUEPRINTBEETLE_BIGSHOTGUN: 240108,
	LocationName.BLUEPRINTBEETLE_GUNDERFURY: 240201,
	LocationName.BLUEPRINTBEETLE_GLAIVE: 240202,
	LocationName.BLUEPRINTBEETLE_LUTE: 240203,
	LocationName.BLUEPRINTBEETLE_TETRIS: 240204,
	LocationName.BLUEPRINTBEETLE_TRIGUN: 240205,
	LocationName.BLUEPRINTBEETLE_SHOVEL: 240206,
	LocationName.BLUEPRINTBEETLE_PREDATOR: 240207,
	LocationName.BLUEPRINTBEETLE_VOIDCORELAUNCHER: 240208,
	LocationName.BLUEPRINTBEETLE_BLANKBULLETS: 240209,
	LocationName.BLUEPRINTBEETLE_ORBITALBULLETS: 240210,
	LocationName.BLUEPRINTBEETLE_SCOUTER: 240211,
	LocationName.BLUEPRINTBEETLE_CONTROLLER: 240212,
	LocationName.BLUEPRINTBEETLE_GUNNER: 240213,
}

AllLocationIds = {
    **OxAndCadenceLocations,
    **GooptonLocations,
    **TrorcLocations,
    **DougLocations
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class GungeonLocation(Location):
    game = "Enter The Gungeon"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: EnterTheGungeonWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: EnterTheGungeonWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    overworld = world.get_region("Overworld")
    top_left_room = world.get_region("Top Left Room")
    bottom_right_room = world.get_region("Bottom Right Room")
    right_room = world.get_region("Right Room")

    # One way to create locations is by just creating them directly via their constructor.
    bottom_left_chest = GungeonLocation(
        world.player, "Bottom Left Chest", world.location_name_to_id["Bottom Left Chest"], overworld
    )

    # You can then add them to the region.
    overworld.locations.append(bottom_left_chest)

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    bottom_right_room_locations = get_location_names_with_ids(
        ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    )
    bottom_right_room.add_locations(bottom_right_room_locations, GungeonLocation)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    top_left_room.add_locations(top_left_room_locations, GungeonLocation)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    right_room.add_locations(right_room_locations, GungeonLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, GungeonLocation)
    else:
        overworld.add_locations(top_middle_room_locations, GungeonLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, GungeonLocation)


def create_events(world: EnterTheGungeonWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    #top_left_room = world.get_region("Top Left Room")
    #final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    #button_in_top_left_room = GungeonLocation(world.player, "Top Left Room Button", None, top_left_room)
    #top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    #button_item = items.GungeonItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    #button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    #final_boss_room.add_event(
    #    "Final Boss Defeated", "Victory", location_type=GungeonLocation, item_type=items.GungeonItem
    #)

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
