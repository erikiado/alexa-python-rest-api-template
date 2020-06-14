# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = _("Pokedex")
WELCOME_MESSAGE = _("Hola, soy tu {}. Que pokemon deseas analizar?")
WELCOME_REPROMPT = _("Para saber que puedes analizar di ayuda pokedex")
DISPLAY_CARD_TITLE = _("{}  - Recipe for {}.")

HELP_MESSAGE = _("ayuda pokedex! yo te puedo describir el pokemon que solicites, solo di su nombre o di. 'describe a squirtle'.")
HELP_REPROMPT = _("You can say things like, what's the recipe for a {}, or you can say exit...Now, what can I help you with?")
FALLBACK_MESSAGE = _("The {} skill can't help you with that.")

STOP_MESSAGE = _("Adios!")

POKEMON_REPEAT_MESSAGE = _("Try saying repeat.")
# speech = "Sorry, there was some problem. Please try again!!"
POKEMON_NOT_FOUND_MESSAGE = _("Disculpa, hubo un problema. porfavor intenta de nuevo o repite ayuda pokedex!")
POKEMON_NOT_FOUND_WITH_ITEM_NAME = _("the recipe for {}. ")
POKEMON_NOT_FOUND_WITHOUT_ITEM_NAME = _("that recipe. ")
POKEMON_NOT_FOUND_REPROMPT = _("What else can I help with?")


POKEMON_ES_MX = {
    'snow golem': 'A snow golem can be created by placing a pumpkin on top of  two snow blocks on the ground.',
    'pillar quartz block': 'A pillar of quartz can be obtained by placing a block of quartz on top of a block of quartz in mine craft.',
    'firework rocket': 'A firework rocket can be crafted by placing a firework star in the left middle square, a piece of paper in the center square, and gunpowder in the right middle square in a crafting table. Similar to a firework star, a firework rocket can have more gunpowder added in the bottom row to increase the duration of a rocket.',
}

POKEMON_EN_US = {
    'snow golem': 'A snow golem can be created by placing a pumpkin on top of  two snow blocks on the ground.',
    'pillar quartz block': 'A pillar of quartz can be obtained by placing a block of quartz on top of a block of quartz in mine craft.',
    'firework rocket': 'A firework rocket can be crafted by placing a firework star in the left middle square, a piece of paper in the center square, and gunpowder in the right middle square in a crafting table. Similar to a firework star, a firework rocket can have more gunpowder added in the bottom row to increase the duration of a rocket.',
}

POKEMON_DE_DE = {
    'snow golem': 'A snow golem can be created by placing a pumpkin on top of  two snow blocks on the ground.',
    'pillar quartz block': 'A pillar of quartz can be obtained by placing a block of quartz on top of a block of quartz in mine craft.',
    'firework rocket': 'A firework rocket can be crafted by placing a firework star in the left middle square, a piece of paper in the center square, and gunpowder in the right middle square in a crafting table. Similar to a firework star, a firework rocket can have more gunpowder added in the bottom row to increase the duration of a rocket.',
}