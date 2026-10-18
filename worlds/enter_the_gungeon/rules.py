from __future__ import annotations

from typing import TYPE_CHECKING

# from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .Names import RegionName
from .Names import ItemNames
from .regions import get_connection_name

if TYPE_CHECKING:
    from .world import EnterTheGungeonWorld


def set_all_rules(world: EnterTheGungeonWorld) -> None:
    set_all_entrance_rules(world)
    # set_all_location_rules(world)
    # set_completion_condition(world)


def set_all_entrance_rules(world: EnterTheGungeonWorld) -> None:
    # Shops
    ox_page_1 = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.OxAndCadence1))
    ox_page_2 = world.get_entrance(get_connection_name(RegionName.OxAndCadence1, RegionName.OxAndCadence2))
    ox_page_3 = world.get_entrance(get_connection_name(RegionName.OxAndCadence2, RegionName.OxAndCadence3))
    ox_page_4 = world.get_entrance(get_connection_name(RegionName.OxAndCadence3, RegionName.OxAndCadence4))
    ox_page_5 = world.get_entrance(get_connection_name(RegionName.OxAndCadence4, RegionName.OxAndCadence5))
    ox_page_6 = world.get_entrance(get_connection_name(RegionName.OxAndCadence5, RegionName.OxAndCadence6))
    ox_page_7 = world.get_entrance(get_connection_name(RegionName.OxAndCadence6, RegionName.OxAndCadence7))
    goopton_page_1 = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Goopton1))
    goopton_page_2 = world.get_entrance(get_connection_name(RegionName.Goopton1, RegionName.Goopton2))
    trorc_page_1 = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Trorc1))
    trorc_page_2 = world.get_entrance(get_connection_name(RegionName.Trorc1, RegionName.Trorc2))
    doug_page_1 = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Doug1))
    doug_page_2 = world.get_entrance(get_connection_name(RegionName.Doug1, RegionName.Doug2))
    doug_page_3 = world.get_entrance(get_connection_name(RegionName.Doug2, RegionName.Doug3))
    doug_page_4 = world.get_entrance(get_connection_name(RegionName.Doug3, RegionName.Doug4))
    doug_page_5 = world.get_entrance(get_connection_name(RegionName.Doug4, RegionName.Doug5))
    doug_page_6 = world.get_entrance(get_connection_name(RegionName.Doug5, RegionName.Doug6))

    # Other
    past_killable = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.PastKillable))
    payday_items_access = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Payday))
    rat_lair_access = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.RatLair))
    rat_fight_access = world.get_entrance(get_connection_name(RegionName.RatLair, RegionName.RatFight))
    oubliette_access = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Oubliette))
    abbey_access = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.Abbey))
    rngdept_access = world.get_entrance(get_connection_name(RegionName.Breach, RegionName.RngDepartment))


    # Ox and Cadence access
    world.set_rule(ox_page_1, Has(ItemNames.OxAndCadence, 1))
    world.set_rule(ox_page_2, Has(ItemNames.OxAndCadence, 2))
    world.set_rule(ox_page_3, Has(ItemNames.OxAndCadence, 3))
    world.set_rule(ox_page_4, Has(ItemNames.OxAndCadence, 4))
    world.set_rule(ox_page_5, Has(ItemNames.OxAndCadence, 5))
    world.set_rule(ox_page_6, Has(ItemNames.OxAndCadence, 6))
    world.set_rule(ox_page_7, Has(ItemNames.OxAndCadence, 7))
    
    # goopton access
    world.set_rule(goopton_page_1, Has(ItemNames.ProfessorGoop, 1))
    world.set_rule(goopton_page_2, Has(ItemNames.ProfessorGoop, 2))
    
    # trorc access
    world.set_rule(trorc_page_1, Has(ItemNames.Trorc, 1))
    world.set_rule(trorc_page_2, Has(ItemNames.Trorc, 2))

    # doug access
    world.set_rule(doug_page_1, Has(ItemNames.Doug, 1))
    world.set_rule(doug_page_2, Has(ItemNames.Doug, 2))
    world.set_rule(doug_page_3, Has(ItemNames.Doug, 3))
    world.set_rule(doug_page_4, Has(ItemNames.Doug, 4))
    world.set_rule(doug_page_5, Has(ItemNames.Doug, 5))
    world.set_rule(doug_page_6, Has(ItemNames.Doug, 6))

    # kill the past
    world.set_rule(past_killable, HasAll(ItemNames.PrimePrimer, ItemNames.ArcanePowder, ItemNames.PlanarLead, ItemNames.ObsidianShellCasing))

    # secret area access
    world.set_rule(oubliette_access, Has(ItemNames.OublietteUnlock))
    world.set_rule(abbey_access, Has(ItemNames.OldCrest))
    world.set_rule(rat_lair_access, Has(ItemNames.GnawedKey))
    world.set_rule(rngdept_access, Has(ItemNames.RnGDepartmentUnlock))

    # resourceful rat fight
    world.set_rule(rat_fight_access, Has(ItemNames.InfuriatingNote))

# def set_all_location_rules(world: EnterTheGungeonWorld) -> None:
    # TODO: Figure this out...

# def set_completion_condition(world: EnterTheGungeonWorld) -> None:
    # TODO: Figure out if this is even needed. It seems like this might just be handled by the client.