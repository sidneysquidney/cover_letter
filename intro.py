from context import context


def intro(type: str = 'formal', element_one: str = None) -> str:
    type = type.lower()
    paragraph = ''
    if type == 'formal':
        paragraph += f"I am interested in seeking employment with {context['company_name']}, please find my resume enclosed with the details relevant to my experience, skills and education. References, or other information you require are available on request.\n\nAs my resume indicates, I am a self-taught {context['job_title']}. Across the past 3 years, I have autonomously learned:"
    elif type == 'informal':
        paragraph += f"As my resume indicates, I am a self-taught {context['job_title']}. This has given me great confidence in my ability to learn skills and complete projects. Across the past 3 years, I have autonomously learned:"
    elif type == 'busy':
        paragraph += f"I am interested in seeking employment with {context['company_name']}. As my resume indicates, I am a self-taught {context['job_title']}. This has given me great confidence in my ability to learn skills and complete projects. I am really excited about a number of elements within {context['company_name']}, your '{element_one}' being one of them, and believe the ability to learn quickly, and be curious, is essential. Across the past 3 years, I have autonomously learned:"
    elif type == 'startup':
        paragraph += f"I am interested in seeking employment with {context['company_name']}. As my resume indicates, I am a self-taught {context['job_title']}. This has given me great confidence in my ability to learn skills and complete projects. I think this would position me perfectly in the start-up environment of {context['company_name']}. Across the past 3 years, I have autonomously learned:"
    elif type == 'variety':
        paragraph += f"I am interested in seeking employment with {context['company_name']}. As my resume indicates, I am a self-taught {context['job_title']}. This has given me great confidence in my ability to learn skills and complete projects. I think this is an essential skill for a company (such as {context['company_name']}), that completes a wide variety of tasks. Across the past 3 years, I have autonomously learned:"
    return paragraph


# print(intro('variety'))
