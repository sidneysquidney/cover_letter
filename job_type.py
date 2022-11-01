from context import context


def job(type: str) -> str:
    type = type.lower()
    paragraph = ''
    # creativity, games, strategy, stocks, data,
    if type == 'data':
        paragraph += f"As part of my computer science course on Codecademy, I learnt about databases. I can create, manipulate, query, and possess all the essential skills needed to work with databases. I enjoy data and statistics, and combined this skill with my love of great sayings and quotes to create a database website project. Try this one by Abraham Lincoln: 'We should be too big to take offense and too noble to give it.'"
    elif type == 'stocks':
        paragraph += f"My main interests are in data, algorithms, strategy, and maths, and so the trading emphasis on the role excites me greatly. I do not invest myself, as after a lengthy research process culminating in me being a lot more scared of the whole process than I was at the start, made me rethink. But I still find the whole subject fascinating, and never lose an opportunity to quiz my less risk-averse investment minded friends on the latest trends and tactics."
    elif type == 'games':
        paragraph += f"Since I was a child I have loved strategy games. I grew up on chess, civilization, and diplomacy, and have recently started (attempting) playing go. Programming seemed to fit right into that bracket - problem solving, I fell in love. Joining the gaming industry would be an amazing opportunity, and make me very happy."
    return paragraph


# print(intro('variety'))
