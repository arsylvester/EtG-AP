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
    # progressive
    ItemNames.ProgCasingMult: ItemDetails(1018, ItemClassification.useful, 3),
    ItemNames.ProgCredMult: ItemDetails(1019, ItemClassification.useful, 3),
    ItemNames.ProgCurseReduction: ItemDetails(1020, ItemClassification.useful, 3),
    ItemNames.ProgCoolness: ItemDetails(1021, ItemClassification.useful, 3),
    ItemNames.ProgStartChest: ItemDetails(1022, ItemClassification.useful, 5),
    ItemNames.ProgShortCut: ItemDetails(1023, ItemClassification.useful, 5),
    ItemNames.FiveHedgemonyCredits: ItemDetails(1024, ItemClassification.useful, 5),
}

AMMONOMICON_DICTIONARY = {
    ItemNames.magic_lamp: ItemDetails(0, ItemClassification.filler, 1, False),
    ItemNames.winchester: ItemDetails(1, ItemClassification.filler, 1, True),
    ItemNames.thompson: ItemDetails(2, ItemClassification.filler, 1, False),
    ItemNames.screecher: ItemDetails(3, ItemClassification.filler, 1, True),
    ItemNames.sticky_crossbow: ItemDetails(4, ItemClassification.filler, 1, True),
    ItemNames.awp: ItemDetails(5, ItemClassification.filler, 1, False),
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
    # TODO: Set up special logic that most of the filler will be unique gungeon gun/item unlocks

    if world.random.randint(0, 99) < world.options.traps_percentage:
        return list(TRAP_DICTIONARY)[world.random.randint(0, len(TRAP_DICTIONARY)) - 1]
    elif len(FILLER_TO_PULL_FROM) <= 0:
        # If we somehow run out of unique ammonomicon items to pull from, just pull any item from the list, duplicates or base items are fine.
        return list(AMMONOMICON_DICTIONARY)[world.random.randint(0, len(AMMONOMICON_DICTIONARY)) - 1]
    else:
        return FILLER_TO_PULL_FROM.pop(world.random.randint(0, len(FILLER_TO_PULL_FROM)) - 1)


def create_item_with_details(world: EnterTheGungeonWorld, name: str) -> GungeonItem:
    #TODO: Include any changes to items depending on options here.

    if name in ITEM_NAME_TO_DETAILS:
        return GungeonItem(name, ITEM_NAME_TO_DETAILS[name].classification, ITEM_NAME_TO_DETAILS[name].itemID, world.player)
    elif name in AMMONOMICON_DICTIONARY:
        return GungeonItem(name, AMMONOMICON_DICTIONARY[name].classification, AMMONOMICON_DICTIONARY[name].itemID, world.player)
    elif name in TRAP_DICTIONARY:
        return GungeonItem(name, ItemClassification.trap, TRAP_DICTIONARY[name].itemID, world.player)

    # We should never get here, but return a safe item to have multiple of is somehow we do.
    return GungeonItem(ItemNames.FiveHedgemonyCredits, ITEM_NAME_TO_DETAILS[ItemNames.FiveHedgemonyCredits].classification, ITEM_NAME_TO_DETAILS[ItemNames.FiveHedgemonyCredits].itemID, world.player)


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
            item_pool.append(world.create_item(key))

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