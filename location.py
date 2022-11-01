def location(loc: str, type: str) -> str:
    loc, type = loc.lower(), type.lower()
    paragraph = ''
    if loc == 'bath':
        paragraph += "\n\nI live in Bath, and to be honest, expected to have to commute for a job in tech. But I love the city, and if I had the opportunity to work here, it'd be a dream."
    elif loc == 'bristol':
        paragraph += '\n\nI live close-by (Bath), and love the city of Bristol. I have many fond memories of it, while it is easily commutable.'
    elif loc == 'london':
        paragraph += "\n\nI live in Bath, but love the city of London, and often commute up for current work commitments (which I'd be happy to do 2-3 times a week). I spent some of the best years of my life studying and working there and was truly inspird by its history, people, and energy."
    if type == 'office' or type == 'hybrid':
        paragraph += f" Furthermore, a {type} role suits me really well. I've always been self-employed, and a big part of my decision to change career is based in my desire for more of a team ethos. I want to learn and grow, from and with, the people around me."
    elif type == 'remote':
        paragraph += "These qualities, combined with my ability to autonomously learn, make me an ideal employee for remote work."
    return paragraph
