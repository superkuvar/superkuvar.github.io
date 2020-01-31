---
layout: default
title: Index
---

<form method="get" id="search-google" action="https://www.google.com/search" target="_blank"><input type="hidden" name="sitesearch" value="superkuvar.com" /><input type="text" name="q" maxlength="255" value="" placeholder="Google pretraga" class="form-control" /></form>
<style>
input{
float: right;
padding: 10px;
border-radius: 10px;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
font-size: 20px;
}
</style>



<!-- 
{% for category in site.categories %}
  <h3 id="{{ category[0] }}">{{ category[0] | upcase }} ({{ category[1].size }})</h3>
{% endfor %} -->


{% for category in site.categories %}
 
  <h3 id="{{ category[0] }}">{{ category[0] | upcase }} ({{ category[1].size }})</h3>
  
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

