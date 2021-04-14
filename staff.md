---
layout: page
title: Who We Are
description: A listing of all course members.
nav_order: 3
---

# Staff

The information below is stored in the `_staffers` directory and rendered according to the layout file, `_layouts/staffer.html`.

## Instructors
{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

{% assign teaching_assistants = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign num_teaching_assistants = teaching_assistants | size %}
{% if num_teaching_assistants != 0 %}
## Teaching Assistants
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign leads = site.staffers | where: 'role', 'Lead ULA' %}
{% assign num_leads = leads | size %}
{% if num_leads != 0 %}
## Lead ULAs
{% for staffer in leads %}
{{ staffer }}
{% endfor %}
{% endif %}

{% assign learning_assistants = site.staffers | where: 'role', 'Undergraduate Learning Assistant' %}
{% assign num_learning_assistants = learning_assistants | size %}
{% if num_learning_assistants != 0 %}
## Undergraduate Learning Assistants
{% for staffer in learning_assistants %}
{{ staffer }}
{% endfor %}
{% endif %}

