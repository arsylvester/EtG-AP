from dataclasses import dataclass

from .items import TRAP_DICTIONARY

from Options import Choice, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, DeathLink

class EnableHegemonyCreditScalingOption(DefaultOnToggle):
    """
    Enable a progressive scaling AP item which multiplies to the amount of Hegemony Credits dropped.

    TODO: Complete this description! 
    """
    display_name = "Progressive Scaling for Hegemony Credits"

class EnableCasingScalingOption(DefaultOnToggle):
    """
    Enable a progressive scaling multiplier to the amount of Casings dropped.

    The multiplier is controlled by a progressive AP item.

    TODO: Complete this description! 
    """
    display_name = "Progressive Scaling for Casings"

class EnableTrapsOption(OptionSet):
    """
    Control which traps should be included in the AP item pool.
    """
    display_name = "Enable Traps"
    valid_keys = {trap for trap in TRAP_DICTIONARY.keys()}
    default = valid_keys

class TrapPercentageOption(Range):
    """
    Define the percentage of filler AP item slots that become traps.

    (All gungeon guns/items are considered filler AP items)
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 5

class LimitStartingGungeoneerOption(OptionSet):
    """
    Start the game with only 1 playable gungeoneer. All remaining gungeoneers will be unlocked as AP items.

    Select **"Off"** to start with all 4 default gungeoneers unlocked. 
    """ 
    display_name = "Start With Single Playable Character"
    option_off = 0
    option_convict = 1
    option_hunter = 2
    option_marine = 3
    option_hunter = 4
    option_bullet = 5
    option_robot = 6
    option_paradox = 7
    option_gunslinger = 8
    option_random_character_from_base_roster = 9
    option_random_character_from_full_roster = 10
    default = 0

class CurseReductionModeOption(Toggle):
    """
    Begin the playthrough with a high curse value that persists between runs. The curse level is permanently lowered via a progressive AP item.  
    """
    display_name = "Curse Reduction Mode (Not Implemented)"

class IncludeSkinsInItemPool(DefaultOnToggle):
    """
    Unlock alternate character/weapon skins as AP items.

    If false, the alternate skins will be excluded from the item pool.
    """
    # TODO: Enhance the description to indicate if the skins can still be unlocked in-game if the value is False.
    display_name = "Alternate Skins from AP Items"

class NoHitBossesAsProgressionOption(Choice):
    """
    Define how the AP logic should prioritize earning a floor's Master Round for the first time.

    - **Allow Priority:** You may be expected to No-Hit floor bosses to unlock progression AP items.
    - **Forbid Priority:** Locations achieved by No-Hitting a floor boss will never include progression AP items.
    """
    display_name = "Earning Master Rounds"
    option_allow_priority_items = 1
    option_forbid_priority_items = 2
    default = 1

class MiniBossesAsProgressionOption(Choice):
    """
    Define how the AP logic should prioritize defeating mini-bosses for the first time.

    - **Allow Priority:** You may be expected to defeat specific mini-bosses to unlock progression AP items.
    - **Forbid Priority:** Locations achieved by defeating specific mini-bosses will never include progression AP items.       
    """
    display_name = "Mini Bosses"
    option_allow_priority_items = 1
    option_forbid_priority_items = 2
    default = 1

class KillingRatAsProgressionOption(Choice):
    """
    Define how the AP logic should handle defeating the first 2 phases of the Resourceful Rat boss fight.

    - **Allow Priority:** To unlock progression AP items, you may be expected to complete the first 2 phases of the rat fight.
    - **Forbid Priority:** This location will never include progression AP items.       
    """
    display_name = "Resourceful Rat (Phases 1 & 2)"
    option_allow_priority_items = 1
    option_forbid_priority_items = 2
    default = 1

class RatChestsAsProgressionOption(Choice):
    """
    Define how the AP logic should handle the chests unlocked by defeating the Resourceful Rat's punch-out phase.

    - **Allow Priority:** The rat chests may contain progression AP items.
    - **Forbid Priority:** The rat chests will never include progression AP items.       
    """
    # TODO: Fact check the description for this option.
    display_name = "Resourceful Rat (Punch Out)"
    option_allow_priority_items = 1
    option_forbid_priority_items = 2
    default = 1

class IncludeFrifleQuestsInLogicOption(Toggle):
    """
    Determine if the hunting quests given Frifle and the Grey Mauser should be included in the AP logic as locations. 
    """
    display_name = "Include Hunting Quests"

@dataclass
class GungeonOptions(PerGameCommonOptions):
    limit_starting_gungeoneer: LimitStartingGungeoneerOption
    death_link: DeathLink
    curse_reduction_mode: CurseReductionModeOption
    include_hunting_quests: IncludeFrifleQuestsInLogicOption
    include_skins: IncludeSkinsInItemPool
    enable_traps: EnableTrapsOption
    traps_percentage: TrapPercentageOption

    # Currency Scaling Options
    hegemony_scaling: EnableHegemonyCreditScalingOption
    casing_scaling: EnableCasingScalingOption

    # Priority Location Controls
    priority_nohit_bosses: NoHitBossesAsProgressionOption
    priority_mini_bosses: MiniBossesAsProgressionOption
    priority_rat_fight: KillingRatAsProgressionOption
    priority_rat_chests: RatChestsAsProgressionOption


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Currency Scaling Options", [
            EnableHegemonyCreditScalingOption, 
            EnableCasingScalingOption
        ],
    ),
    OptionGroup(
        "Priority Location Controls", [
            NoHitBossesAsProgressionOption,
            MiniBossesAsProgressionOption, 
            KillingRatAsProgressionOption, 
            RatChestsAsProgressionOption
        ],
    ),
]