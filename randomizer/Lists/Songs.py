"""Data of the song breakdowns in ROM."""
from randomizer.Enums.SongGroups import SongGroup
from randomizer.Enums.SongType import SongType


class Song:
    """Class used for managing song objects."""

    def __init__(self, name, type=SongType.System, memory=None, groups=[]):
        """Init SONG objects.

        Args:
            name (str): Name of the song.
            type (enum, optional): Songtype enum of the item. Defaults to SongType.System.
        """
        self.name = name
        self.output_name = name
        self.type = type
        self.memory = memory
        self.default_memory = memory
        self.channel = (memory >> 3) & 0xF
        self.groups = groups.copy()

    def Reset(self):
        """Reset song object so that output_name is reset between generations."""
        self.output_name = self.name
        self.memory = self.default_memory

class SongExclusionItem:
    """Song Exclusion multiselector information."""

    def __init__(self, name, shift, tooltip=""):
        """Initialize with given data."""
        self.name = name
        self.shift = shift
        self.tooltip = tooltip


song_data = [
    Song("Silence", type=SongType.System, memory=0x00),
    Song("Jungle Japes (Starting Area)", type=SongType.BGM, memory=0x101),
    Song("Cranky's Lab", type=SongType.BGM, memory=0x100),
    Song("Jungle Japes (Minecart)", type=SongType.BGM, memory=0x188),
    Song("Jungle Japes (Army Dillo)", type=SongType.BGM, memory=0x189),
    Song("Jungle Japes (Caves/Underground)", type=SongType.BGM, memory=0x100),
    Song("Funky's Hut", type=SongType.BGM, memory=0x100),
    Song("Unused Coin Pickup", type=SongType.Protected, memory=0x440),
    Song("Bonus Minigames", type=SongType.BGM, memory=0x189),
    Song("Triangle Trample", type=SongType.Event, memory=0x8C2),
    Song("Guitar Gazump", type=SongType.Event, memory=0x8C2),
    Song("Bongo Blast", type=SongType.Event, memory=0x8C2),
    Song("Trombone Tremor", type=SongType.Event, memory=0x8C2),
    Song("Saxaphone Slam", type=SongType.Event, memory=0x8C2),
    Song("Angry Aztec", type=SongType.BGM, memory=0x100),
    Song("Transformation", type=SongType.Event, memory=0xA34),
    Song("Mini Monkey", type=SongType.BGM, memory=0x19A),
    Song("Hunky Chunky", type=SongType.BGM, memory=0x19A),
    Song("GB/Key Get", type=SongType.MajorItem, memory=0x8C4),
    Song("Angry Aztec (Beetle Slide)", type=SongType.BGM, memory=0x109),
    Song("Oh Banana", type=SongType.MajorItem, memory=0xABD),
    Song("Angry Aztec (Temple)", type=SongType.BGM, memory=0x101),
    Song("Company Coin Get", type=SongType.MajorItem, memory=0x637),
    Song("Banana Coin Get", type=SongType.MinorItem, memory=0x637),
    Song("Going through Vulture Ring", type=SongType.Event, memory=0x647),
    Song("Angry Aztec (Dogadon)", type=SongType.BGM, memory=0x100),
    Song("Angry Aztec (5DT)", type=SongType.BGM, memory=0x100),
    Song("Frantic Factory (Car Race)", type=SongType.BGM, memory=0x188),
    Song("Frantic Factory", type=SongType.BGM, memory=0x100),
    Song("Snide's HQ", type=SongType.BGM, memory=0x100),
    Song("Jungle Japes (Tunnels)", type=SongType.BGM, memory=0x18A),
    Song("Candy's Music Shop", type=SongType.BGM, memory=0x100),
    Song("Minecart Coin Get", type=SongType.MinorItem, memory=0x63F),
    Song("Melon Slice Get", type=SongType.MinorItem, memory=0x63F),
    Song("Pause Menu", type=SongType.BGM, memory=0x1D4),
    Song("Crystal Coconut Get", type=SongType.MinorItem, memory=0x63F),
    Song("Rambi", type=SongType.BGM, memory=0x198),
    Song("Angry Aztec (Tunnels)", type=SongType.BGM, memory=0x192),
    Song("Water Droplets", type=SongType.Ambient, memory=0x914),
    Song("Frantic Factory (Mad Jack)", type=SongType.BGM, memory=0x100),
    Song("Success", type=SongType.Event, memory=0x8CD),
    Song("Start (To pause game)", type=SongType.Protected, memory=0x85E),
    Song("Failure", type=SongType.Event, memory=0x89D),
    Song("DK Transition (Opening)", type=SongType.System, memory=0x854),
    Song("DK Transition (Closing)", type=SongType.System, memory=0x854),
    Song("Unused High-Pitched Japes", type=SongType.Protected, memory=0x444),
    Song("Fairy Tick", type=SongType.MinorItem, memory=0x8C5),
    Song("Melon Slice Drop", type=SongType.MinorItem, memory=0x635),
    Song("Angry Aztec (Chunky Klaptraps)", type=SongType.BGM, memory=0x188),
    Song("Frantic Factory (Crusher Room)", type=SongType.BGM, memory=0x100),
    Song("Jungle Japes (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("Frantic Factory (R&D)", type=SongType.BGM, memory=0x18A),
    Song("Frantic Factory (Production Room)", type=SongType.BGM, memory=0x18A),
    Song("Troff 'n' Scoff", type=SongType.BGM, memory=0x100),
    Song("Boss Defeat", type=SongType.Event, memory=0x89A),
    Song("Angry Aztec (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (Outside)", type=SongType.BGM, memory=0x101),
    Song("Boss Unlock", type=SongType.Event, memory=0x98),
    Song("Awaiting Entering the Boss", type=SongType.BGM, memory=0x190),
    Song("Generic Twinkly Sounds", type=SongType.Ambient, memory=0x934),
    Song("Gloomy Galleon (Pufftoss)", type=SongType.BGM, memory=0x108),
    Song("Gloomy Galleon (Seal Race)", type=SongType.BGM, memory=0x188),
    Song("Gloomy Galleon (Tunnels)", type=SongType.BGM, memory=0x18B),
    Song("Gloomy Galleon (Lighthouse)", type=SongType.BGM, memory=0x100),
    Song("Battle Arena", type=SongType.BGM, memory=0x100),
    Song("Drop Coins (Minecart)", type=SongType.MinorItem, memory=0x445),
    Song("Fairy Nearby", type=SongType.Ambient, memory=0x925),
    Song("Checkpoint", type=SongType.MinorItem, memory=0x447),
    Song("Fungi Forest (Day)", type=SongType.BGM, memory=0x101),
    Song("Blueprint Get", type=SongType.MajorItem, memory=0x4C5),
    Song("Fungi Forest (Night)", type=SongType.BGM, memory=0x188),
    Song("Strong Kong", type=SongType.BGM, memory=0x19A),
    Song("Rocketbarrel Boost", type=SongType.BGM, memory=0x192),
    Song("Orangstand Sprint", type=SongType.BGM, memory=0x190),
    Song("Fungi Forest (Minecart)", type=SongType.BGM, memory=0x100),
    Song("DK Rap", type=SongType.BGM, memory=0x900),
    Song("Blueprint Drop", type=SongType.MajorItem, memory=0x63D),
    Song("Gloomy Galleon (2DS)", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (5DS/Submarine)", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (Pearls Chest)", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (Mermaid Palace)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Dogadon)", type=SongType.BGM, memory=0x188),
    Song("Mad Maze Maul", type=SongType.BGM, memory=0x188),
    Song("Crystal Caves", type=SongType.BGM, memory=0x101),
    Song("Crystal Caves (Giant Kosha Tantrum)", type=SongType.BGM, memory=0x193),
    Song("Nintendo Logo (Old?)", type=SongType.System, memory=0x102),
    Song("Success (Races)", type=SongType.Event, memory=0x118),
    Song("Failure (Races & Try Again)", type=SongType.Event, memory=0x118),
    Song("Bonus Barrel Introduction", type=SongType.Protected, memory=0x100),
    Song("Stealthy Snoop", type=SongType.BGM, memory=0x188),
    Song("Minecart Mayhem", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (Mechanical Fish)", type=SongType.BGM, memory=0x101),
    Song("Gloomy Galleon (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Anthill)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Barn)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Mill)", type=SongType.BGM, memory=0x100),
    Song("Generic Seaside Sounds", type=SongType.Ambient, memory=0x912),
    Song("Fungi Forest (Spider)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Mushroom Top Rooms)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Giant Mushroom)", type=SongType.BGM, memory=0x100),
    Song("Boss Introduction", type=SongType.BGM, memory=0x100),
    Song("Tag Barrel (All of them)", type=SongType.Protected, memory=0x1CA),
    Song("Crystal Caves (Beetle Race)", type=SongType.BGM, memory=0x108),
    Song("Crystal Caves (Igloos)", type=SongType.BGM, memory=0x100),
    Song("Mini Boss", type=SongType.BGM, memory=0x1AA),
    Song("Creepy Castle", type=SongType.BGM, memory=0x101),
    Song("Creepy Castle (Minecart)", type=SongType.BGM, memory=0x100),
    Song("Baboon Balloon", type=SongType.Event, memory=0x19A),
    Song("Gorilla Gone", type=SongType.BGM, memory=0x190),
    Song("DK Isles", type=SongType.BGM, memory=0x101),
    Song("DK Isles (K Rool's Ship)", type=SongType.BGM, memory=0x109),
    Song("DK Isles (Banana Fairy Island)", type=SongType.BGM, memory=0x101),
    Song("DK Isles (K-Lumsy's Prison)", type=SongType.BGM, memory=0x101),
    Song("Hideout Helm (Blast-O-Matic On)", type=SongType.BGM, memory=0x100),
    Song("Move Get", type=SongType.MajorItem, memory=0x892),
    Song("Gun Get", type=SongType.MajorItem, memory=0x892),
    Song("Hideout Helm (Blast-O-Matic Off)", type=SongType.BGM, memory=0x100),
    Song("Hideout Helm (Bonus Barrels)", type=SongType.BGM, memory=0x188),
    Song("Crystal Caves (Cabins)", type=SongType.BGM, memory=0x100),
    Song("Crystal Caves (Rotating Room)", type=SongType.BGM, memory=0x100),
    Song("Crystal Caves (Tile Flipping)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Tunnels)", type=SongType.BGM, memory=0x100),
    Song("Intro Story Medley", type=SongType.BGM, memory=0x100),
    Song("Training Grounds", type=SongType.BGM, memory=0x101),
    Song("Enguarde", type=SongType.BGM, memory=0x198),
    Song("K-Lumsy Celebration", type=SongType.BGM, memory=0x110),
    Song("Creepy Castle (Crypt)", type=SongType.BGM, memory=0x100),
    Song("Headphones Get", type=SongType.MajorItem, memory=0x4BC),
    Song("Pearl Get", type=SongType.MajorItem, memory=0x43E),
    Song("Creepy Castle (Dungeon w/ Chains)", type=SongType.BGM, memory=0x100),
    Song("Angry Aztec (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Jungle Japes (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Frantic Factory (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Gloomy Galleon (Lobby)", type=SongType.BGM, memory=0x101),
    Song("Main Menu", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Inner Crypts)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Ballroom)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Greenhouse)", type=SongType.BGM, memory=0x100),
    Song("K Rool's Theme", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Winch)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Wind Tower)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Tree)", type=SongType.BGM, memory=0x101),
    Song("Creepy Castle (Museum)", type=SongType.BGM, memory=0x100),
    Song("BBlast Final Star", type=SongType.Event, memory=0x445),
    Song("Drop Rainbow Coin", type=SongType.MajorItem, memory=0x647),
    Song("Rainbow Coin Get", type=SongType.MajorItem, memory=0x647),
    Song("Normal Star", type=SongType.MinorItem, memory=0x645),
    Song("Bean Get", type=SongType.MajorItem, memory=0x645),
    Song("Crystal Caves (Army Dillo)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Kut Out)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Dungeon w/out Chains)", type=SongType.BGM, memory=0x100),
    Song("Banana Medal Get", type=SongType.MajorItem, memory=0x645),
    Song("K Rool's Battle", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Crystal Caves (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Hideout Helm (Lobby)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Trash Can)", type=SongType.BGM, memory=0x100),
    Song("End Sequence", type=SongType.BGM, memory=0x100),
    Song("K-Lumsy Ending", type=SongType.BGM, memory=0x100),
    Song("Jungle Japes", type=SongType.BGM, memory=0x101),
    Song("Jungle Japes (Cranky's Area)", type=SongType.BGM, memory=0x100),
    Song("K Rool Takeoff", type=SongType.BGM, memory=0x100),
    Song("Crystal Caves (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("Creepy Castle (Baboon Blast)", type=SongType.BGM, memory=0x100),
    Song("DK Isles (Snide's Room)", type=SongType.BGM, memory=0x100),
    Song("K Rool's Entrance", type=SongType.BGM, memory=0x100),
    Song("Monkey Smash", type=SongType.BGM, memory=0x100),
    Song("Fungi Forest (Rabbit Race)", type=SongType.BGM, memory=0x188),
    Song("Game Over", type=SongType.Protected, memory=0x1D8),
    Song("Wrinkly Kong", type=SongType.BGM, memory=0x18A),
    Song("100th CB Get", type=SongType.Event, memory=0x645),
    Song("K Rool's Defeat", type=SongType.Protected, memory=0x18),
    Song("Nintendo Logo", type=SongType.BGM, memory=0x108),
]

ExcludedSongsSelector = []
# If you make changes to this list, make sure to change the corresponding
# MiscChangesSelected enum in randomizer.Enums.Settings.
ExclSongsItems = [
    SongExclusionItem("Wrinkly", 0, "Removes Wrinkly doors from playing her theme."),
    SongExclusionItem("Transformation", 3, "The game will no longer play the transformation sound effect."),
    SongExclusionItem("Pause Music", 4, "The pause menu music will no longer play."),
    SongExclusionItem("Sub Areas", 5, "Sub-Areas will no longer play their song, meaning that there's 1 piece of music for the entire level."),
    # SongExclusionItem("Shops", 1, "COMING SOON: Makes shops inherit the previous song."), # TODO: Fix this
    # SongExclusionItem("Events", 2, "COMING SOON: Events will no longer play a song."), # TODO: Fix this

]
for item in ExclSongsItems:
    if item.name != "No Group":
        ExcludedSongsSelector.append({"name": item.name, "value": item.name.lower().replace(" ", "_"), "tooltip": item.tooltip, "shift": item.shift})
