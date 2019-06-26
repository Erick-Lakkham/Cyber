from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

ip = input ("\nWhat\'s your IP? ")

mc = Minecraft.create(ip, 4711)
x, y, z = mc.player.getPos()

opt = input ("\nEnter an option\n\n[p] - Post to chat.\n[f] - Places flowers around the player every \"t\" seconds.\n[s] - Makes a sandstone structure around the player.\n[demo] - Does some stuff.\n\n")

if opt == "p":
	
	out = input ("\nWhat do you want to post to the chat?\n\n")
	mc.postToChat (out)
	
elif opt == "f":
	
	out = int (input ("\nWhat do you want to set the value of \"t\" to? (must be type int)\n"))
	
	while True:
		
		mc.setBlock (x, y, z, 37)
		mc.setBlock (x, y+1, z, 37)
		sleep (out)
		x, y, z = mc.player.getPos()
		
elif opt == "s":
	
	mc.setBlocks (x-5, y, z-5, x+5, y+3, z+5, 0)
	mc.setBlocks (x-5, y-1, z-5, x+5, y-1, z+5, 24)
	mc.setBlocks (x-5, y+3, z-5, x+5, y+3, z+5, 24)
	mc.setBlocks (x-5, y-1, z-5, x+5, y+3, z-5, 24)
	mc.setBlocks (x-5, y-1, z+5, x+5, y+3, z+5, 24)
	mc.setBlocks (x-5, y-1, z-5, x-5, y+3, z+5, 24)
	mc.setBlocks (x+6, y-1, z-5, x+6, y+3, z+3, 24)
	
elif opt == "demo":
	
	i = 1000
	while i > 0:
		
		mc.postToChat ("I like to play Mnecraft!")
		i = i - 1
	
	mc.setBlocks (x-5, y, z-5, x+5, y+3, z+5, 0)
	mc.setBlocks (x-5, y-1, z-5, x+5, y-1, z+5, 24)
	mc.setBlocks (x-5, y+3, z-5, x+5, y+3, z+5, 24)
	mc.setBlocks (x-5, y-1, z-5, x+5, y+3, z-5, 24)
	mc.setBlocks (x-5, y-1, z+5, x+5, y+3, z+5, 24)
	mc.setBlocks (x-5, y-1, z-5, x-5, y+3, z+5, 24)
	mc.setBlocks (x+6, y-1, z-5, x+6, y+3, z+3, 24)
	
	mc.setBlock (x, y, z+1, 46, 1)
	mc.setBlock (x, y, z-1, 46, 1)
	mc.setBlock (x-1, y, z, 46, 1)
	mc.setBlock (x+1, y, z, 46, 1)
	
	j = 10
	while True:
		
		mc.setBlock (x, y+1, z, 37)
		mc.setBlock (x, y, z, 37)
		
		if j > 0:
			
			mc.player.setPos (x, y+3, z)
			j = j-1
		
		sleep (0.5)
		x, y, z = mc.player.getPos()
	
else:
	print ("\n\"" + opt + "\" is not an option.")

"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""


