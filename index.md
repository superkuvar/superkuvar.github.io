---
layout: default
title:  🍳
---


<form method="get" id="search-google" action="https://www.google.com/search" target="_blank"><input type="hidden" name="sitesearch" value="superkuvar.com" /><input type="text" name="q" maxlength="255" value="" placeholder="Google pretraga" class="form-control" /></form>


{% for category in site.categories %}
 
  <h3>{{ category[0] | upcase }} ({{ category[1].size }})</h3>
  
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

