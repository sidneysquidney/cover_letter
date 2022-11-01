from context import context


def fun_perks(perks: list, fun_perk_one: str = None, fun_perk_two: str = None) -> str:
    fun_perks = ''
    if fun_perk_one or fun_perk_two:
        fun_perks = fun_perk_one
        if fun_perk_two:
            fun_perks += f" and the {fun_perk_two}"
        fun_perk = f"\n\nFinally, the list of benefits mentioned sounds extremely desirable (most notably the {fun_perks}!), especially coming from a self-employed background."
    return fun_perks


def perks(perks: list, quote: str) -> str:
    paragraph = ''
    if 'mentorship' in perks:
        paragraph += f"Finally, as I am moving into a new career and greatly enjoying programming, my continued development and learning are very important to me. This is both from a career perspective and a personal one. This is one of my biggest motivations for a job, and one that your company seems to value with your declaration of '{quote}'"
    return paragraph
    # progression, mentorship, intellectual, variety, creativity,


# print(perks('free birthday cake', 'complementary car'))
