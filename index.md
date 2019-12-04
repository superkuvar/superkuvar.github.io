---
layout: default
---

<form method="get" id="search-google" action="https://www.google.com/search" target="_blank"><input type="hidden" name="sitesearch" value="superkuvar.com" /><input type="text" name="q" maxlength="255" value="" placeholder="Search via Google" class="form-control" /></form>


{% for category in site.categories %}
  <h3>{{ category[0] }}</h3>
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}


{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
