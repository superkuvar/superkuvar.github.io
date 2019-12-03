---
layout: default
---

<ul class="">
    {% assign tags =  site.vacancies | map: 'tags' | join: ','  | split: ',' | uniq %}
     {% for tag in tags %}
        <li class="text-capitalize">
            <a href="{{ tag }}" class="sidebar-tag">{{ tag }}</a>
        </li>
     {% endfor %}
 </ul>