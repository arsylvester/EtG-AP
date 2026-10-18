from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, LocationProgressType
from .Names import LocationName
from .Names import RegionName

from . import items

if TYPE_CHECKING:
    from .world import EnterTheGungeonWorld

OxAndCadenceLocations1 = {
    LocationName.BLUEPRINTMETA_THOMPSON: 200001,
    LocationName.BLUEPRINTMETA_HEARTBOTTLE: 200002,
    LocationName.BLUEPRINTMETA_GAMMARAY: 200003,
    LocationName.BLUEPRINTMETA_RPG: 200004,
    LocationName.BLUEPRINTMETA_ROCKETBULLETS: 200005,
    LocationName.BLUEPRINTMETA_HEGEMONYRIFLE: 200006,
}
OxAndCadenceLocations2 = {
    LocationName.BLUEPRINTMETA_HEARTLOCKET: 200007,
    LocationName.BLUEPRINTMETA_FIREBULLETS: 200008,
    LocationName.BLUEPRINTMETA_FREEZERAY: 200009,
    LocationName.BLUEPRINTMETA_HEARTLUNCHBOX: 200010,
    LocationName.BLUEPRINTMETA_BOX: 200011,
    LocationName.BLUEPRINTMETA_MAILBOX: 200012,
}
OxAndCadenceLocations3 = {
    LocationName.BLUEPRINTMETA_FATBULLETS: 200013,
    LocationName.BLUEPRINTMETA_BETTERBULLETS: 200014,
    LocationName.BLUEPRINTMETA_ANGRYBULLETS: 200015,
    LocationName.BLUEPRINTMETA_SIREN: 200016,
    LocationName.BLUEPRINTMETA_HEARTPURSE: 200017,
    LocationName.BLUEPRINTMETA_ORIGUNI: 200018,
}
OxAndCadenceLocations4 = {
    LocationName.BLUEPRINTMETA_EYEPATCH: 200019,
    LocationName.BLUEPRINTMETA_BLOODYEYE: 200020,
    LocationName.BLUEPRINTMETA_SPICE: 200021,
    LocationName.BLUEPRINTMETA_GRASSCHOPPER: 200022,
    LocationName.BLUEPRINTMETA_SUNGLASSES: 200023,
    LocationName.BLUEPRINTMETA_FLASHRAYGUN: 200024,
}
OxAndCadenceLocations5 = {
    LocationName.BLUEPRINTMETA_SINGULARITY: 200025,
    LocationName.BLUEPRINTMETA_SCIENCECANNON: 200026,
    LocationName.BLUEPRINTMETA_NANOMACHINES: 200027,
    LocationName.BLUEPRINTMETA_ICEBREAKER: 200028,
    LocationName.BLUEPRINTMETA_PORTABLETURRET: 200029,
    LocationName.BLUEPRINTMETA_DUCTTAPE: 200030,
}
OxAndCadenceLocations6 = {
    LocationName.BLUEPRINTMETA_TANGLER: 200031,
    LocationName.BLUEPRINTMETA_LAMP: 200032,
    LocationName.BLUEPRINTMETA_FACEMELTER: 200033,
    LocationName.BLUEPRINTMETA_HEROINE: 200034,
    LocationName.BLUEPRINTMETA_MASSSHOTGUN: 200035,
    LocationName.BLUEPRINTMETA_CEREBRALBORE: 200036,
}
OxAndCadenceLocations7 = {
    LocationName.BLUEPRINTMETA_RAIDENCOIL: 200037,
    LocationName.BLUEPRINTMETA_BLACKHOLEGUN: 200038,
    LocationName.BLUEPRINTMETA_SPACEFRIEND: 200039,
    LocationName.BLUEPRINTMETA_YARI: 200040,
    LocationName.BLUEPRINTMETA_RAILGUN: 200041,
    LocationName.BLUEPRINTMETA_BROCCOLI: 200042,
}
OxAndCadenceLocations8 = {
    #LocationName.BLUEPRINTMETA_MTXGUN: 200043,
    LocationName.BLUEPRINTMETA_PLATINUMBULLETS: 200100,
}

GooptonLocations1 = {
    LocationName.BLUEPRINTGOOP_BUGBOOTS: 220001,
    LocationName.BLUEPRINTGOOP_FOSSILIZEDGUN: 220002,
    LocationName.BLUEPRINTGOOP_MONSTERBLOOD: 220003,
    LocationName.BLUEPRINTGOOP_PLAGUEPISTOL: 220004,
    LocationName.BLUEPRINTGOOP_MEMBRANE: 220005,
    LocationName.BLUEPRINTGOOP_PLUNGER: 220006,
}
GooptonLocations2 = {
    LocationName.BLUEPRINTGOOP_SPONGE: 220007,
    LocationName.BLUEPRINTGOOP_TENTACLEARM: 220008,
    LocationName.BLUEPRINTGOOP_NAPALMSTRIKE: 220009,
    LocationName.BLUEPRINTGOOP_GUNDROMEDASTRAIN: 220010,
    LocationName.BLUEPRINTGOOP_EVOLVER: 220011,
}

TrorcLocations1 = {
    LocationName.BLUEPRINTTRUCK_CLUSTERMINE: 230001,
    LocationName.BLUEPRINTTRUCK_MSIXTEEN: 230002,
    LocationName.BLUEPRINTTRUCK_RATION: 230003,
    LocationName.BLUEPRINTTRUCK_AIRSTRIKE: 230004,
    LocationName.BLUEPRINTTRUCK_COMMANDO: 230005,
    LocationName.BLUEPRINTTRUCK_AWP: 230006,
}
TrorcLocations2 = {
    LocationName.BLUEPRINTTRUCK_NIKITA: 230007,
    LocationName.BLUEPRINTTRUCK_BIGBOY: 230008,
    LocationName.BLUEPRINTTRUCK_CHAFFGRENADE: 230009,
    LocationName.BLUEPRINTTRUCK_PATRIOT: 230010,
    LocationName.BLUEPRINTTRUCK_MAGAZINERACK: 230011,
}

DougLocations1 = {
    LocationName.BLUEPRINTBEETLE_DEVOLVER: 240001,
    LocationName.BLUEPRINTBEETLE_BASEBALLBAT: 240002,
    LocationName.BLUEPRINTBEETLE_DAWNHAMMER: 240003,
    LocationName.BLUEPRINTBEETLE_STRAFEGUN: 240004,
    LocationName.BLUEPRINTBEETLE_HYPERLIGHT: 240005,
    LocationName.BLUEPRINTBEETLE_STARPEW: 240006,
}
DougLocations2 = {
    LocationName.BLUEPRINTBEETLE_DUELINGLASER: 240007,
    LocationName.BLUEPRINTBEETLE_TELEPORTERPROTOTYPE: 240008,
    LocationName.BLUEPRINTBEETLE_VORPALGUN: 240009,
    LocationName.BLUEPRINTBEETLE_STOUTIES: 240010,
    LocationName.BLUEPRINTBEETLE_CHARMERS: 240011,
    LocationName.BLUEPRINTBEETLE_FLAKTUALLY: 240012,
}
DougLocations3 = {
    LocationName.BLUEPRINTBEETLE_MAGICITES: 240013,
    LocationName.BLUEPRINTBEETLE_METROIDBOMBS: 240014,
    LocationName.BLUEPRINTBEETLE_SILVALLIES: 240015,
    LocationName.BLUEPRINTBEETLE_HELIX: 240016,
    LocationName.BLUEPRINTBEETLE_GOLDIES: 240017,
    LocationName.BLUEPRINTBEETLE_BEEBULLETS: 240101,
}
DougLocations4 = {
    LocationName.BLUEPRINTBEETLE_DEVOLVERBULLETS: 240102,
    LocationName.BLUEPRINTBEETLE_CRITICALBULLETS: 240103,
    LocationName.BLUEPRINTBEETLE_SNOWBALLETS: 240104,
    LocationName.BLUEPRINTBEETLE_BIGGIANTHEAD: 240105,
    LocationName.BLUEPRINTBEETLE_COMBINERIFLE: 240106,
    LocationName.BLUEPRINTBEETLE_EXOTICGUN: 240107,
}
DougLocations5 = {
    LocationName.BLUEPRINTBEETLE_BIGSHOTGUN: 240108,
    LocationName.BLUEPRINTBEETLE_GUNDERFURY: 240201,
    LocationName.BLUEPRINTBEETLE_GLAIVE: 240202,
    LocationName.BLUEPRINTBEETLE_LUTE: 240203,
    LocationName.BLUEPRINTBEETLE_TETRIS: 240204,
    LocationName.BLUEPRINTBEETLE_TRIGUN: 240205,
}
DougLocations6 = {
    LocationName.BLUEPRINTBEETLE_SHOVEL: 240206,
    LocationName.BLUEPRINTBEETLE_PREDATOR: 240207,
    LocationName.BLUEPRINTBEETLE_VOIDCORELAUNCHER: 240208,
    LocationName.BLUEPRINTBEETLE_BLANKBULLETS: 240209,
    LocationName.BLUEPRINTBEETLE_ORBITALBULLETS: 240210,
    LocationName.BLUEPRINTBEETLE_SCOUTER: 240211,
    LocationName.BLUEPRINTBEETLE_CONTROLLER: 240212,
    LocationName.BLUEPRINTBEETLE_GUNNER: 240213,
}

BreachLocations = {
	LocationName.NPCJAILCELL_1: 400001,
	LocationName.NPCJAILCELL_2: 400002,
	LocationName.NPCJAILCELL_3: 400003,
	LocationName.NPCJAILCELL_4: 400004,
	LocationName.NPCJAILCELL_5: 400005,
	LocationName.NPCJAILCELL_6: 400006,
	LocationName.NPCJAILCELL_7: 400007,
	LocationName.NPCJAILCELL_8: 400008,
	LocationName.NPCJAILCELL_9: 400009,
	LocationName.NPCJAILCELL_10: 400010,
	LocationName.NPCJAILCELL_11: 400011,
	LocationName.NPCJAILCELL_12: 400012,
	LocationName.NPCJAILCELL_13: 400013,
	LocationName.NPCJAILCELL_14: 400014,
	LocationName.NPCJAILCELL_15: 400015,
	LocationName.SHOP_HAS_MET_TRUCK: 45501,
    LocationName.WINCHESTER_MET_PREVIOUSLY: 25506,
    LocationName.SHERPA_ACTIVE_IN_ELEVATOR_ROOM: 30005,

	LocationName.BLACKSMITH_ELEMENT1: 50105,
	LocationName.BLACKSMITH_ELEMENT2: 50106,
	LocationName.BLACKSMITH_ELEMENT3: 50107,
	LocationName.BLACKSMITH_ELEMENT4: 50108,
	LocationName.ACHIEVEMENT_NOBOSSDAMAGE_CASTLE: 300001,
	LocationName.ACHIEVEMENT_NOBOSSDAMAGE_GUNGEON: 300002,
	LocationName.ACHIEVEMENT_NOBOSSDAMAGE_MINES: 300003,
	LocationName.ACHIEVEMENT_NOBOSSDAMAGE_HOLLOW: 300004,
	LocationName.ACHIEVEMENT_NOBOSSDAMAGE_FORGE: 300005,

    LocationName.BOSSKILLED_BULLET_KING: 10000,
	LocationName.BOSSKILLED_BULLET_BROS: 10010,
	LocationName.BOSSKILLED_GATLING_GULL: 10100,
	LocationName.BOSSKILLED_MEDUZI: 10110,
	LocationName.BOSSKILLED_BASHELLISK: 10120,
    LocationName.BOSSKILLED_BEHOLSTER: 10300,
	LocationName.BOSSKILLED_TANK: 10130,
	LocationName.BOSSKILLED_POWDERSKULL: 10140,
    LocationName.BOSSKILLED_MINEFLAYER: 10600,
    LocationName.BOSSKILLED_HIGH_PRIEST: 10400,
    LocationName.BOSSKILLED_STATUES: 10160,
    LocationName.BOSSKILLED_DEMONWALL: 10170,
	LocationName.BOSSKILLED_DOORMIMIC: 10150,
    LocationName.BOSSKILLED_DRAGUN: 10500,
    LocationName.BOSSKILLED_MINI_FUSELIER: 10602,
    LocationName.BOSSKILLED_MINI_MAGICIAN: 400100,

    LocationName.ACHIEVEMENT_CASTLE_MANYTIMES: 300007,
	LocationName.ACHIEVEMENT_GUNGEON_MANYTIMES: 300008,
	LocationName.ACHIEVEMENT_MINES_MANYTIMES: 300009,
	LocationName.ACHIEVEMENT_HOLLOW_MANYTIMES: 300010,
	LocationName.ACHIEVEMENT_FORGE_MANYTIMES: 300011,
	LocationName.ACHIEVEMENT_STEAL_THINGS: 300013,
	LocationName.ACHIEVEMENT_TABLE_PIT: 300015,
	LocationName.ACHIEVEMENT_BEASTMODE: 300016,
	LocationName.ACHIEVEMENT_TABLES_FLIPPED: 300017,
	LocationName.ACHIEVEMENT_SURPRISE_MIMIC: 300022,
	LocationName.ACHIEVEMENT_KILL_JAMMED_BOSS: 300024,
	LocationName.ACHIEVEMENT_BIGGEST_WALLET: 300025,
}

OtherLocations = {
    LocationName.BLACKSMITH_BULLET_COMPLETE: 50120,
    LocationName.BOSSKILLED_BLOBULORD: 10190,
    LocationName.BOSSKILLED_OLDKING: 10180,
	LocationName.BOSSKILLED_RESOURCEFULRAT: 10220,
	LocationName.BOSSKILLED_HELICOPTER: 10505,
	LocationName.BOSSKILLED_LICH: 19000, #TODO add to a region
	LocationName.BOSSKILLED_HIGHDRAGUN: 19001, #TODO add to a region
    LocationName.TUTORIAL_KILLED_MANFREDS_RIVAL: 2002, #TODO add to a region
    LocationName.ACHIEVEMENT_BREACH_POPULATED: 300014, #TODO add to a region
    LocationName.ACHIEVEMENT_ACCESS_OUBLIETTE: 300020,
	LocationName.ACHIEVEMENT_ACCESS_ABBEY: 300021,
}

AllLocationIds = {
    **OxAndCadenceLocations1,
    **OxAndCadenceLocations2,
    **OxAndCadenceLocations3,
    **OxAndCadenceLocations4,
    **OxAndCadenceLocations5,
    **OxAndCadenceLocations6,
    **OxAndCadenceLocations7,
    **OxAndCadenceLocations8,
    **GooptonLocations1,
    **GooptonLocations2,
    **TrorcLocations1,
    **TrorcLocations2,
    **DougLocations1,
    **DougLocations2,
    **DougLocations3,
    **DougLocations4,
    **DougLocations5,
    **DougLocations6,
	**BreachLocations,
    **OtherLocations,
}

ExcludedPriorityLocations = [
    LocationName.ACHIEVEMENT_CASTLE_MANYTIMES,
	LocationName.ACHIEVEMENT_GUNGEON_MANYTIMES,
	LocationName.ACHIEVEMENT_MINES_MANYTIMES,
	LocationName.ACHIEVEMENT_HOLLOW_MANYTIMES,
	LocationName.ACHIEVEMENT_FORGE_MANYTIMES,
    LocationName.BOSSKILLED_DOORMIMIC,
]

class GungeonLocation(Location):
    game = "Enter The Gungeon"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: AllLocationIds[location_name] for location_name in location_names}


def create_all_locations(world: EnterTheGungeonWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: EnterTheGungeonWorld) -> None:
    world.get_region(RegionName.Breach).add_locations(BreachLocations, GungeonLocation)
    world.get_region(RegionName.OxAndCadence1).add_locations(OxAndCadenceLocations1, GungeonLocation)
    world.get_region(RegionName.OxAndCadence2).add_locations(OxAndCadenceLocations2, GungeonLocation)
    world.get_region(RegionName.OxAndCadence3).add_locations(OxAndCadenceLocations3, GungeonLocation)
    world.get_region(RegionName.OxAndCadence4).add_locations(OxAndCadenceLocations4, GungeonLocation)
    world.get_region(RegionName.OxAndCadence5).add_locations(OxAndCadenceLocations5, GungeonLocation)
    world.get_region(RegionName.OxAndCadence6).add_locations(OxAndCadenceLocations6, GungeonLocation)
    world.get_region(RegionName.OxAndCadence7).add_locations(OxAndCadenceLocations7, GungeonLocation)
    world.get_region(RegionName.OxAndCadence8).add_locations(OxAndCadenceLocations8, GungeonLocation)

    world.get_region(RegionName.Doug1).add_locations(DougLocations1, GungeonLocation)
    world.get_region(RegionName.Doug2).add_locations(DougLocations2, GungeonLocation)
    world.get_region(RegionName.Doug3).add_locations(DougLocations3, GungeonLocation)
    world.get_region(RegionName.Doug4).add_locations(DougLocations4, GungeonLocation)
    world.get_region(RegionName.Doug5).add_locations(DougLocations5, GungeonLocation)
    world.get_region(RegionName.Doug6).add_locations(DougLocations6, GungeonLocation)

    world.get_region(RegionName.Goopton1).add_locations(GooptonLocations1, GungeonLocation)
    world.get_region(RegionName.Goopton2).add_locations(GooptonLocations2, GungeonLocation)

    world.get_region(RegionName.Trorc1).add_locations(TrorcLocations1, GungeonLocation)
    world.get_region(RegionName.Trorc2).add_locations(TrorcLocations2, GungeonLocation)

    oubliette = world.get_region(RegionName.Oubliette)
    oubliette.add_locations(get_location_names_with_ids(
        [LocationName.ACHIEVEMENT_ACCESS_OUBLIETTE, LocationName.BOSSKILLED_BLOBULORD]))

    abbey = world.get_region(RegionName.Abbey)
    abbey.add_locations(get_location_names_with_ids(
        [LocationName.ACHIEVEMENT_ACCESS_ABBEY, LocationName.BOSSKILLED_OLDKING]))

    ratFight = world.get_region(RegionName.RatFight)
    ratFight.add_locations(get_location_names_with_ids([LocationName.BOSSKILLED_RESOURCEFULRAT]))

    rngDep = world.get_region(RegionName.RngDepartment)
    rngDep.add_locations(get_location_names_with_ids([LocationName.BOSSKILLED_HELICOPTER]))

    pastKillable = world.get_region(RegionName.PastKillable)
    pastKillable.add_locations(get_location_names_with_ids([LocationName.BLACKSMITH_BULLET_COMPLETE]))

    # Set Location Priority
    for location in ExcludedPriorityLocations:
        world.get_location(location).progress_type = LocationProgressType.EXCLUDED

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
    return
