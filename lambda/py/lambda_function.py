# -*- coding: utf-8 -*-

# This is a simple Pokedex Alexa Skill, built using
# the decorators approach in skill builder, supports i18n and slot handling.
import logging
import gettext

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

from alexa import data, util

import requests

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
  """Handler for Pokedex Launch."""
  # type: (HandlerInput) -> Response
  _ = handler_input.attributes_manager.request_attributes["_"]
  speech = _(data.WELCOME_MESSAGE).format(_(data.SKILL_NAME))

  return handler_input.response_builder.speak(speech).set_card(
      SimpleCard(_(data.SKILL_NAME), speech)).set_should_end_session(
      False).response


@sb.request_handler(can_handle_func=is_intent_name("GetPokemonIntent"))
def get_pokemon_intent_handler(handler_input):
  """Handler for Get Pokemon Intent."""
  # type: (HandlerInput) -> Response
  slots = handler_input.request_envelope.request.intent.slots
  if len(slots) > 0:
    slot = handler_input.request_envelope.request.intent.slots['pokemon']
    if slot.value:
      r = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(slot.value))
      pokemon_json = r.json()
      speech = "{} es el numero {}, ".format(slot.value, pokemon_json.get('id','no encontrado'))
      speech += "pesa {}, ".format(pokemon_json.get('weight','no encontrado'))
      speech += "mide en promedio {}, ".format(pokemon_json.get('height','no encontrado'))
      speech += "y es de tipo "
      for t in pokemon_json.get('types',[]):
        speech += "{} ".format(t.get('type',dict()).get('name'))
  else:
    speech = "No he encontrado un pokemon con ese nombre"

  return handler_input.response_builder.speak(speech).set_card(
      SimpleCard("Pokemon Info", speech)).set_should_end_session(
      True).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
  """Handler for Help Intent."""
  # type: (HandlerInput) -> Response
  _ = handler_input.attributes_manager.request_attributes["_"]
  speech = _(data.HELP_MESSAGE)

  return handler_input.response_builder.speak(speech).ask(
      speech).set_card(SimpleCard(
          "Hello World", speech)).response


@sb.request_handler(
  can_handle_func=lambda handler_input:
    is_intent_name("AMAZON.CancelIntent")(handler_input) or
    is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
  """Single handler for Cancel and Stop Intent."""
  # type: (HandlerInput) -> Response
  _ = handler_input.attributes_manager.request_attributes["_"]
  speech = _(data.STOP_MESSAGE)

  return handler_input.response_builder.speak(speech).set_card(
      SimpleCard(_(data.SKILL_NAME), speech)).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
  """AMAZON.FallbackIntent is only available in en-US locale.
  This handler will not be triggered except in that locale,
  so it is safe to deploy on any locale.
  """
  # type: (HandlerInput) -> Response
  speech = (
      "The Pokedex skill can't help you with that.  "
      "You can ask for pokemon!!")
  reprompt = "You can ask for a pokemon!!"
  handler_input.response_builder.speak(speech).ask(reprompt)
  return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
  """Handler for Session End."""
  # type: (HandlerInput) -> Response
  return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
  """Catch all exception handler, log exception and
  respond with custom message.
  """
  # type: (HandlerInput, Exception) -> Response
  logger.error(exception, exc_info=True)
  _ = handler_input.attributes_manager.request_attributes["_"]

  speech = _(data.POKEMON_NOT_FOUND_MESSAGE)
  handler_input.response_builder.speak(speech).ask(speech)

  return handler_input.response_builder.response


@sb.global_request_interceptor()
def request_logger(handler_input):
  # print("Request received: {}".format(handler_input.request_envelope.request))
  locale = handler_input.request_envelope.request.locale
  # logger.info("Locale is {}".format(locale))

  # Add locale translation to every request
  i18n = gettext.translation(
      'data', localedir='locales', languages=[locale], fallback=True)
  handler_input.attributes_manager.request_attributes[
      "_"] = i18n.gettext


lambda_handler = sb.lambda_handler()
