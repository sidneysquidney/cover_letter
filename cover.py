from docxtpl import DocxTemplate

from context import context
from intro import intro
from location import location
from job_type import job_type
from projects import projects
from flare import flare
from perks import perks, fun_perks


context['intro'] = intro()
context['location'] = location('bath', 'office')
context['job_type'] = job_type('back-end')
context['projects'] = projects('savvy')
context['flare'] = flare()
context['perks'] = perks('mentorship')
context['fun_perks'] = fun_perks('free cake', 'complementary car')

doc = DocxTemplate('cover_template.docx')

doc.render(context)
doc.save(context['company_name'] + ' ' +
         context['job_title'] + ' cover letter')

# type of intro

# job perks - eg free meal at end
# projects - back-end, front savvy
# flare at the end - public speaking
# interests paragraph - data, creativity, strategy, algrotihms, problem-solving, charity, business
# job - development, training, progression, data
