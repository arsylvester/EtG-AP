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
    ItemNames.magic_lamp: ItemDetails(900, ItemClassification.filler, 1, False), #0 can't be used as an id
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
    ItemNames.scope: ItemDetails(102, ItemClassification.filler, 1, True),
    ItemNames.ration: ItemDetails(104, ItemClassification.filler, 1, False),
    ItemNames.fortunes_favor: ItemDetails(105, ItemClassification.filler, 1, True),
    ItemNames.jetpack: ItemDetails(106, ItemClassification.filler, 1, True),
    ItemNames.raiden_coil: ItemDetails(107, ItemClassification.filler, 1, False),
    ItemNames.bomb: ItemDetails(108, ItemClassification.filler, 1, True),
    ItemNames.ice_bomb: ItemDetails(109, ItemClassification.filler, 1, True),
    ItemNames.magic_sweet: ItemDetails(110, ItemClassification.filler, 1, True),
    ItemNames.heavy_bullets: ItemDetails(111, ItemClassification.filler, 1, True),
    ItemNames.cartographers_ring: ItemDetails(112, ItemClassification.filler, 1, True),
    ItemNames.rocket_powered_bullets: ItemDetails(113, ItemClassification.filler, 1, False),
    ItemNames.bionic_leg: ItemDetails(114, ItemClassification.filler, 1, True),
    ItemNames.ballot: ItemDetails(115, ItemClassification.filler, 1, True),
    ItemNames.ammo_synthesizer: ItemDetails(116, ItemClassification.filler, 1, True),
    ItemNames.eyepatch: ItemDetails(118, ItemClassification.filler, 1, False),
    ItemNames.metronome: ItemDetails(119, ItemClassification.filler, 1, True),
    ItemNames.disintegrator: ItemDetails(121, ItemClassification.filler, 1, True),
    ItemNames.blunderbuss: ItemDetails(122, ItemClassification.filler, 1, True),
    ItemNames.pulse_cannon: ItemDetails(123, ItemClassification.filler, 1, True),
    ItemNames.cactus: ItemDetails(124, ItemClassification.filler, 1, True),
    ItemNames.flame_hand: ItemDetails(125, ItemClassification.filler, 1, True),
    ItemNames.shotbow: ItemDetails(126, ItemClassification.filler, 1, True),
    ItemNames.junk: ItemDetails(127, ItemClassification.filler, 1, True),
    ItemNames.rube_adyne_mk2: ItemDetails(128, ItemClassification.filler, 1, True),
    ItemNames.com4nd0: ItemDetails(129, ItemClassification.filler, 1, False),
    ItemNames.glacier: ItemDetails(130, ItemClassification.filler, 1, True),
    ItemNames.utility_belt: ItemDetails(131, ItemClassification.filler, 1, True),
    ItemNames.ring_of_miserly_protection: ItemDetails(132, ItemClassification.filler, 1, True),
    ItemNames.backpack: ItemDetails(133, ItemClassification.filler, 1, True),
    ItemNames.ammo_belt: ItemDetails(134, ItemClassification.filler, 1, True),
    ItemNames.cog_of_battle: ItemDetails(135, ItemClassification.filler, 1, True),
    ItemNames.c4: ItemDetails(136, ItemClassification.filler, 1, True),
    ItemNames.honeycomb: ItemDetails(138, ItemClassification.filler, 1, True),
    ItemNames.master_of_unlocking: ItemDetails(140, ItemClassification.filler, 1, True),
    ItemNames.rube_adyne_prototype: ItemDetails(142, ItemClassification.filler, 1, True),
    ItemNames.shotgun_full_of_hate: ItemDetails(143, ItemClassification.filler, 1, True),
    ItemNames.witch_pistol: ItemDetails(145, ItemClassification.filler, 1, True),
    ItemNames.dragunfire: ItemDetails(145, ItemClassification.filler, 1, True),
    ItemNames.face_melter: ItemDetails(149, ItemClassification.filler, 1, False),
    ItemNames.t_shirt_cannon: ItemDetails(150, ItemClassification.filler, 1, True),
    ItemNames.the_membrane: ItemDetails(151, ItemClassification.filler, 1, False),
    ItemNames.the_kiln: ItemDetails(152, ItemClassification.filler, 1, True),
    ItemNames.shock_rifle: ItemDetails(153, ItemClassification.filler, 1, True),
    ItemNames.trashcannon: ItemDetails(154, ItemClassification.filler, 1, True),
    ItemNames.singularity: ItemDetails(155, ItemClassification.filler, 1, False),
    ItemNames.laser_lotus: ItemDetails(156, ItemClassification.filler, 1, True),
    ItemNames.big_iron: ItemDetails(157, ItemClassification.filler, 1, True),
    ItemNames.amulet_of_the_pit_lord: ItemDetails(158, ItemClassification.filler, 1, True),
    ItemNames.gundromeda_strain: ItemDetails(159, ItemClassification.filler, 1, False),
    ItemNames.gunknight_helmet: ItemDetails(160, ItemClassification.filler, 1, False),
    ItemNames.gunknight_greaves: ItemDetails(161, ItemClassification.filler, 1, True),
    ItemNames.gunknight_gauntlet: ItemDetails(162, ItemClassification.filler, 1, True),
    ItemNames.gunknight_armor: ItemDetails(163, ItemClassification.filler, 1, True),
    ItemNames.heart_synthesizer: ItemDetails(164, ItemClassification.filler, 1, True),
    ItemNames.oiled_cylinder: ItemDetails(165, ItemClassification.filler, 1, True),
    ItemNames.shelleton_key: ItemDetails(166, ItemClassification.filler, 1, False),
    ItemNames.bloody_eye: ItemDetails(167, ItemClassification.filler, 1, False),
    ItemNames.double_vision: ItemDetails(168, ItemClassification.filler, 1, True),
    ItemNames.black_hole_gun: ItemDetails(169, ItemClassification.filler, 1, False),
    ItemNames.ice_cube: ItemDetails(170, ItemClassification.filler, 1, True),
    ItemNames.ghost_bullets: ItemDetails(172, ItemClassification.filler, 1, True),
    ItemNames.potion_of_gun_friendship: ItemDetails(174, ItemClassification.filler, 1, True),
    ItemNames.tangler: ItemDetails(175, ItemClassification.filler, 1, False),
    ItemNames.gungeon_ant: ItemDetails(176, ItemClassification.filler, 1, True),
    ItemNames.alien_engine: ItemDetails(177, ItemClassification.filler, 1, True),
    ItemNames.crestfaller: ItemDetails(178, ItemClassification.filler, 1, True),
    ItemNames.proton_backpack: ItemDetails(179, ItemClassification.filler, 1, True),
    ItemNames.grasschopper: ItemDetails(180, ItemClassification.filler, 1, False),
    ItemNames.winchester_rifle: ItemDetails(181, ItemClassification.filler, 1, True),
    ItemNames.grey_mauser: ItemDetails(182, ItemClassification.filler, 1, False),
    ItemNames.the_judge: ItemDetails(184, ItemClassification.filler, 1, True),
    ItemNames.machine_fist: ItemDetails(186, ItemClassification.filler, 1, True),
    ItemNames.disarming_personality: ItemDetails(187, ItemClassification.filler, 1, False),
    ItemNames.rolling_eye: ItemDetails(190, ItemClassification.filler, 1, False),
    ItemNames.ring_of_fire_resistance: ItemDetails(191, ItemClassification.filler, 1, True),
    ItemNames.bug_boots: ItemDetails(193, ItemClassification.filler, 1, False),
    ItemNames.fossilized_gun: ItemDetails(196, ItemClassification.filler, 1, False),
    ItemNames.pea_shooter: ItemDetails(197, ItemClassification.filler, 1, False),
    ItemNames.gunslingers_ashes: ItemDetails(198, ItemClassification.filler, 1, False),
    ItemNames.luxin_cannon: ItemDetails(199, ItemClassification.filler, 1, True),
    ItemNames.charmed_bow: ItemDetails(200, ItemClassification.filler, 1, True),
    ItemNames.portable_turret: ItemDetails(201, ItemClassification.filler, 1, False),
    ItemNames.sawed_off: ItemDetails(202, ItemClassification.filler, 1, True),
    ItemNames.cigarettes: ItemDetails(203, ItemClassification.filler, 1, True),
    ItemNames.irradiated_lead: ItemDetails(204, ItemClassification.filler, 1, True),
    ItemNames.poison_vial: ItemDetails(205, ItemClassification.filler, 1, True),
    ItemNames.charm_horn: ItemDetails(206, ItemClassification.filler, 1, True),
    ItemNames.plague_pistol: ItemDetails(207, ItemClassification.filler, 1, False),
    ItemNames.plunger: ItemDetails(208, ItemClassification.filler, 1, False),
    ItemNames.sense_of_direction: ItemDetails(209, ItemClassification.filler, 1, True),
    ItemNames.gunbow: ItemDetails(210, ItemClassification.filler, 1, True),
    ItemNames.ballistic_boots: ItemDetails(212, ItemClassification.filler, 1, True),
    ItemNames.lichy_trigger_finger: ItemDetails(213, ItemClassification.filler, 1, True),
    ItemNames.coin_crown: ItemDetails(214, ItemClassification.filler, 1, False),
    ItemNames.box: ItemDetails(216, ItemClassification.filler, 1, False),
    ItemNames.old_knights_shield: ItemDetails(219, ItemClassification.filler, 1, False),
    ItemNames.old_knights_helm: ItemDetails(222, ItemClassification.filler, 1, False),
    ItemNames.cold_45: ItemDetails(223, ItemClassification.filler, 1, True),
    ItemNames.ice_breaker: ItemDetails(225, ItemClassification.filler, 1, False),
    ItemNames.particulator: ItemDetails(228, ItemClassification.filler, 1, True),
    ItemNames.hegemony_carbine: ItemDetails(229, ItemClassification.filler, 1, False),
    ItemNames.helix: ItemDetails(230, ItemClassification.filler, 1, True),
    ItemNames.gilded_hydra: ItemDetails(231, ItemClassification.filler, 1, False),
    ItemNames.space_friend: ItemDetails(232, ItemClassification.filler, 1, False),
    ItemNames.ibomb_companion_app: ItemDetails(234, ItemClassification.filler, 1, True),
    ItemNames.aged_bell: ItemDetails(237, ItemClassification.filler, 1, True),
    ItemNames.duct_tape: ItemDetails(239, ItemClassification.filler, 1, False),
    ItemNames.crutch: ItemDetails(240, ItemClassification.filler, 1, True),
    ItemNames.scattershot: ItemDetails(241, ItemClassification.filler, 1, True),
    ItemNames.napalm_strike: ItemDetails(242, ItemClassification.filler, 1, False),
    ItemNames.owl: ItemDetails(249, ItemClassification.filler, 1, False),
    ItemNames.grappling_hook: ItemDetails(250, ItemClassification.filler, 1, True),
    ItemNames.air_strike: ItemDetails(252, ItemClassification.filler, 1, False),
    ItemNames.gungeon_pepper: ItemDetails(253, ItemClassification.filler, 1, True),
    ItemNames.ring_of_chest_friendship: ItemDetails(254, ItemClassification.filler, 1, True),
    ItemNames.ancient_heros_bandana: ItemDetails(255, ItemClassification.filler, 1, False),
    ItemNames.heavy_boots: ItemDetails(256, ItemClassification.filler, 1, True),
    ItemNames.broccoli: ItemDetails(258, ItemClassification.filler, 1, False),
    ItemNames.antibody: ItemDetails(259, ItemClassification.filler, 1, False),
    ItemNames.pink_guon_stone: ItemDetails(260, ItemClassification.filler, 1, True),
    ItemNames.white_guon_stone: ItemDetails(262, ItemClassification.filler, 1, True),
    ItemNames.orange_guon_stone: ItemDetails(263, ItemClassification.filler, 1, True),
    ItemNames.clear_guon_stone: ItemDetails(264, ItemClassification.filler, 1, True),
    ItemNames.old_knights_flask: ItemDetails(267, ItemClassification.filler, 1, True),
    ItemNames.red_guon_stone: ItemDetails(269, ItemClassification.filler, 1, True),
    ItemNames.blue_guon_stone: ItemDetails(270, ItemClassification.filler, 1, True),
    ItemNames.riddle_of_lead: ItemDetails(271, ItemClassification.filler, 1, False),
    ItemNames.iron_coin: ItemDetails(272, ItemClassification.filler, 1, False),
    ItemNames.laser_sight: ItemDetails(273, ItemClassification.filler, 1, True),
    ItemNames.dark_marker: ItemDetails(274, ItemClassification.filler, 1, True),
    ItemNames.flare_gun: ItemDetails(275, ItemClassification.filler, 1, True),
    ItemNames.spice: ItemDetails(276, ItemClassification.filler, 1, False),
    ItemNames.fat_bullets: ItemDetails(277, ItemClassification.filler, 1, False),
    ItemNames.frost_bullets: ItemDetails(278, ItemClassification.filler, 1, True),
    ItemNames.super_hot_watch: ItemDetails(279, ItemClassification.filler, 1, False),
    ItemNames.drum_clip: ItemDetails(280, ItemClassification.filler, 1, True),
    ItemNames.gungeon_blueprint: ItemDetails(281, ItemClassification.filler, 1, False),
    ItemNames.homing_bullets: ItemDetails(284, ItemClassification.filler, 1, True),
    ItemNames.blood_brooch: ItemDetails(285, ItemClassification.filler, 1, False),
    ItemNames.plus_one_bullets: ItemDetails(286, ItemClassification.filler, 1, False),
    ItemNames.backup_gun: ItemDetails(287, ItemClassification.filler, 1, True),
    ItemNames.bouncy_bullets: ItemDetails(288, ItemClassification.filler, 1, True),
    ItemNames.seven_leaf_clover: ItemDetails(289, ItemClassification.filler, 1, False),
    ItemNames.sunglasses: ItemDetails(290, ItemClassification.filler, 1, False),
    ItemNames.meatbun: ItemDetails(291, ItemClassification.filler, 1, True),
    ItemNames.molotov_launcher: ItemDetails(292, ItemClassification.filler, 1, True),
    ItemNames.mimic_tooth_necklace: ItemDetails(293, ItemClassification.filler, 1, False),
    ItemNames.ring_of_mimic_friendship: ItemDetails(294, ItemClassification.filler, 1, True),
    ItemNames.hot_lead: ItemDetails(295, ItemClassification.filler, 1, False),
    ItemNames.shock_rounds: ItemDetails(298, ItemClassification.filler, 1, True),
    ItemNames.dog: ItemDetails(300, ItemClassification.filler, 1, False),
    ItemNames.super_space_turtle: ItemDetails(301, ItemClassification.filler, 1, False),
    ItemNames.explosive_rounds: ItemDetails(304, ItemClassification.filler, 1, True),
    ItemNames.escape_rope: ItemDetails(306, ItemClassification.filler, 1, True),
    ItemNames.wax_wings: ItemDetails(307, ItemClassification.filler, 1, True),
    ItemNames.cluster_mine: ItemDetails(308, ItemClassification.filler, 1, False),
    ItemNames.cloranthy_ring: ItemDetails(309, ItemClassification.filler, 1, True),
    ItemNames.clone: ItemDetails(311, ItemClassification.filler, 1, False),
    ItemNames.blast_helmet: ItemDetails(312, ItemClassification.filler, 1, False),
    ItemNames.monster_blood: ItemDetails(313, ItemClassification.filler, 1, False),
    ItemNames.nanomachines: ItemDetails(314, ItemClassification.filler, 1, False),
    ItemNames.gunboots: ItemDetails(315, ItemClassification.filler, 1, False),
    ItemNames.r2g2: ItemDetails(318, ItemClassification.filler, 1, False),
    ItemNames.ticket: ItemDetails(320, ItemClassification.filler, 1, False),
    ItemNames.gold_ammolet: ItemDetails(321, ItemClassification.filler, 1, True),
    ItemNames.lodestone_ammolet: ItemDetails(322, ItemClassification.filler, 1, True),
    ItemNames.angry_bullets: ItemDetails(323, ItemClassification.filler, 1, False),
    ItemNames.chaos_ammolet: ItemDetails(325, ItemClassification.filler, 1, True),
    ItemNames.number_2: ItemDetails(326, ItemClassification.filler, 1, False),
    ItemNames.corsair: ItemDetails(327, ItemClassification.filler, 1, True),
    ItemNames.charge_shot: ItemDetails(328, ItemClassification.filler, 1, True),
    ItemNames.zilla_shotgun: ItemDetails(329, ItemClassification.filler, 1, True),
    ItemNames.the_emperor: ItemDetails(330, ItemClassification.filler, 1, True),
    ItemNames.science_cannon: ItemDetails(331, ItemClassification.filler, 1, False),
    ItemNames.lil_bomber: ItemDetails(332, ItemClassification.filler, 1, True),
    ItemNames.mutation: ItemDetails(333, ItemClassification.filler, 1, False),
    ItemNames.wind_up_gun: ItemDetails(334, ItemClassification.filler, 1, True),
    ItemNames.silencer: ItemDetails(335, ItemClassification.filler, 1, True),
    ItemNames.pitchfork: ItemDetails(336, ItemClassification.filler, 1, True),
    ItemNames.composite_gun: ItemDetails(337, ItemClassification.filler, 1, True),
    ItemNames.gunther: ItemDetails(338, ItemClassification.filler, 1, False),
    ItemNames.mahoguny: ItemDetails(339, ItemClassification.filler, 1, True),
    ItemNames.lower_case_r: ItemDetails(340, ItemClassification.filler, 1, True),
    ItemNames.buzzkill: ItemDetails(341, ItemClassification.filler, 1, True),
    ItemNames.uranium_ammolet: ItemDetails(342, ItemClassification.filler, 1, True),
    ItemNames.copper_ammolet: ItemDetails(343, ItemClassification.filler, 1, True),
    ItemNames.frost_ammolet: ItemDetails(344, ItemClassification.filler, 1, True),
    ItemNames.fightsabre: ItemDetails(345, ItemClassification.filler, 1, True),
    ItemNames.huntsman: ItemDetails(346, ItemClassification.filler, 1, True),
    ItemNames.shotgrub: ItemDetails(347, ItemClassification.filler, 1, True),
    ItemNames.shadow_bullets: ItemDetails(352, ItemClassification.filler, 1, False),
    ItemNames.enraging_photo: ItemDetails(353, ItemClassification.filler, 1, False),
    ItemNames.military_training: ItemDetails(354, ItemClassification.filler, 1, False),
    ItemNames.trusty_lockpicks: ItemDetails(356, ItemClassification.filler, 1, False),
    ItemNames.cat_claw: ItemDetails(357, ItemClassification.filler, 1, False),
    ItemNames.railgun: ItemDetails(358, ItemClassification.filler, 1, False),
    ItemNames.compressed_air_tank: ItemDetails(359, ItemClassification.filler, 1, False),
    ItemNames.snakemaker: ItemDetails(360, ItemClassification.filler, 1, False),
    ItemNames.bullet_bore: ItemDetails(362, ItemClassification.filler, 1, False),
    ItemNames.trick_gun: ItemDetails(363, ItemClassification.filler, 1, True),
    ItemNames.heart_of_ice: ItemDetails(364, ItemClassification.filler, 1, True),
    ItemNames.mass_shotgun: ItemDetails(365, ItemClassification.filler, 1, False),
    ItemNames.molotov: ItemDetails(366, ItemClassification.filler, 1, False),
    ItemNames.bait_launcher: ItemDetails(369, ItemClassification.filler, 1, False),
    ItemNames.prototype_railgun: ItemDetails(370, ItemClassification.filler, 1, True),
    ItemNames.rc_rocket: ItemDetails(372, ItemClassification.filler, 1, False),
    ItemNames.alpha_bullets: ItemDetails(373, ItemClassification.filler, 1, False),
    ItemNames.omega_bullets: ItemDetails(374, ItemClassification.filler, 1, False),
    ItemNames.easy_reload_bullets: ItemDetails(375, ItemClassification.filler, 1, True),
    ItemNames.brick_breaker: ItemDetails(376, ItemClassification.filler, 1, True),
    ItemNames.excaliber: ItemDetails(377, ItemClassification.filler, 1, False),
    ItemNames.derringer: ItemDetails(378, ItemClassification.filler, 1, True),
    ItemNames.shotgun_full_of_love: ItemDetails(379, ItemClassification.filler, 1, True),
    ItemNames.betrayers_shield: ItemDetails(380, ItemClassification.filler, 1, False),
    ItemNames.triple_crossbow: ItemDetails(381, ItemClassification.filler, 1, True),
    ItemNames.sling: ItemDetails(382, ItemClassification.filler, 1, False),
    ItemNames.flash_ray: ItemDetails(383, ItemClassification.filler, 1, False),
    ItemNames.phoenix: ItemDetails(384, ItemClassification.filler, 1, True),
    ItemNames.hexagun: ItemDetails(385, ItemClassification.filler, 1, True),
    ItemNames.frost_giant: ItemDetails(387, ItemClassification.filler, 1, False),
    ItemNames.cobalt_hammer: ItemDetails(390, ItemClassification.filler, 1, False),
    ItemNames.anvillain: ItemDetails(393, ItemClassification.filler, 1, True),
    ItemNames.mine_cutter: ItemDetails(394, ItemClassification.filler, 1, False),
    ItemNames.staff_of_firepower: ItemDetails(395, ItemClassification.filler, 1, False),
    ItemNames.table_tech_sight: ItemDetails(396, ItemClassification.filler, 1, True),
    ItemNames.table_tech_money: ItemDetails(397, ItemClassification.filler, 1, True),
    ItemNames.table_tech_rocket: ItemDetails(398, ItemClassification.filler, 1, True),
    ItemNames.table_tech_rage: ItemDetails(399, ItemClassification.filler, 1, True),
    ItemNames.table_tech_blanks: ItemDetails(400, ItemClassification.filler, 1, True),
    ItemNames.gungine: ItemDetails(401, ItemClassification.filler, 1, False),
    ItemNames.snowballer: ItemDetails(402, ItemClassification.filler, 1, True),
    ItemNames.melted_rock: ItemDetails(403, ItemClassification.filler, 1, True),
    ItemNames.siren: ItemDetails(404, ItemClassification.filler, 1, True),
    ItemNames.rattler: ItemDetails(406, ItemClassification.filler, 1, False),
    ItemNames.sixth_chamber: ItemDetails(407, ItemClassification.filler, 1, False),
    ItemNames.battery_bullets: ItemDetails(410, ItemClassification.filler, 1, False),
    ItemNames.coolant_leak: ItemDetails(411, ItemClassification.filler, 1, True),
    ItemNames.friendship_cookie: ItemDetails(412, ItemClassification.filler, 1, True),
    ItemNames.heros_sword: ItemDetails(413, ItemClassification.filler, 1, False),
    ItemNames.live_ammo: ItemDetails(414, ItemClassification.filler, 1, True),
    ItemNames.blasphemy: ItemDetails(417, ItemClassification.filler, 1, False),
    ItemNames.heart_holster: ItemDetails(421, ItemClassification.filler, 1, True),
    ItemNames.heart_lunchbox: ItemDetails(422, ItemClassification.filler, 1, False),
    ItemNames.heart_locket: ItemDetails(423, ItemClassification.filler, 1, False),
    ItemNames.heart_bottle: ItemDetails(424, ItemClassification.filler, 1, False),
    ItemNames.heart_purse: ItemDetails(425, ItemClassification.filler, 1, False),
    ItemNames.shotga_cola: ItemDetails(426, ItemClassification.filler, 1, True),
    ItemNames.shotgun_coffee: ItemDetails(427, ItemClassification.filler, 1, True),
    ItemNames.liquid_valkyrie: ItemDetails(431, ItemClassification.filler, 1, True),
    ItemNames.jar_of_bees: ItemDetails(432, ItemClassification.filler, 1, True),
    ItemNames.stuffed_star: ItemDetails(433, ItemClassification.filler, 1, True),
    ItemNames.bullet_idol: ItemDetails(434, ItemClassification.filler, 1, True),
    ItemNames.mustache: ItemDetails(435, ItemClassification.filler, 1, True),
    ItemNames.bloodied_scarf: ItemDetails(436, ItemClassification.filler, 1, False),
    ItemNames.muscle_relaxant: ItemDetails(437, ItemClassification.filler, 1, True),
    ItemNames.explosive_decoy: ItemDetails(438, ItemClassification.filler, 1, True),
    ItemNames.bracket_key: ItemDetails(439, ItemClassification.filler, 1, False),
    ItemNames.ruby_bracelet: ItemDetails(440, ItemClassification.filler, 1, True),
    ItemNames.emerald_bracelet: ItemDetails(441, ItemClassification.filler, 1, False),
    ItemNames.badge: ItemDetails(442, ItemClassification.filler, 1, False),
    ItemNames.big_boy: ItemDetails(443, ItemClassification.filler, 1, False),
    ItemNames.trident: ItemDetails(444, ItemClassification.filler, 1, True),
    ItemNames.the_scrambler: ItemDetails(445, ItemClassification.filler, 1, True),
    ItemNames.shield_of_the_maiden: ItemDetails(447, ItemClassification.filler, 1, False),
    ItemNames.boomerang: ItemDetails(448, ItemClassification.filler, 1, True),
    ItemNames.teleporter_prototype: ItemDetails(449, ItemClassification.filler, 1, False),
    ItemNames.armor_synthesizer: ItemDetails(450, ItemClassification.filler, 1, True),
    ItemNames.pig: ItemDetails(451, ItemClassification.filler, 1, False),
    ItemNames.sponge: ItemDetails(452, ItemClassification.filler, 1, False),
    ItemNames.gas_mask: ItemDetails(453, ItemClassification.filler, 1, True),
    ItemNames.hazmat_suit: ItemDetails(454, ItemClassification.filler, 1, False),
    ItemNames.ring_of_triggers: ItemDetails(456, ItemClassification.filler, 1, True),
    ItemNames.armor_of_thorns: ItemDetails(457, ItemClassification.filler, 1, True),
    ItemNames.ring_of_ethereal_form: ItemDetails(458, ItemClassification.filler, 1, True),
    ItemNames.chaff_grenade: ItemDetails(460, ItemClassification.filler, 1, False),
    ItemNames.blank_companions_ring: ItemDetails(461, ItemClassification.filler, 1, True),
    ItemNames.smoke_bomb: ItemDetails(462, ItemClassification.filler, 1, True),
    ItemNames.ring_of_the_resourceful_rat: ItemDetails(463, ItemClassification.filler, 1, False),
    ItemNames.shellegun: ItemDetails(464, ItemClassification.filler, 1, False),
    ItemNames.table_tech_stun: ItemDetails(465, ItemClassification.filler, 1, True),
    ItemNames.green_guon_stone: ItemDetails(466, ItemClassification.filler, 1, True),
    ItemNames.hidden_compartment: ItemDetails(473, ItemClassification.filler, 1, False),
    ItemNames.abyssal_tentacle: ItemDetails(474, ItemClassification.filler, 1, False),
    ItemNames.quad_laser: ItemDetails(475, ItemClassification.filler, 1, True),
    ItemNames.microtransaction_gun: ItemDetails(476, ItemClassification.filler, 1, False),
    ItemNames.origuni: ItemDetails(477, ItemClassification.filler, 1, False),
    ItemNames.banana: ItemDetails(478, ItemClassification.filler, 1, True),
    ItemNames.super_meat_gun: ItemDetails(479, ItemClassification.filler, 1, True),
    ItemNames.makeshift_cannon: ItemDetails(480, ItemClassification.filler, 1, False),
    ItemNames.camera: ItemDetails(481, ItemClassification.filler, 1, True),
    ItemNames.gunzheng: ItemDetails(482, ItemClassification.filler, 1, False),
    ItemNames.tetrominator: ItemDetails(483, ItemClassification.filler, 1, False),
    ItemNames.devolver: ItemDetails(484, ItemClassification.filler, 1, False),
    ItemNames.orange: ItemDetails(485, ItemClassification.filler, 1, True),
    ItemNames.book_of_chest_anatomy: ItemDetails(487, ItemClassification.filler, 1, False),
    ItemNames.ring_of_chest_vampirism: ItemDetails(488, ItemClassification.filler, 1, True),
    ItemNames.gun_soul: ItemDetails(489, ItemClassification.filler, 1, False),
    ItemNames.brick_of_cash: ItemDetails(490, ItemClassification.filler, 1, True),
    ItemNames.wingman: ItemDetails(491, ItemClassification.filler, 1, False),
    ItemNames.wolf: ItemDetails(492, ItemClassification.filler, 1, False),
    ItemNames.briefcase_of_cash: ItemDetails(493, ItemClassification.filler, 1, False),
    ItemNames.galactic_medal_of_valor: ItemDetails(494, ItemClassification.filler, 1, False),
    ItemNames.unity: ItemDetails(495, ItemClassification.filler, 1, False),
    ItemNames.elder_blank: ItemDetails(499, ItemClassification.filler, 1, True),
    ItemNames.hip_holster: ItemDetails(500, ItemClassification.filler, 1, True),
    ItemNames.bullet: ItemDetails(503, ItemClassification.filler, 1, True),
    ItemNames.hyper_light_blaster: ItemDetails(504, ItemClassification.filler, 1, False),
    ItemNames.really_special_lute: ItemDetails(506, ItemClassification.filler, 1, False),
    ItemNames.starpew: ItemDetails(507, ItemClassification.filler, 1, False),
    ItemNames.dueling_laser: ItemDetails(508, ItemClassification.filler, 1, False),
    ItemNames.jk47: ItemDetails(510, ItemClassification.filler, 1, True),
    ItemNames.third_party_controller: ItemDetails(511, ItemClassification.filler, 1, False),
    ItemNames.shell: ItemDetails(512, ItemClassification.filler, 1, True),
    ItemNames.poxcannon: ItemDetails(513, ItemClassification.filler, 1, True),
    ItemNames.directional_pad: ItemDetails(514, ItemClassification.filler, 1, True),
    ItemNames.mourning_star: ItemDetails(515, ItemClassification.filler, 1, False),
    ItemNames.triple_gun: ItemDetails(516, ItemClassification.filler, 1, False),
    ItemNames.combined_rifle: ItemDetails(519, ItemClassification.filler, 1, False),
    ItemNames.balloon_gun: ItemDetails(520, ItemClassification.filler, 1, True),
    ItemNames.chance_bullets: ItemDetails(521, ItemClassification.filler, 1, False),
    ItemNames.stout_bullets: ItemDetails(523, ItemClassification.filler, 1, False),
    ItemNames.bloody_9mm: ItemDetails(524, ItemClassification.filler, 1, False),
    ItemNames.lament_configurum: ItemDetails(525, ItemClassification.filler, 1, False),
    ItemNames.springheel_boots: ItemDetails(526, ItemClassification.filler, 1, False),
    ItemNames.charming_rounds: ItemDetails(527, ItemClassification.filler, 1, False),
    ItemNames.zombie_bullets: ItemDetails(528, ItemClassification.filler, 1, True),
    ItemNames.battle_standard: ItemDetails(529, ItemClassification.filler, 1, False),
    ItemNames.remote_bullets: ItemDetails(530, ItemClassification.filler, 1, True),
    ItemNames.flak_bullets: ItemDetails(531, ItemClassification.filler, 1, False),
    ItemNames.gilded_bullets: ItemDetails(532, ItemClassification.filler, 1, False),
    ItemNames.magic_bullets: ItemDetails(533, ItemClassification.filler, 1, False),
    ItemNames.relodestone: ItemDetails(536, ItemClassification.filler, 1, True),
    ItemNames.vorpal_gun: ItemDetails(537, ItemClassification.filler, 1, False),
    ItemNames.silver_bullets: ItemDetails(538, ItemClassification.filler, 1, False),
    ItemNames.boxing_glove: ItemDetails(539, ItemClassification.filler, 1, False),
    ItemNames.glass_cannon: ItemDetails(540, ItemClassification.filler, 1, True),
    ItemNames.casey: ItemDetails(541, ItemClassification.filler, 1, False),
    ItemNames.strafe_gun: ItemDetails(542, ItemClassification.filler, 1, False),
    ItemNames.the_predator: ItemDetails(543, ItemClassification.filler, 1, False),
    ItemNames.ac15: ItemDetails(545, ItemClassification.filler, 1, True),
    ItemNames.windgunner: ItemDetails(546, ItemClassification.filler, 1, True),
    ItemNames.knights_gun: ItemDetails(550, ItemClassification.filler, 1, False),
    ItemNames.crown_of_guns: ItemDetails(551, ItemClassification.filler, 1, True),
    ItemNames.bottle: ItemDetails(558, ItemClassification.filler, 1, False),
    ItemNames.the_fat_line: ItemDetails(562, ItemClassification.filler, 1, False),
    ItemNames.the_exotic: ItemDetails(563, ItemClassification.filler, 1, False),
    ItemNames.full_metal_jacket: ItemDetails(564, ItemClassification.filler, 1, True),
    ItemNames.glass_guon_stone: ItemDetails(565, ItemClassification.filler, 1, False),
    ItemNames.rad_gun: ItemDetails(566, ItemClassification.filler, 1, True),
    ItemNames.roll_bomb: ItemDetails(567, ItemClassification.filler, 1, False),
    ItemNames.helix_bullets: ItemDetails(568, ItemClassification.filler, 1, False),
    ItemNames.chaos_bullets: ItemDetails(569, ItemClassification.filler, 1, False),
    ItemNames.yellow_chamber: ItemDetails(570, ItemClassification.filler, 1, False),
    ItemNames.cursed_bullets: ItemDetails(571, ItemClassification.filler, 1, False),
    ItemNames.chicken_flute: ItemDetails(572, ItemClassification.filler, 1, False),
    ItemNames.chest_teleporter: ItemDetails(573, ItemClassification.filler, 1, False),
    ItemNames.robots_left_hand: ItemDetails(576, ItemClassification.filler, 1, False),
    ItemNames.turbo_gun: ItemDetails(577, ItemClassification.filler, 1, True),
    ItemNames.sprun: ItemDetails(578, ItemClassification.filler, 1, False),
    ItemNames.blank_bullets: ItemDetails(579, ItemClassification.filler, 1, False),
    ItemNames.void_core_cannon: ItemDetails(593, ItemClassification.filler, 1, False),
    ItemNames.life_orb: ItemDetails(595, ItemClassification.filler, 1, False),
    ItemNames.teapot: ItemDetails(596, ItemClassification.filler, 1, True),
    ItemNames.mr_accretion_jr: ItemDetails(597, ItemClassification.filler, 1, True),
    ItemNames.stone_dome: ItemDetails(598, ItemClassification.filler, 1, False),
    ItemNames.bubble_blaster: ItemDetails(599, ItemClassification.filler, 1, True),
    ItemNames.spread_ammo: ItemDetails(600, ItemClassification.filler, 1, True),
    ItemNames.big_shotgun: ItemDetails(601, ItemClassification.filler, 1, False),
    ItemNames.gunner: ItemDetails(602, ItemClassification.filler, 1, False),
    ItemNames.slinger: ItemDetails(604, ItemClassification.filler, 1, True),
    ItemNames.loot_bag: ItemDetails(605, ItemClassification.filler, 1, False),
    ItemNames.clown_mask: ItemDetails(607, ItemClassification.filler, 1, False),
    ItemNames.wood_beam: ItemDetails(610, ItemClassification.filler, 1, False),
    ItemNames.drill: ItemDetails(625, ItemClassification.filler, 1, False),
    ItemNames.elimentaler: ItemDetails(626, ItemClassification.filler, 1, False),
    ItemNames.platinum_bullets: ItemDetails(627, ItemClassification.filler, 1, False),
    ItemNames.bumbullets: ItemDetails(630, ItemClassification.filler, 1, False),
    ItemNames.holey_grail: ItemDetails(631, ItemClassification.filler, 1, False),
    ItemNames.turkey: ItemDetails(632, ItemClassification.filler, 1, False),
    ItemNames.table_tech_shotgun: ItemDetails(633, ItemClassification.filler, 1, True),
    ItemNames.crisis_stone: ItemDetails(634, ItemClassification.filler, 1, False),
    ItemNames.snowballets: ItemDetails(636, ItemClassification.filler, 1, False),
    ItemNames.weird_egg: ItemDetails(637, ItemClassification.filler, 1, False),
    ItemNames.devolver_rounds: ItemDetails(638, ItemClassification.filler, 1, False),
    ItemNames.vorpal_bullets: ItemDetails(640, ItemClassification.filler, 1, False),
    ItemNames.gold_junk: ItemDetails(641, ItemClassification.filler, 1, True),
    ItemNames.daruma: ItemDetails(643, ItemClassification.filler, 1, False),
    ItemNames.portable_table_device: ItemDetails(644, ItemClassification.filler, 1, False),
    ItemNames.turtle_problem: ItemDetails(645, ItemClassification.filler, 1, False),
    ItemNames.chamber_gun: ItemDetails(647, ItemClassification.filler, 1, False),
    ItemNames.hungry_bullets: ItemDetails(655, ItemClassification.filler, 1, False),
    ItemNames.kruller_glaive: ItemDetails(656, ItemClassification.filler, 1, False),
    ItemNames.orbital_bullets: ItemDetails(661, ItemClassification.filler, 1, False),
    ItemNames.partially_eaten_cheese: ItemDetails(662, ItemClassification.filler, 1, False),
    ItemNames.resourceful_sack: ItemDetails(663, ItemClassification.filler, 1, False),
    ItemNames.baby_good_mimic: ItemDetails(664, ItemClassification.filler, 1, True),
    ItemNames.macho_brace: ItemDetails(665, ItemClassification.filler, 1, False),
    ItemNames.table_tech_heat: ItemDetails(666, ItemClassification.filler, 1, True),
    ItemNames.rat_boots: ItemDetails(667, ItemClassification.filler, 1, False),
    ItemNames.high_dragunfire: ItemDetails(670, ItemClassification.filler, 1, False),
    ItemNames.gunderfury: ItemDetails(732, ItemClassification.filler, 1, False),
    ItemNames.mimic_gun: ItemDetails(734, ItemClassification.filler, 1, False),
    ItemNames.serpent: ItemDetails(735, ItemClassification.filler, 1, False),
    ItemNames.sunlight_javelin: ItemDetails(748, ItemClassification.filler, 1, False),
    ItemNames.evolver: ItemDetails(755, ItemClassification.filler, 1, False),
    ItemNames.high_kaliber: ItemDetails(761, ItemClassification.filler, 1, True),
    ItemNames.finished_gun: ItemDetails(762, ItemClassification.filler, 1, False),
    ItemNames.magazine_rack: ItemDetails(814, ItemClassification.filler, 1, False),
    ItemNames.lichs_eye_bullets: ItemDetails(815, ItemClassification.filler, 1, False),
    ItemNames.cat_bullet_king_throne: ItemDetails(817, ItemClassification.filler, 1, False),
    ItemNames.baby_good_shelleton: ItemDetails(818, ItemClassification.filler, 1, False),
    ItemNames.shadow_clone: ItemDetails(820, ItemClassification.filler, 1, True),
    ItemNames.scouter: ItemDetails(821, ItemClassification.filler, 1, False),
    ItemNames.katana_bullets: ItemDetails(822, ItemClassification.filler, 1, False),
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
    return GungeonItem(ItemNames.FiveHegemonyCredits, ITEM_NAME_TO_DETAILS[ItemNames.FiveHegemonyCredits].classification, ITEM_NAME_TO_DETAILS[ItemNames.FiveHegemonyCredits].itemID, world.player)

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