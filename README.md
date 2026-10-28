# Enter the Gungeon AP World


> [!NOTE] 
> This is mod that incorporates Enter the Gungeon into the Archipelago multi-game randomizer. You can read more about Archipelago from the [Archipelago repo](https://github.com/ArchipelagoMW/Archipelago).


## What is this?
This AP World is needed for seed and template generation. 

To play the EtG Archipelago, your copy of *Enter the Gungeon* will require the [companion mod](https://github.com/NoahSims/GungeonArchipelagoPlugin).

## Gameplay of EtG Archipelago

### What does randomization do in this game?
- ~~Any action~~ *Most actions* that would normally unlock an entry in the [Ammonomicon](https://enterthegungeon.wiki.gg/wiki/Ammonomicon) will instead send a multiworld item.
- Important in-game progression will now need to be unlocked by multiworld items. These include:
	- Playable characters
	- The 4 parts of the *Bullet That Can Kill The Past*
	- Access to NPC shops
	- Ability to access secret floors
	- Access to in-game guns/items (Ammonomicon entries)


### What is the goal of EtG in Archipelago?
The current goal condition is to *kill the past* of any playable gungeoneer. 

In the future we plan to support alternate goal conditions such as:
- Kill the Lich
- Kill the Gunslinger's past
- Kill every boss


# Setup

### Creating a `.yaml` file
To play an Archipelago game, you will need a `.yaml` file for the game you would like to play.

1. Download and install [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases).
2. Download `enter_the_gungeon.apworld` from the mod's releases page and install it, either by double clicking the `.apworld` file, opening the Archipelago Launcher and selecting "Install APWorld", or by selecting "Browse Files" and adding it to the `custom_worlds` folder.
3. To create a `.yaml` file, open the Archipelago Launcher and search for "Options Creator". You can then customize all of the options for Enter the Gungeon, and then save the `.yaml` file.
    - Alternatively, if you would prefer to manually edit the `.yaml` file in a text editor, you can click "Generate Template Options" in the Archipelago Launcher instead.

### Generating a multiworld
When you have collected all `.yaml` files for each player in the multiworld, move them all into the `Players` folder. You can easily find the Players folder by opening the Archipelago Launcher and clicking "Browse Files".

Note that only one player in the multiworld will need to generate. If the player who is hosting is not yourself, they will also need to install the apworld for Enter the Gungeon.

Once all `.yaml` files are ready, click "Generate" in the launcher. A command prompt window will open, and if successful it will close itself. Your generated multiworld will appear in the `output` folder.

You can host the game by [uploading](https://archipelago.gg/uploads) it to the Archipelago website and clicking Create New Room. The address you will need to connect to the server will be displayed at the top of the room page.
- You can also host the game yourself by clicking "Host" in the launcher. You will need to know how to port forward if you want other players to be able to connect to a manually hosted server.

### Connecting to a server
A walkthrough for connecting from the in-game client can be found in the [companion mod's repo](https://github.com/NoahSims/GungeonArchipelagoPlugin).


> [!NOTE]
> The setup section formatting/wording is shamelessly borrowed from the exceptionally detailed [ULTRAKILL apworld](https://github.com/TRPG0/ArchipelagoULTRAKILL).

