# Define your word lists
attributes = [
    # Environ
    "desert", "tundra", "mountain", "space", "field", "urban", "jungle", "ocean", "arctic", "savanna", 
    "swamp", "cavern", "volcano", "forest", "meadow", "canyon", "island", "cliff", "valley", "prairie",
    # Stealth and cunning
    "hidden", "covert", "uncanny", "scheming", "decisive", "untouchable", "stalking", "sneaky", "elusive", 
    "shadowy", "silent", "calculating", "crafty", "subtle", "mysterious", "invisible", "guileful", "sly", 
    "undercover", "furtive",
    # Volatility
    "rowdy", "dangerous", "explosive", "threatening", "warring", "deadly", "killer", "insane", "wild", 
    "chaotic", "furious", "volatile", "unpredictable", "destructive", "fiery", "reckless", "menacing", 
    "berserk", "frenzied", "savage",
    # Needs correction
    "bad", "unnecessary", "unknown", "unexpected", "waning", "flawed", "incomplete", "unstable", "faulty", 
    "obsolete", "irrelevant", "outdated", "broken", "unusable", "unreliable", "defective", "unfinished", 
    "unpolished", "unrefined", "unwanted",
    # Organic Gems and materials
    "amber", "bone", "coral", "ivory", "jet", "nacre", "pearl", "obsidian", "glass", "shell", "resin", 
    "silk", "wool", "leather", "fur", "feather", "scale", "horn", "charcoal", "wax",
    # Regular Gems
    "agate", "beryl", "diamond", "opal", "ruby", "onyx", "sapphire", "emerald", "jade", "amethyst", 
    "topaz", "garnet", "quartz", "citrine", "peridot", "zircon", "tourmaline", "spinel", "moonstone", 
    "lapis lazuli",
    # Colors
    "red", "orange", "yellow", "green", "blue", "violet", "indigo", "crimson", "scarlet", "gold", 
    "silver", "bronze", "turquoise", "magenta", "cyan", "maroon", "teal", "lavender", "emerald", "azure",
    # Emotions
    "joyful", "sorrowful", "angry", "fearful", "hopeful", "despairing", "loving", "hating", "calm", 
    "anxious", "excited", "bored", "confused", "amused", "jealous", "proud", "ashamed", "lonely", 
    "content", "furious",
    # Elements
    "fire", "water", "earth", "air", "metal", "wood", "ice", "lightning", "shadow", "light", "void", 
    "plasma", "crystal", "mud", "steam", "lava", "dust", "smoke", "mist", "rainbow",
    # Mythology
    "olympian", "titan", "valkyrie", "phoenix", "sphinx", "basilisk", "chimera", "kraken", "leviathan", 
    "hydra", "banshee", "golem", "centaur", "minotaur", "werewolf", "vampire", "zombie", "ghost", 
    "demon", "angel",
    # Science
    "quantum", "atomic", "nuclear", "molecular", "biological", "chemical", "genetic", "robotic", 
    "cybernetic", "astronomical", "geological", "meteorological", "theoretical", "experimental", 
    "mathematical", "physical", "organic", "inorganic", "synthetic", "analytical",
    # Fantasy
    "enchanted", "cursed", "magical", "mythical", "legendary", "epic", "heroic", "divine", "infernal", 
    "celestial", "ethereal", "mystic", "arcane", "sorcerous", "warlock", "druidic", "shamanic", 
    "necromantic", "alchemical", "runed",
    # Unsorted
    "draconic", "wireless", "spinning", "falling", "orbiting", "hunting", "chasing", "searching", 
    "revealing", "flying", "destroyed", "inconceivable", "tarnished", "radiant", "glowing", "sparking", 
    "whirling", "drifting", "soaring", "crashing"
]

objects = [
    # Large cats
    "panther", "wildcat", "tiger", "lion", "cheetah", "cougar", "leopard", "jaguar", "lynx", "ocelot", 
    "serval", "caracal", "snow leopard", "bobcat", "puma", "margay", "clouded leopard", "sand cat", 
    "black-footed cat", "fishing cat",
    # Snakes
    "viper", "cottonmouth", "python", "boa", "sidewinder", "cobra", "anaconda", "mamba", "taipan", 
    "rattlesnake", "krait", "sea snake", "garter snake", "king cobra", "black mamba", "green anaconda", 
    "horned viper", "coral snake", "grass snake", "adder",
    # Other predators
    "grizzly", "jackal", "falcon", "wolf", "hyena", "eagle", "hawk", "vulture", "shark", "orca", 
    "crocodile", "alligator", "komodo dragon", "polar bear", "wolverine", "osprey", "leopard seal", 
    "barracuda", "piranha", "black widow",
    # Prey
    "wildebeest", "gazelle", "zebra", "elk", "moose", "deer", "stag", "pony", "koala", "sloth", 
    "rabbit", "antelope", "buffalo", "bison", "goat", "sheep", "alpaca", "llama", "reindeer", "impala",
    # HORSES!
    "horse", "stallion", "foal", "colt", "mare", "yearling", "filly", "gelding", "mustang", "clydesdale", 
    "thoroughbred", "arabian", "appaloosa", "palomino", "quarter horse", "pony", "draft horse", 
    "friesian", "andalusian", "shire",
    # Mythical creatures
    "mermaid", "unicorn", "fairy", "troll", "yeti", "pegasus", "griffin", "dragon", "phoenix", "sphinx", 
    "basilisk", "chimera", "kraken", "leviathan", "hydra", "banshee", "golem", "centaur", "minotaur", 
    "werewolf",
    # Occupations
    "nomad", "wizard", "cleric", "pilot", "captain", "commander", "general", "major", "admiral", 
    "chef", "inspector", "merchant", "blacksmith", "alchemist", "sorcerer", "astronaut", "engineer", 
    "architect", "sculptor", "bard",
    # Technology
    "mainframe", "device", "motherboard", "network", "transistor", "packet", "robot", "android", 
    "cyborg", "display", "battery", "memory", "disk", "cartridge", "tape", "camera", "projector", 
    "processor", "sensor", "antenna", "drone", "hologram", "satellite", "microchip", "circuit",
    # Sea life
    "octopus", "lobster", "crab", "barnacle", "hammerhead", "orca", "piranha", "jellyfish", "starfish", 
    "seahorse", "dolphin", "whale", "shark", "squid", "ray", "eel", "clam", "oyster", "urchin", "anemone",
    # Weather
    "storm", "thunder", "lightning", "rain", "hail", "sun", "drought", "snow", "drizzle", "hurricane", 
    "tornado", "cyclone", "blizzard", "monsoon", "typhoon", "frost", "mist", "fog", "dew", "heatwave",
    # Musical
    "piano", "keyboard", "guitar", "trumpet", "trombone", "flute", "cornet", "horn", "tuba", 
    "clarinet", "saxophone", "piccolo", "violin", "harp", "cello", "drum", "organ", "banjo", 
    "rhythm", "beat", "sound", "song", "melody", "harmony", "choir", "symphony", "opera", "ballad", 
    "lullaby",
    # Tools
    "screwdriver", "sander", "lathe", "mill", "welder", "mask", "hammer", "drill", "compressor", 
    "wrench", "mixer", "router", "vacuum", "pliers", "chisel", "saw", "anvil", "forge", "vise", 
    "level", "tape measure",
    # Other
    "warning", "presence", "weapon", "player", "ink", "case", "cup", "chain", "door", "mirror", 
    "clock", "book", "scroll", "map", "key", "lock", "shield", "sword", "arrow", "bow",
    # Fantasy objects
    "artifact", "relic", "tome", "grimoire", "cipher", "beacon", "lantern", "forge", "anvil", "crucible", 
    "pendulum", "hourglass", "monolith", "obelisk", "altar", "portal", "gate", "rune", "sigil", "totem",
    # Science objects
    "particle", "atom", "molecule", "cell", "organism", "planet", "star", "galaxy", "nebula", "quasar", 
    "black hole", "wormhole", "dimension", "experiment", "laboratory", "observatory", "telescope", 
    "microscope", "spectrometer", "accelerator"
]