# coding=utf-8
"""
py.py - Sopel Python Eval Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
from __future__ import unicode_literals, absolute_import, print_function, division

from requests import get

from sopel import module
from sopel.tools.web import quote


BASE_TUMBOLIA_URI = 'https://oblique.sopel.chat/'


@module.commands('py')
@module.output_prefix('[py] ')
@module.example('.py len([1,2,3])', '3', online=True)
def py(bot, trigger):
    """Evaluate a Python expression."""
    if not trigger.group(2):
        return bot.reply('I need an expression to evaluate.')

    query = trigger.group(2)
    uri = BASE_TUMBOLIA_URI + 'py/'
    answer = get(uri + quote(query)).content.decode('utf-8')
    if answer:
        bot.say(answer)
    else:
        bot.reply('Sorry, no result.')


if __name__ == "__main__":
    from sopel.test_tools import run_example_tests
    run_example_tests(__file__)