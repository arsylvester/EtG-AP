from __future__ import annotations
from .Names import ItemNames
from dataclasses import dataclass

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import EnterTheGungeonWorld

'''
Need a table that includes all gungeon ammonomicon items with its display name, gungeon id, enum of base, unlockable, or exclude
Then another table that is all of base items that will be in all runs, like npcs, progressives, etc. with name, id, classification, and quantity. 

'''
@dataclass
class ItemDetails:
    itemID: int
    classification: ItemClassification
    quantity: int
    isBaseAmmonomicon: bool = False
    grouping: str = ""

# All unlockable guns/items will use the same ID as Gungeon uses. Then all custom unlocks will start at 1000.
ITEM_NAME_TO_DETAILS = {
    # Shop unlocks
    ItemNames.OxAndCadence: ItemDetails(1000, ItemClassification.progression | ItemClassification.useful, 7),
    ItemNames.ProfessorGoop: ItemDetails(1001, ItemClassification.progression | ItemClassification.useful, 2),
    ItemNames.Trorc: ItemDetails(1002, ItemClassification.progression | ItemClassification.useful, 2),
    ItemNames.Doug: ItemDetails(1003, ItemClassification.progression | ItemClassification.useful, 6),
    ItemNames.Tinker: ItemDetails(1004, ItemClassification.progression | ItemClassification.useful, 1),
    # NPCs
    ItemNames.Sorceress: ItemDetails(1005, ItemClassification.useful, 1),
    ItemNames.Daisuke: ItemDetails(1006, ItemClassification.useful, 1),
    ItemNames.Frifle: ItemDetails(1007, ItemClassification.useful, 1),
    ItemNames.GunslingKing: ItemDetails(1008, ItemClassification.useful, 1),
    ItemNames.Adventurer: ItemDetails(1009, ItemClassification.useful, 1),
    ItemNames.Goblin: ItemDetails(1010, ItemClassification.useful, 1),
    ItemNames.Tonic: ItemDetails(1011, ItemClassification.useful, 1),
    ItemNames.Bowler: ItemDetails(1012, ItemClassification.useful, 1),
    ItemNames.OldRed: ItemDetails(1013, ItemClassification.useful, 1),
    ItemNames.Flynt: ItemDetails(1014, ItemClassification.useful, 1),
    ItemNames.Cursula: ItemDetails(1015, ItemClassification.useful, 1),
    ItemNames.Synergrace: ItemDetails(1016, ItemClassification.useful, 1),
    ItemNames.Vampire: ItemDetails(1017, ItemClassification.useful, 1),
    # Progressive
    ItemNames.ProgCasingMult: ItemDetails(1018, ItemClassification.useful, 3),
    ItemNames.ProgCredMult: ItemDetails(1019, ItemClassification.progression, 3),
    ItemNames.ProgCurseReduction: ItemDetails(1020, ItemClassification.progression, 3),
    ItemNames.ProgCoolness: ItemDetails(1021, ItemClassification.useful, 3),
    ItemNames.ProgStartChest: ItemDetails(1022, ItemClassification.progression, 5),
    ItemNames.ProgShortCut: ItemDetails(1023, ItemClassification.progression, 5),
    ItemNames.FiveHegemonyCredits: ItemDetails(1024, ItemClassification.useful | ItemClassification.skip_balancing, 3),
    ItemNames.TenHegemonyCredits: ItemDetails(1025, ItemClassification.useful | ItemClassification.skip_balancing, 3),
    ItemNames.TwentyHegemonyCredits: ItemDetails(1026, ItemClassification.useful, 3),
    # Characters
    ItemNames.PlayAsPilot: ItemDetails(1027, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsMarine: ItemDetails(1028, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsConvict: ItemDetails(1029, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsHunter: ItemDetails(1030, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsRobot: ItemDetails(1031, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsBullet: ItemDetails(1032, ItemClassification.progression | ItemClassification.useful, 1, False, "character"),
    ItemNames.PlayAsGunslinger: ItemDetails(1033, ItemClassification.progression, 1, False, "character"),
    # Cosmetic
    ItemNames.CosmeticKnight: ItemDetails(1034, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticBeastmaster: ItemDetails(1035, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticJailbird: ItemDetails(1036, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticRogue: ItemDetails(1037, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticTermbot: ItemDetails(1038, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticRabbit: ItemDetails(1039, ItemClassification.filler, 1, False, "cosmetic"),
    ItemNames.CosmeticShell: ItemDetails(1040, ItemClassification.filler, 1, False, "cosmetic"),
    # Key Items
    ItemNames.Payday: ItemDetails(1041, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.PrimePrimer: ItemDetails(1042, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.PlanarLead: ItemDetails(1043, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.ObsidianShellCasing: ItemDetails(1044, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.ArcanePowder: ItemDetails(1045, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.OublietteUnlock: ItemDetails(1046, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.OldCrest: ItemDetails(1047, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.GnawedKey: ItemDetails(1048, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.InfuriatingNote: ItemDetails(1049, ItemClassification.progression | ItemClassification.useful, 1),
    ItemNames.RnGDepartmentUnlock: ItemDetails(1050, ItemClassification.progression | ItemClassification.useful, 1),
}

AMMONOMICON_DICTIONARY = {
    ItemNames.magic_lamp: ItemDetails(0, ItemClassification.filler, 1, False),
    ItemNames.winchester: ItemDetails(1, ItemClassification.filler, 1, True),
    ItemNames.thompson: ItemDetails(2, ItemClassification.filler, 1, False),
    ItemNames.screecher: ItemDetails(3, ItemClassification.filler, 1, True),
    ItemNames.sticky_crossbow: ItemDetails(4, ItemClassification.filler, 1, True),
    ItemNames.awp: ItemDetails(5, ItemClassification.filler, 1, False),
    ItemNames.zorgun: ItemDetails(6, ItemClassification.filler, 1, True),
    ItemNames.barrel: ItemDetails(7, ItemClassification.filler, 1, True),
    ItemNames.bow: ItemDetails(8, ItemClassification.filler, 1, True),
    ItemNames.dueling_pistol: ItemDetails(9, ItemClassification.filler, 1, True),
    ItemNames.mega_douser: ItemDetails(10, ItemClassification.filler, 1, True),
    ItemNames.crossbow: ItemDetails(12, ItemClassification.filler, 1, True),
    ItemNames.thunderclap: ItemDetails(13, ItemClassification.filler, 1, True),
    ItemNames.bee_hive: ItemDetails(14, ItemClassification.filler, 1, True),
    ItemNames.ak47: ItemDetails(15, ItemClassification.filler, 1, True),
    ItemNames.yari_launcher: ItemDetails(16, ItemClassification.filler, 1, False),
    ItemNames.heck_blaster: ItemDetails(17, ItemClassification.filler, 1, True),
    ItemNames.blooper: ItemDetails(18, ItemClassification.filler, 1, True),
    ItemNames.grenade_launcher: ItemDetails(19, ItemClassification.filler, 1, True),
    ItemNames.moonscraper: ItemDetails(20, ItemClassification.filler, 1, True),
    ItemNames.bsg: ItemDetails(21, ItemClassification.filler, 1, True),
    ItemNames.shades_revolver: ItemDetails(22, ItemClassification.filler, 1, True),
    ItemNames.dungeon_eagle: ItemDetails(23, ItemClassification.filler, 1, True),
    ItemNames.dart_gun: ItemDetails(24, ItemClassification.filler, 1, True),
    ItemNames.m1: ItemDetails(25, ItemClassification.filler, 1, True),
    ItemNames.nail_gun: ItemDetails(26, ItemClassification.filler, 1, True),
    ItemNames.light_gun: ItemDetails(27, ItemClassification.filler, 1, True),
    ItemNames.mailbox: ItemDetails(28, ItemClassification.filler, 1, False),
    ItemNames.vertebraek47: ItemDetails(29, ItemClassification.filler, 1, True),
    ItemNames.m1911: ItemDetails(30, ItemClassification.filler, 1, True),
    ItemNames.klobbe: ItemDetails(31, ItemClassification.filler, 1, True),
    ItemNames.void_marshal: ItemDetails(32, ItemClassification.filler, 1, True),
    ItemNames.tear_jerker: ItemDetails(33, ItemClassification.filler, 1, True),
    ItemNames.smileys_revolver: ItemDetails(35, ItemClassification.filler, 1, True),
    ItemNames.megahand: ItemDetails(36, ItemClassification.filler, 1, True),
    ItemNames.serious_cannon: ItemDetails(37, ItemClassification.filler, 1, True),
    ItemNames.magnum: ItemDetails(38, ItemClassification.filler, 1, True),
    ItemNames.rpg: ItemDetails(39, ItemClassification.filler, 1, False),
    ItemNames.freeze_ray: ItemDetails(40, ItemClassification.filler, 1, False),
    ItemNames.heroine: ItemDetails(41, ItemClassification.filler, 1, False),
    ItemNames.trank_gun: ItemDetails(42, ItemClassification.filler, 1, True),
    ItemNames.machine_pistol: ItemDetails(43, ItemClassification.filler, 1, True),
    ItemNames.skull_spitter: ItemDetails(45, ItemClassification.filler, 1, True),
    ItemNames.jolter: ItemDetails(47, ItemClassification.filler, 1, True),
    ItemNames.sniper_rifle: ItemDetails(49, ItemClassification.filler, 1, True),
    ItemNames.saa: ItemDetails(50, ItemClassification.filler, 1, True),
    ItemNames.regular_shotgun: ItemDetails(51, ItemClassification.filler, 1, True),
    ItemNames.crescent_crossbow: ItemDetails(52, ItemClassification.filler, 1, True),
    ItemNames.au_gun: ItemDetails(53, ItemClassification.filler, 1, True),
    ItemNames.laser_rifle: ItemDetails(54, ItemClassification.filler, 1, True),
    ItemNames.void_shotgun: ItemDetails(55, ItemClassification.filler, 1, True),
    ItemNames.three_eight_special: ItemDetails(56, ItemClassification.filler, 1, True),
    ItemNames.alien_sidearm: ItemDetails(57, ItemClassification.filler, 1, True),
    ItemNames.void_core_assault_rifle: ItemDetails(58, ItemClassification.filler, 1, True),
    ItemNames.hegemony_rifle: ItemDetails(59, ItemClassification.filler, 1, True),
    ItemNames.demon_head: ItemDetails(60, ItemClassification.filler, 1, True),
    ItemNames.bundle_of_wands: ItemDetails(61, ItemClassification.filler, 1, False),
    ItemNames.colt_1851: ItemDetails(62, ItemClassification.filler, 1, True),
    ItemNames.medkit: ItemDetails(63, ItemClassification.filler, 1, True),
    ItemNames.potion_of_lead_skin: ItemDetails(64, ItemClassification.filler, 1, True),
    ItemNames.knife_shield: ItemDetails(65, ItemClassification.filler, 1, True),
    ItemNames.proximity_mine: ItemDetails(66, ItemClassification.filler, 1, True),
    ItemNames.bullet_time: ItemDetails(69, ItemClassification.filler, 1, True),
    ItemNames.decoy: ItemDetails(71, ItemClassification.filler, 1, True),
    ItemNames.supply_drop: ItemDetails(77, ItemClassification.filler, 1, True),
    ItemNames.makarov: ItemDetails(79, ItemClassification.filler, 1, True),
    ItemNames.budget_revolver: ItemDetails(80, ItemClassification.filler, 1, True),
    ItemNames.deck4rd: ItemDetails(81, ItemClassification.filler, 1, True),
    ItemNames.elephant_gun: ItemDetails(82, ItemClassification.filler, 1, False),
    ItemNames.unfinished_gun: ItemDetails(83, ItemClassification.filler, 1, True),
    ItemNames.vulcan_cannon: ItemDetails(84, ItemClassification.filler, 1, True),
    ItemNames.marine_sidearm: ItemDetails(86, ItemClassification.filler, 1, True),
    ItemNames.gamma_ray: ItemDetails(87, ItemClassification.filler, 1, False),
    ItemNames.robots_right_hand: ItemDetails(88, ItemClassification.filler, 1, True),
    ItemNames.rogue_special: ItemDetails(89, ItemClassification.filler, 1, True),
    ItemNames.eye_of_the_beholster: ItemDetails(90, ItemClassification.filler, 1, True),
    ItemNames.h4mmer: ItemDetails(91, ItemClassification.filler, 1, True),
    ItemNames.stinger: ItemDetails(92, ItemClassification.filler, 1, True),
    ItemNames.old_goldie: ItemDetails(93, ItemClassification.filler, 1, True),
    ItemNames.mac10: ItemDetails(94, ItemClassification.filler, 1, True),
    ItemNames.akey47: ItemDetails(95, ItemClassification.filler, 1, False),
    ItemNames.m16: ItemDetails(96, ItemClassification.filler, 1, False),
    ItemNames.polaris: ItemDetails(97, ItemClassification.filler, 1, False),
    ItemNames.patriot: ItemDetails(98, ItemClassification.filler, 1, False),
    ItemNames.rusty_sidearm: ItemDetails(99, ItemClassification.filler, 1, True),
    ItemNames.unicorn_horn: ItemDetails(100, ItemClassification.filler, 1, False),
}

TRAP_DICTIONARY = {
    "Rats!! Trap": ItemDetails(2000, ItemClassification.useful, 1),
    "Mimic Gun Trap": ItemDetails(2001, ItemClassification.useful, 1),
    "Curse Trap": ItemDetails(2002, ItemClassification.useful, 1),
    "Fumble Gun Trap": ItemDetails(2003, ItemClassification.useful, 1),
    "Fire Trap": ItemDetails(2004, ItemClassification.useful, 1),
    "Poison Trap": ItemDetails(2005, ItemClassification.useful, 1),
    "Curse Meter Trap": ItemDetails(2006, ItemClassification.useful, 1),
    "Enemy Trap": ItemDetails(2007, ItemClassification.useful, 1),
}

FULL_ITEM_DICTIONARY = {
    **AMMONOMICON_DICTIONARY,
    **ITEM_NAME_TO_DETAILS,
    **TRAP_DICTIONARY
}

FILLER_TO_PULL_FROM = []

# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class GungeonItem(Item):
    game = "Enter The Gungeon"

# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: EnterTheGungeonWorld) -> str:
    if world.random.randint(0, 99) < world.options.traps_percentage:
        return list(TRAP_DICTIONARY)[world.random.randint(0, len(TRAP_DICTIONARY)) - 1]
    elif len(FILLER_TO_PULL_FROM) <= 0:
        # If we somehow run out of unique ammonomicon items to pull from, just pull any item from the list, duplicates or base items are fine.
        return list(AMMONOMICON_DICTIONARY)[world.random.randint(0, len(AMMONOMICON_DICTIONARY)) - 1]
    else:
        return FILLER_TO_PULL_FROM.pop(world.random.randint(0, len(FILLER_TO_PULL_FROM)) - 1)


def create_item_with_details(world: EnterTheGungeonWorld, name: str) -> GungeonItem:
    if name in ITEM_NAME_TO_DETAILS:
        return GungeonItem(name, ITEM_NAME_TO_DETAILS[name].classification, ITEM_NAME_TO_DETAILS[name].itemID, world.player)
    elif name in AMMONOMICON_DICTIONARY:
        return GungeonItem(name, AMMONOMICON_DICTIONARY[name].classification, AMMONOMICON_DICTIONARY[name].itemID, world.player)
    elif name in TRAP_DICTIONARY:
        return GungeonItem(name, ItemClassification.trap, TRAP_DICTIONARY[name].itemID, world.player)

    # We should never get here, but return a safe item to have multiple of is somehow we do.
    return GungeonItem(ItemNames.FiveHedgemonyCredits, ITEM_NAME_TO_DETAILS[ItemNames.FiveHedgemonyCredits].classification, ITEM_NAME_TO_DETAILS[ItemNames.FiveHedgemonyCredits].itemID, world.player)

def check_for_options_rule(world: EnterTheGungeonWorld, name: str, item: ItemDetails) -> bool:
    should_add = True
    if name == ItemNames.ProgCasingMult and not world.options.casing_scaling:
        should_add = False
    if name == ItemNames.ProgCurseReduction and not world.options.curse_reduction_mode:
        should_add = False
    if name == ItemNames.ProgCredMult and not world.options.hegemony_scaling:
        should_add = False
    if name == ItemNames.ProgStartChest and not world.options.progressive_start_chest:
        should_add = False
    if item.grouping == "cosmetic" and not world.options.include_skins:
        should_add = False
    if item.grouping == "character":
        # Handle characters separately, so don't add now
        should_add = False
    return should_add

# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: EnterTheGungeonWorld) -> None:
    """
    Rough plan:
    Generate all custom items into the itempool, these are all the things we will always want in all runs.
    Add in anything that the options might dictate.
    Any remaining slots (difference of itempool and locations) will be filled in with ammonomicon unlockable items, plus a small percent of traps/filler consumables if enabled.
    """
    item_pool: list[Item] = []
    for key in ITEM_NAME_TO_DETAILS:
        for count in range(ITEM_NAME_TO_DETAILS[key].quantity):
            if check_for_options_rule(world, key, ITEM_NAME_TO_DETAILS[key]):
                item_pool.append(world.create_item(key))

    # Character items
    character_items_to_add: list[str] = [
        ItemNames.PlayAsPilot,
        ItemNames.PlayAsHunter,
        ItemNames.PlayAsConvict,
        ItemNames.PlayAsMarine,
        ItemNames.PlayAsBullet,
        ItemNames.PlayAsRobot,
        ItemNames.PlayAsGunslinger
    ]

    # Depending on the option, precollect the character(s) available at the start.
    match world.options.limit_starting_gungeoneer:
        case "off":
            character_items_to_add.remove(ItemNames.PlayAsPilot)
            world.push_precollected(world.create_item(ItemNames.PlayAsPilot))
            character_items_to_add.remove(ItemNames.PlayAsMarine)
            world.push_precollected(world.create_item(ItemNames.PlayAsMarine))
            character_items_to_add.remove(ItemNames.PlayAsConvict)
            world.push_precollected(world.create_item(ItemNames.PlayAsConvict))
            character_items_to_add.remove(ItemNames.PlayAsHunter)
            world.push_precollected(world.create_item(ItemNames.PlayAsHunter))
        case "pilot":
            character_items_to_add.remove(ItemNames.PlayAsPilot)
            world.push_precollected(world.create_item(ItemNames.PlayAsPilot))
        case "convict":
            character_items_to_add.remove(ItemNames.PlayAsConvict)
            world.push_precollected(world.create_item(ItemNames.PlayAsConvict))
        case "marine":
            character_items_to_add.remove(ItemNames.PlayAsMarine)
            world.push_precollected(world.create_item(ItemNames.PlayAsMarine))
        case "hunter":
            character_items_to_add.remove(ItemNames.PlayAsHunter)
            world.push_precollected(world.create_item(ItemNames.PlayAsHunter))
        case "bullet":
            character_items_to_add.remove(ItemNames.PlayAsBullet)
            world.push_precollected(world.create_item(ItemNames.PlayAsBullet))
        case "robot":
            character_items_to_add.remove(ItemNames.PlayAsRobot)
            world.push_precollected(world.create_item(ItemNames.PlayAsRobot))
        case "gunslinger":
            character_items_to_add.remove(ItemNames.PlayAsGunslinger)
            world.push_precollected(world.create_item(ItemNames.PlayAsGunslinger))
        case "random_character_from_base_roster":
            world.push_precollected(world.create_item(character_items_to_add.pop(world.random.randint(0, 3))))
        case "random_character_from_full_roster":
            world.push_precollected(world.create_item(character_items_to_add.pop(world.random.randint(0, len(character_items_to_add)) - 1)))

    # Add remaining characters
    for character in character_items_to_add:
        item_pool.append(world.create_item(character))

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    for key in AMMONOMICON_DICTIONARY:
        if not AMMONOMICON_DICTIONARY[key].isBaseAmmonomicon:
            FILLER_TO_PULL_FROM.append(key)


    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += item_pool