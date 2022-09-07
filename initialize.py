from classes import Deck, Item, Ship, Person, Captain, get_list_item_by_name


captains = [
    Captain(
        name='Malcolm',
        base_fight=2,
        base_talk=1,
        professions=['pilot', 'soldier'],
        is_moral=True,
        bonus_name='Brown Coat',
        bonus_text="When you complete a Crime Job, take $500.",
        bonus_type='crime',
        bonus_amount=500
        # bonus_2_name="Big Damn Heroes",
        # bonus_2_text="When you proceed while misbehaving, take $100.",
        # bonus_2_type='misbehave',
        # bonus_2_amount=100
    ),
    Captain(
        name='Atherton',
        base_fight=1,
        base_talk=2,
        green_word=['FANCY DUDS', 'FAKE IDS'],
        bonus_name='Black Mark',
        bonus_text="May not hire crew with the Companion profession",
        expansion='Blue Sun'
    ),
    Captain(
        name='Burgess',
        base_fight=1,
        base_tech=1,
        base_talk=1,
        keywords=['FANCY DUDS'],
        bonus_name="Taker",
        bonus_text="When you complete a shipping job, load 1 cargo."
    ),
    Captain(
        name='Corbin',
        professions=['mechanic'],
        base_tech=2,
        base_talk=1,
        bonus_name='Chop Shop',
        bonus_text="You may buy Drive Cores and Ship Upgrades at half price."
    ),
    Captain(
        name='Jubal Early',
        professions=['pilot'],
        base_fight=1,
        base_tech=1,
        base_talk=1,
        equipment_max=2,
        bonus_name='Bounty Hunter',
        bonus_text="+2 fight when attacking in showdown. May carry 2 gear."
    ),
    Captain(
        name='Marco',
        base_fight=2,
        base_tech=1,
        bonus_name='Gun Runner',
        bonus_text='You may buy gear with the "Explosives" or "Firearm" professions at half price.',
        keywords=['TRANSPORT']
    ),
    Captain(
        name='Monty',
        base_fight=2,
        base_tech=1,
        is_moral=True,
        professions=['mechanic', 'soldier'],
        bonus_name="Smuggler Extraordinaire",
        bonus_text="When you complete a Smuggling Job, take $500",
        bonus_type='smuggling',
        bonus_amount=500
    ),
    Captain(
        name='Murphy',
        base_tech=2,
        base_fight=1,
        is_moral=1,
        professions=['medic', 'mechanic'],
        bonus_name='Trade Baron',
        bonus_text="Whenever you sell cargo or contraband to a contact, take an extra $100 each.",
        expansion="Blue Sun"
    ),
    Captain(
        name='Nandy',
        base_talk=2,
        base_fight=1,
        is_moral=1,
        professions=['companion'],
        bonus_name='Heart of Gold',
        bonus_text="May hire crew at no cost."
    ),
    Captain(
        name='Sash',
        base_talk=2,
        base_tech=1,
        keywords=['HACKING RIG'],
        bonus_name='Pirate',
        bonus_text="When you complete a Piracy Job, steal $500 from the targeted rival.",
        expansion='Pirates and Bounty Hunters'
    ),
    Captain(
        name="Wright",
        professions=['grifter'],
        base_fight=1,
        base_tech=1,
        base_talk=1,
        bonus_name="Dirty Slaver",
        bonus_text="Whenever you deliver fugitives, you may take an extra $100 per fugitive. This counts as immoral.",
        expansion='Kalidasa'
    ),
    Captain(
        name="Womack",
        professions=['soldier'],
        base_fight=2,
        base_talk=1,
        bonus_name='Cold and Heartless',
        bonus_text='When you complete an immoral job, take $500.'
    ),
]

engines = [
    Item(
        name='Radeon Accelerator Mark I'
    ),
    Item(
        name='Radeon 6',
        full_burn_range=6
    ),
    Item(
        name='Echelon LR-8',
        full_burn_range=8,
        full_burn_cost=0,
        special='Unique Core: May not be replaced. May only be used on Interceptor.'
    ),
    Item(
        name='Tri-Capissen 28HD',
        full_burn_range=4,
        special='Unique Core: May not be replaced. May only be used on S.S. Walden. Immune to Heavy Load penalty.'
    )
]


ships = [
    Ship(
        name='Serenity',
        engine=get_list_item_by_name(engines, 'Radeon Accelerator Mark I')
    ),
    Ship(
        name="Bonnie Mae",
        engine=get_list_item_by_name(engines, 'Radeon Accelerator Mark I')
    ),
    Ship(
        name='Yang Xi',
        engine=get_list_item_by_name(engines, 'Radeon Accelerator Mark I')
    ),
    Ship(
        name='Bonanza',
        engine=get_list_item_by_name(engines, 'Radeon Accelerator Mark I')
    ),
    Ship(
        name='Artful Dodger',
        crew_size=7,
        hold_storage_size=6,
        hold_stash_size=3,
        engine=get_list_item_by_name(engines, 'Radeon 6'),
        expansion='Artful Dodger'
    )
]
you_cant_take_the_sky_from_me_deck = []
you_cant_take_the_sky_from_me_deck.extend(captains)
you_cant_take_the_sky_from_me_deck.extend(ships)
you_cant_take_the_sky_from_me_deck.extend(engines)

you_cant_take_the_sky_from_me = Deck(
    name="You Can't Take the Sky from Me",
    type='setup',
    deck=you_cant_take_the_sky_from_me_deck
)


persephone_deck = [
    Person(
        name='Simon Tam',
        base_tech=3,
        professions=['medic'],
        keywords=['FANCY DUDS'],
        is_wanted=True,
        reroll_on='medic',
        reroll_condition='all'
    )
]
for card in persephone_deck:
    card.planet_deck = 'Persephone'
persephone = Deck(name='Persephone', type='Supply', deck=persephone_deck)


regina_deck = [
    Person(
        name='Kaylee',
        base_tech=3,
        professions=['mechanic'],
        is_moral=True,
        reroll_on='tech',
        reroll_condition='all',
        bonus_type='misbehave',
        bonus_amount=100
    )
]
for card in regina_deck:
    card.planet_deck = 'Regina'
regina = Deck(name='Regina', type='Supply', deck=regina_deck)


silverhold_deck = [
    Person(
        name='Zoe',
        base_fight=3,
        professions=['soldier'],
        is_wanted=1,
        reroll_on='fight',
        roroll_conditions='all',
        bonus_type='misbehave',
        bounus_amount=100,
    ),
    Person(
        name='Jayne',
        base_fight=2,
        professions=['merc'],
        is_wanted=1
    )
]
for card in silverhold_deck:
    card.planet_deck = 'Silverhold'
silverhold = Deck(name='Silverhold', type='Supply', deck=silverhold_deck)


space_bazaar_deck = [
    Person(
        name='Wash',
        cost=200,
        base_tech=1,
        base_talk=1,
        professions=['pilot'],
        is_moral=True,
        bonus_name='Hard Burn',
        bonus_text='+1 to full burn range'
    ),
    Person(
        name='Tracey',
        cost=100,
        base_fight=1,
        base_talk=1,
        professions=['grifter'],
        is_wanted=True,
        bonus_name='Unlucky',
        special_rule="When a crew is killed, Tracey must be killed first."
    ),
    Item(
        name="Wash's Lucky Dinosaurs",
        reroll_on='any',
        reroll_condition='1',
        reroll_requires_discard=True
    )
]
for card in space_bazaar_deck:
    card.planet_deck = 'Space Bazaar'
space_bazaar = Deck(name='Space Bazaar', type='Supply', deck=space_bazaar_deck)


serenity = get_list_item_by_name(ships, 'Serenity')
serenity.crew[1]=get_list_item_by_name(captains, 'Malcolm')
serenity.crew[2]=get_list_item_by_name(regina_deck, 'Kaylee')
serenity.crew[3]=get_list_item_by_name(persephone_deck, 'Simon Tam')
serenity.get_names('crew')
# artful_dodger = get_list_item_by_name(ships, 'artful dodger')
# simon = get_list_item_by_name(persephone, 'Simon Tam')

# mal.pprint_attributes()
serenity.attributes()
# simon.pprint_attributes()
