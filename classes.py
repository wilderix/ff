from pprint import pprint


# TODO:
# Add "expansion" as an attribute on all cards


def get_list_item_by_name(item_list, name):
    output = None
    for item in item_list:
        if item.name.lower() == name.lower():
            output = item
    return output


def pprint_attributes(object):

    print(f"{'*'*5} {object.name} {'*'*5}")

    attributes = {}
    for outer_key, outer_val in object.__dict__.items():
        if isinstance(outer_val, dict):
            new_outer_val = {}
            for inner_key, inner_val in outer_val.items():
                if inner_val is None:
                    new_inner_val = 'Empty'
                elif isinstance(inner_val, str):
                    new_inner_val = inner_val
                elif isinstance(inner_val, int):
                    new_inner_val = inner_val
                else:
                    new_inner_val = inner_val.name
                new_outer_val[inner_key] = new_inner_val
            val = new_outer_val
        elif isinstance(outer_val, list):
            new_outer_val = []
            for inner_val in outer_val:
                if isinstance(inner_val, str):
                    new_inner_val = inner_val
                elif isinstance(inner_val, int):
                    new_inner_val = inner_val
                else:
                    new_inner_val = inner_val.name
                new_outer_val.append(new_inner_val)
        else:
            val = outer_val
        attributes[outer_key] = val

    pprint(attributes)
    print()


def get_ship_color(name):
    ship_colors = {
        'serenity': 'orange',
        'bonnie mae': 'blue',
        'yang xi': 'yellow',
        'bonanza': 'green',
        'artful dodger': 'teal'
    }
    color = ship_colors.get(name)
    return color



class Deck:
    def __init__(self, **kwargs):
        defaults = {
            'name': None,
            'expansion': 'base',
            'type': None,
            'deck': None
        }
        self.__dict__ = defaults
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in defaults)

        # Initialize lists
        if self.deck is None:
            self.deck = []
        self.discard = []


    ### functions

    # Shuffle

    # Prime the pump
    def prime_the_pump(self):
        if self.type.lower() in ('supply', 'contact'):
            pass
        else:
            pass
    
    # Peek at discard
    # need a way to show name and summarize the 

    # Consider (Pull x from discard and x from deck)

    # Take 1 or 2 cards

    # Return card to discard


class Item:
    def __init__(self, **kwargs):
        defaults = {
            'name': None,
            'expansion': 'base',
            'cost': 0,
            'fight': 0,
            'tech': 0,
            'talk': 0,
            'planet_deck': 'base',
            'type': 'equipment',
            'keywords': None,
            'full_burn_range': 5,
            'full_burn_cost': 1,
            'mosy_range': 1,
            'reroll_requires_discard': False,
            'reroll_on': None,
            'reroll_condition': None
        }
        self.__dict__ = defaults
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in defaults)

    def attributes(self):
        pprint_attributes(self)



class Ship:
    def __init__(self, **kwargs):

        defaults = {
            # Size Limits
            'crew_size': 6,
            'jobs_hand_size': 3,
            'jobs_active_size': 3,
            'hold_storage_size': 8,
            'hold_stash_size': 4,
            'upgrade_slots':4,
            # Basic Attributes
            'name': None,
            'setup': 'basic',
            'engine': None,
            'expansion': 'base'
        }
        self.__dict__ = defaults
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in defaults)

        # Populate derived items
        self.color = get_ship_color(self.name.lower())

        # Initialize containers based on size caps
        self.crew = {c+1: None for c in range(self.crew_size)}
        self.hold_storage = {s+1: None for s in range(self.hold_storage_size)}
        self.hold_stash = {s+1: None for s in range(self.hold_stash_size)}
        self.jobs_hand = {h+1: None for h in range(self.jobs_hand_size)}
        self.jobs_active = {j+1: None for j in range(self.jobs_active_size)}
        self.upgrades = {u+1: None for u in range(self.upgrade_slots)}

        # Initialize empty attributes
        self.jobs_completed = []
        self.solid_with = []
        self.location = None

        # Populate engine based on ship name
        self.upgrades[1] = self.engine
        self.full_burn_range = self.engine.full_burn_range
        self.mosy_range = self.engine.mosy_range

        # Setup
        if self.setup == 'basic':
            # Load up on fuel and parts
            for i in range(1, 5):
                if i == 1:
                    item = 'parts/parts'
                else:
                    item = 'fuel/fuel'
                self.hold_storage[i] = item
            # Get starting credits
            self.credits = 3000
        

    def attributes(self):
        pprint_attributes(self)


    def dict(self):
        print(self.__dict__)


    def get_names(self, container_name):
        
        if container_name == 'crew':
            container = self.crew
        elif container_name == 'upgrades':
            container = self.upgrades
        elif container_name == 'jobs_hand':
            container = self.jobs_hand
        elif container_name == 'jobs_active':
            container = self.jobs_active
        elif container_name == 'jobs_completed':
            container = self.jobs_completed
        elif container_name == 'hold_storage':
            container = self.hold_storage
        elif container_name == 'hold_stash':
            container = self.hold_stash
        else:
            container = None

        if isinstance(container, dict):
            output = {k: v.name for k, v in container.items() if v is not None}
        elif isinstance(container, list):
            output = [c.name for c in container]
        else:
            output = f"{container_name} is not a valid container"

        pprint(output)


    def kill(self):
        print(f"This is where we would kill {self.name}")
        pass
        # Pick a crew member
        # If no crew, disgruntle the captain
        # Do medic check
        # 


class Person:
    def __init__(self, **kwargs):

        defaults = {
            'name': None,
            'expansion': 'base',
            'base_fight': 0,
            'base_tech': 0,
            'base_talk': 0,
            'professions': None,
            'keywords': None,
            'home_planet': None,
            'is_captain': False,
            'is_moral': False,
            'is_lawful': False,
            'is_wanted': False,
            'equipment_max': 1,
            'is_alive': True,
            'bonus_name': None,
            'bonus_text': None,
            'bonus_type': None,
            'bonus_amount': 0,
            'pay_to_hire': None,
            'reroll_on': None,
            'reroll_condition': None,
            'special_rule': None,
        }

        self.__dict__ = defaults
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in defaults)
        
        # Populate the empty lists
        if self.professions is None:
            self.professions = []
        if self.keywords is None:
            self.keywords = []
        
        # Populate size-basd dictionaries
        self.equipment = {e+1: None for e in range(self.equipment_max)}






    def print_stats(self):
        stats = f"{self.name} has the following stats\nFight: {self.base_fight}\nTech: {self.base_tech}\nNegotiate: {self.base_talk}"
        print(stats)

    def attributes(self):
        pprint_attributes(self)


class Captain(Person):
    def __init__(
        self,
        *args,
        is_captain=True,
        home_planet=None,
        pay_to_hire=True,
        **kwargs
    ):
        super().__init__(
            *args,
            is_captain=is_captain,
            home_planet=home_planet,
            pay_to_hire=pay_to_hire,
            **kwargs
        )
