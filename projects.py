from context import context


def projects(type: str) -> str:
    paragraph = f"I have completed a number of projects in my own time (which can be viewed on my portfolio website and github profile)."
    if type == 'back-end':
        paragraph += f"The area I enjoyed most was the back-end, and in particular the algorithms and various strategies I had to use to create my connect four game, and cipher decrypter. I learnt about the hillclimb algorithm, the minimax algorithm, the montecarlo tree search algorthim, Index of coincidence, and frequency attacks. to think, that once upon a time these terms meant nothing to me!"
    elif type == 'front-end':
        paragraph += f"Presently, I'm learning React to make the front-end of a Window Cleaning Website that supports musicians. It's a big project, that I have a vested interest in, being one of its founders. I've had to tunnel deep into the rabbit hole of what makes a successful website, logo, brand, UX, and how to unlock the full potential of the unique USP we've created."
    elif type == 'savvy':
        paragraph += f"In fact, one of the projects I created, was a cover letter creator, that I even used to write this letter! I grew very disenfranchised and impatient with how long each letter would take to compose, while the chances of hearing back from the company were always slim. It seemed an unfair trade-off. But rest assured, if you give me the honour in responding to my application, I will give full commitment to whatever following steps the interview or job role may take."
    return paragraph
