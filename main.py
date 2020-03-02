# Import the required module for text
# to speech conversion
from gtts import gTTS
from moviepy.editor import *
import random

# The text that you want to convert to audio
food = ["Angelica", "Savoy cabbage", "Silver linden", "Kiwi", "Allium (Onion)", "Garden onion", "Leek", "Garlic",
        "Chives", "Lemon verbena", "Cashew nut", "Pineapple", "Dill", "Custard apple", "Wild celery", "Peanut",
        "Burdock", "Horseradish", "Tarragon", "Mugwort", "Asparagus", "Oat", "Star fruit", "Brazil nut",
        "Common beet", "Borage", "Chinese mustard", "Swede", "Rape", "Common cabbage", "Cauliflower",
        "Brussel sprouts", "Kohlrabi", "Broccoli", "Chinese cabbage", "Turnip", "Pigeon pea", "Tea", "Capers",
        "Pepper (C. annuum)", "Papaya", "Safflower", "Caraway", "Pecan nut", "Chestnut", "Roman camomile", "Chickpea",
        "Endive", "Chicory", "Chinese cinnamon", "Ceylon cinnamon", "Watermelon", "Lime", "Lemon", "Pummelo",
        "Mandarin orange (Clementine, Tangerine)", "Sweet orange", "Coffee", "Arabica coffee", "Robusta coffee",
        "Coriander", "Common hazelnut", "Saffron", "Muskmelon", "Cucumber", "Cucurbita (Gourd)", "Cumin", "Turmeric",
        "Quince", "Lemon grass", "Globe artichoke", "Wild carrot", "Japanese persimmon", "Cardamom",
        "Black crowberry", "Loquat", "Rocket salad (ssp.)", "Wax apple", "Common buckwheat", "Tartary buckwheat",
        "Fig", "Fennel", "Strawberry", "Black huckleberry", "Soy bean", "Sunflower", "Sea-buckthornberry", "Barley",
        "Hyssop", "Star anise", "Swamp cabbage", "Sweet potato", "Black walnut", "Common walnut", "Lettuce",
        "Grass pea", "Sweet bay", "Lentils", "Garden cress", "Lovage", "Flaxseed", "Mexican oregano", "Lichee",
        "Lupine", "Apple", "Mango", "German camomile", "Lemon balm", "Mentha (Mint)", "Orange mint", "Cornmint",
        "Spearmint", "Peppermint", "Medlar", "Bitter gourd", "Mulberry", "Black mulberry", "Nutmeg", "Sweet basil",
        "Evening primrose", "Olive", "Sweet marjoram", "Pot marjoram", "Common oregano", "Rice", "Millet", "Poppy",
        "Passion fruit", "Parsnip", "Avocado", "Parsley", "Scarlet bean", "Lima bean", "Common bean", "Date",
        "Black chokeberry", "Anise", "Pine nut", "Pepper (Spice)", "Pistachio", "Common pea", "Purslane",
        "Prunus (Cherry, Plum)", "Apricot", "Sweet cherry", "Sour cherry", "European plum", "Almond", "Peach",
        "Guava", "Pomegranate", "Pear", "Radish", "Garden rhubarb", "Blackcurrant", "Redcurrant", "Gooseberry",
        "Watercress", "Rosemary", "Rubus (Blackberry, Raspberry)", "Cloudberry", "Red raspberry", "Black raspberry",
        "Sorrel", "Common sage", "Black elderberry", "Summer savory", "Winter savory", "Rye", "Sesame",
        "Garden tomato", "Cherry tomato", "Garden tomato (var.)", "Eggplant", "Potato", "Rowanberry", "Sorghum",
        "Spinach", "Cloves", "Tamarind", "Dandelion", "Cocoa bean", "Common thyme", "Linden", "Small-leaf linden",
        "Fenugreek", "Common wheat", "Vaccinium (Blueberry, Cranberry, Huckleberry)", "Lowbush blueberry",
        "Sparkleberry", "Highbush blueberry", "American cranberry", "Bilberry", "Lingonberry", "Vanilla",
        "Common verbena", "Broad bean", "Adzuki bean", "Gram bean", "Mung bean", "Climbing bean", "Cowpea",
        "Muscadine grape", "Common grape", "Corn", "Ginger", "Arctic blackberry", "Banana", "Bayberry",
        "Elliott's blueberry", "Canada blueberry", "Bog bilberry", "Buffalo currant", "Celeriac", "Celery stalks",
        "Chinese chives", "European cranberry", "Deerberry", "Ginseng", "Cascade huckleberry",
        "Oval-leaf huckleberry", "Evergreen huckleberry", "Red huckleberry", "Longan",
        "Macadamia nut (M. tetraphylla)", "Garden onion (var.)", "Summer grape", "Fox grape", "Nectarine",
        "Peach (var.)", "Pepper (C. baccatum)", "Pepper (C. chinense)", "Pepper (Capsicum)", "Rambutan", "Red rice",
        "Annual wild rice", "Swiss chard", "Lemon thyme", "Tronchuda cabbage", "Japanese walnut", "Welsh onion",
        "Hard wheat", "Shallot", "Rocket salad", "Carrot", "Triticale", "Black cabbage", "Half-highbush blueberry",
        "Celery leaves", "Chicory leaves", "Komatsuna", "Pak choy", "Napa cabbage", "Chicory roots",
        "Grapefruit/Pummelo hybrid", "Grapefruit", "Jostaberry", "Kai-lan", "Italian oregano", "Oxheart cabbage",
        "Daikon radish", "Black radish", "Radish (var.)", "Red beetroot", "Sweet rowanberry", "Pineappple sage",
        "Skunk currant", "Beer", "Other bread", "Breakfast cereal", "Other soy product", "Other cereal product",
        "Pasta", "Biscuit", "Sourdough", "Spirit", "Fortified wine", "Other alcoholic beverage", "Abalone", "Abiyuch",
        "Acerola", "Acorn", "Winter squash", "Agar", "Red king crab", "Alfalfa", "Allspice", "Amaranth", "Arrowhead",
        "Arrowroot", "Asian pear", "Atlantic herring", "Atlantic mackerel", "Painted comber", "Atlantic pollock",
        "Atlantic wolffish", "Bamboo shoots", "Striped bass", "Beaver", "Beech nut", "Beluga whale", "Bison",
        "Black bear", "Alaska blackfish", "Blue crab", "Blue mussel", "Northern bluefin tuna", "Bluefish",
        "Wild boar", "Bowhead whale", "Breadfruit", "Breadnut tree seed", "Rapini", "Brown bear", "Buffalo", "Burbot",
        "Giant butterbur", "American butterfish", "Butternut", "Butternut squash", "Calabash", "Cardoon", "Caribou",
        "Natal plum", "Carob", "Common carp", "Cassava", "Channel catfish", "Chayote", "Cherimoya", "Chervil", "Chia",
        "Chicken (Cock, Hen, Rooster)", "Chinese broccoli", "Chinese chestnut", "Chinese water chestnut",
        "Garland chrysanthemum", "Cisco", "Nuttall cockle", "Coconut", "Pacific cod", "Atlantic cod",
        "Common octopus", "Corn salad", "Cottonseed", "Catjang pea", "Malus (Crab apple)", "Squashberry",
        "Atlantic croaker", "Cusk", "Cuttlefish", "Mule deer", "Devilfish", "Dock", "Dolphin fish", "Freshwater drum",
        "Mallard duck", "Dungeness crab", "Durian", "Eastern oyster", "Freshwater eel", "Elderberry", "Elk", "Emu",
        "Oregon yampah", "European anchovy", "European chestnut", "Turbot", "Fireweed", "Florida pompano",
        "Ginkgo nuts", "Greylag goose", "Grape", "Greenland halibut/turbot", "Groundcherry", "Grouper", "Guinea hen",
        "Haddock", "Hippoglossus (Common halibut)", "Hazelnut", "Hickory nut", "Horse", "Horseradish tree",
        "Alaska blueberry", "Hyacinth bean", "Irish moss", "Pacific jack mackerel", "Jackfruit", "Japanese chestnut",
        "Java plum", "Jerusalem artichoke", "Jujube", "Jute", "Kale", "Kelp", "King mackerel", "Kumquat",
        "Lambsquarters", "Leather chiton", "Wild leek", "Common ling", "Lingcod", "American lobster", "Loganberry",
        "Lotus", "Sacred lotus", "White lupine", "Malabar spinach", "Mammee apple", "Purple mangosteen",
        "Alpine sweetvetch", "Milkfish", "Monkfish", "Moose", "Moth bean", "Mountain yam", "Striped mullet",
        "Muskrat", "White mustard", "Mustard spinach", "New Zealand spinach", "Nopal", "Ocean pout",
        "North Pacific giant octopus", "Ohelo berry", "Okra", "Tunicate", "Opossum", "Ostrich", "Spotted seal",
        "Pacific herring", "Pacific oyster", "Pacific rockfish", "Velvet duck", "Pepper (C. frutescens)",
        "Common persimmon", "Pheasant", "Northern pike", "Pili nut", "Colorado pinyon", "Pitanga",
        "Plains prickly pear", "French plantain", "American pokeweed", "Polar bear", "Opium poppy", "Prairie turnip",
        "Prickly pear", "Quinoa", "European rabbit", "Raccoon", "Rainbow smelt", "Rainbow trout", "Malabar plum",
        "Rose hip", "Roselle", "Orange roughy", "Sablefish", "Pink salmon", "Chum salmon", "Coho salmon",
        "Sockeye salmon", "Chinook salmon", "Atlantic salmon", "Salmonberry", "Common salsify", "Sapodilla",
        "Mamey sapote", "Spanish mackerel", "Pacific sardine", "Scallop", "Scup", "Sea cucumber", "Steller sea lion",
        "Bearded seal", "Ringed seal", "Seatrout", "Sesbania flower", "American shad", "Shark", "Sheefish",
        "Sheep (Mutton, Lamb)", "Sheepshead", "Hedge mustard", "Skipjack tuna", "Snapper", "Soursop", "Spelt",
        "Spirulina", "Squab", "Squirrel", "Strawberry guava", "Greater sturgeon", "White sucker", "Sugar apple",
        "Pumpkinseed sunfish", "Swordfish", "Taro", "Teff", "Tilefish", "Mexican groundcherry", "Towel gourd",
        "Salmonidae (Salmon, Trout)", "Turkey", "Cattle (Beef, Veal)", "Walleye", "Alaska pollock", "Wasabi",
        "Wax gourd", "Whelk", "Coalfish pollock", "Broad whitefish", "Whitefish", "Whiting", "Wild rice",
        "Tea leaf willow", "Winged bean", "Yam", "Jicama", "Yautia", "Yellowfin tuna", "Yellowtail amberjack",
        "Pollock", "Albacore tuna", "Gadus (Common cod)", "Atlantic halibut", "Pacific halibut", "Pacific salmon",
        "Smelt", "Clupeinae (Herring, Sardine, Sprat)", "Spiny lobster", "Snow crab", "Black-eyed pea", "Deer",
        "Macadamia nut", "Percoidei (Bass and others)", "Perciformes (Perch-like fishes)", "Arctic ground squirrel",
        "Rabbit", "Domestic goat", "Beefalo", "Antelope", "Bivalvia (Clam, Mussel, Oyster)", "Squid", "Shrimp",
        "Crayfish", "Flatfish", "Domestic pig (Piglet, Pork)", "Walrus", "Alaska wild rhubarb", "Oriental wheat",
        "Yardlong bean", "Great horned owl", "Quail", "Boysenberry", "Persian lime", "Feijoa", "Rowal", "Jew's ear",
        "Common mushroom", "Shiitake", "Purple laver", "Wakame", "Enokitake", "Epazote", "Oyster mushroom",
        "Cloud ear fungus", "Maitake", "Ostrich fern", "Spot croaker", "Sourdock", "Tinda", "Atlantic menhaden",
        "Wheat", "Common chokecherry", "Agave", "Narrowleaf cattail", "Jellyfish", "Anchovy", "Blue whiting",
        "Carp bream", "Chanterelle", "Sturgeon", "Charr", "Cinnamon", "Crab", "Common dab", "Spiny dogfish",
        "Anatidae (Duck, Goose, Swan)", "Anguilliformes (Eel)", "True frog", "Garfish", "Gadiformes (Cod, Hake)",
        "Mountain hare", "Lake trout", "Lemon sole", "Clawed lobster", "Lumpsucker",
        "Scombridae (Bonito, Mackerel, Tuna)", "Marine mussel", "Norway haddock", "Norway lobster", "Norway pout",
        "Oil palm", "True oyster", "Sago palm", "Persimmon", "Pikeperch", "Pleuronectidae (Dab, Halibut, Plaice)",
        "Rock ptarmigan", "Pacific ocean perch", "Black salsify", "True seal", "Red algae", "Kombu", "Snail",
        "True sole", "Catfish", "Thistle", "Thunnus (Common tuna)", "Walnut", "Cetacea (Dolphin, Porpoise, Whale)",
        "Columbidae (Dove, Pigeon)", "Conch", "Grape wine", "Berry wine", "Other wine", "Apple cider", "Liquor",
        "Cheese", "Milk (Cow)", "Eggs", "Yogurt", "Bean", "Vodka", "Whisky", "Ice cream", "Gin", "Honey", "Liquorice",
        "Vinegar", "Rum", "Port wine", "Vermouth", "Sherry", "Madeira wine", "Nougat", "Toffee", "Cake", "Pizza",
        "Ymer", "Other snack food", "Crisp bread", "Pastry", "Drag�e", "Chewing gum", "Marzipan", "Salad dressing",
        "Sauce", "Salt", "Butter", "Butter substitute", "Cream", "Sugar", "Sausage", "Meatball", "Mustard", "Pate",
        "Sugar substitute", "Meat bouillon", "Other meat product", "Whey", "Casein", "Fruit preserve",
        "Leavening agent", "Marshmallow", "Gelatin", "Water", "Other fish product", "Milk (Human)", "Other beverage",
        "Baby food", "Dumpling", "Soup", "Other vegetable product", "Unclassified food or beverage", "Syrup",
        "Tallow", "Remoulade", "Chocolate spread", "Fruit gum", "Curry powder", "Other candy", "Meringue", "Lard",
        "Other animal fat", "Other cocoa product", "Cocoa butter", "Cocoa powder", "Cocoa liquor", "Chocolate",
        "Hot chocolate", "Dried milk", "Milk (Other mammals)", "Kefir", "Buttermilk", "Other fermented milk",
        "Soy sauce", "Miso", "Tofu", "Zwieback", "Roe", "Cichlidae (Tilapia)", "Icing", "Snack bar", "Green turtle",
        "Energy drink", "Burrito", "Hamburger", "Baked beans", "Chili", "Taco", "Tortilla", "Nachos",
        "Processed cheese", "Salad", "Cream substitute", "Dulce de leche", "Topping", "Sweet custard", "Egg roll",
        "Heart of palm", "Popcorn", "Potato chip", "Tortilla chip", "Corn chip", "Hibiscus tea", "Stew",
        "Gelatin dessert", "Junket", "Falafel", "Frybread", "Other frozen dessert", "Lasagna", "Morchella (Morel)",
        "Pancake", "Pectin", "Pudding", "Waffle", "Soy milk", "Meatloaf", "Sake", "Cocktail", "Couscous", "Bulgur",
        "Coffee substitute", "Coffee mocha", "Chimichanga", "Semolina", "Tapioca pearl", "Tostada", "Quesadilla",
        "Baked potato", "Hot dog", "Spread", "Enchilada", "Egg substitute", "Nutritional drink", "Other sandwich",
        "Ketchup", "Breakfast sandwich", "Adobo", "Macaroni and cheese", "Butterfat", "Horned melon", "Hushpuppy",
        "Fruit juice", "Relish", "Other fruit product", "Fruit salad", "Soy yogurt", "Vegetarian food",
        "Veggie burger", "Cold cut", "Mixed nuts", "Canola", "Babassu palm", "Cupua�_u", "Shea tree",
        "Oil-seed Camellia", "Ucuhuba", "Phyllo dough", "Cooking oil", "Pie crust", "Pie filling", "Pie",
        "Shortening", "Soy cream", "Ice cream cone", "Molasses", "Cracker", "Nance", "Naranjilla", "Natto", "Ravioli",
        "Scrapple", "Other pasta dish", "Succotash", "Tamale", "Rice cake", "Tree fern", "Evaporated milk", "Flour",
        "Akutaq", "Dough", "Pita bread", "Focaccia", "Bagel", "Other bread product", "Piki bread", "French toast",
        "Wheat bread", "Rye bread", "Oat bread", "Potato bread", "Cornbread", "Corn grits", "Multigrain bread",
        "Rice bread", "Pan dulce", "Raisin bread", "Wonton wrapper", "Trail mix", "Greenthread tea",
        "Fruit-flavor drink", "Vegetable juice", "Horchata", "Soft drink", "Frozen yogurt", "Milkshake",
        "Chocolate mousse", "Dripping", "Pupusa", "Empanada", "Arepa", "Ascidians", "Gefilte fish",
        "Yellow pond-lily", "Fish burger", "Other dish", "Pot pie", "Stuffing", "Edible shell", "Fudge", "Candy bar",
        "Condensed milk", "Margarine", "Margarine-like spread", "Hummus", "Potato puffs", "Potato gratin",
        "Milk substitute", "Pepper (C. pubescens)", "Soft-necked garlic", "Cabbage", "Chinese bayberry", "Mushrooms",
        "Alcoholic beverages", "Onion-family vegetables", "Pomes", "Brassicas", "Cereals and cereal products",
        "Citrus", "Cocoa and cocoa products", "Coffee and coffee products", "Crustaceans", "Milk and milk products",
        "Fats and oils", "Fishes", "Herbs and Spices", "Pulses", "Animal foods", "Mollusks", "Nuts", "Beverages",
        "Fruits", "Green vegetables", "Root vegetables", "Sunburst squash (pattypan squash)", "Green zucchini",
        "Yellow zucchini", "Green bell pepper", "Yellow bell pepper", "Orange bell pepper", "Red bell pepper",
        "Italian sweet red pepper", "Yellow wax bean", "Green bean", "Saskatoon berry", "Nanking cherry",
        "Japanese pumpkin", "White cabbage"]


# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed

foodPicker = random.choice(food)
print(food)

foodAudio = gTTS(text=foodPicker, lang='en', slow=False)

# Saving the converted audio

foodAudio.save("audio/text2speech.mp3")

# importing the audio and getting the audio all mashed up
text2speech = AudioFileClip("audio/text2speech.mp3")
videoclip = VideoFileClip("original_video/original_cut.mp4")
editedAudio = videoclip.audio

# playing the original audio then the text
compiledAudio = CompositeAudioClip([editedAudio.set_duration(3.8), text2speech.set_start(3.8)])

videoclip.audio = compiledAudio

videoclip.write_videofile("edited_video/edited.mp4")
