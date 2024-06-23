from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'goat' in lowered:
        return 'Cashbooda cooks!'
    elif 'help' in lowered:
        return 'try: hello, goat, how are you, bye, are you real?, cashbooda, roll dice'
    elif 'cashbooda' in lowered:
        return 'monkey🐒'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'are you real?' in lowered:
        return 'nah im fake bruh'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
