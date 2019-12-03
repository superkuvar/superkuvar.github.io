---
layout: default
---

The list of all Posts in category CATEGORY.
{{site.categories.Kolači}}


The list of all Posts with tag TAG.
{{site.tags.orasi}}

TAGS:
{{site.tags}}

<ul class="">
    {% assign tags =  site.vacancies | map: 'tags' | join: ','  | split: ',' | uniq %}
     {% for tag in tags %}
        <li class="text-capitalize">
            <a href="{{ tag }}" class="sidebar-tag">{{ tag }}</a>
        </li>
     {% endfor %}
 </ul>