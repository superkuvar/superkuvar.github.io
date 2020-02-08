---
layout: default
title: Index
description: Tradicionalna kuhinja i praktični recepti iz bakinih vitrina.
---

<form method="get" id="search-google" action="https://www.google.com/search" target="_blank"><input type="hidden" name="sitesearch" value="superkuvar.com" /><input type="text" name="q" maxlength="255" value="" placeholder="Google pretraga" class="form-control" />
<button type="submit" form="search-google" value="Submit">GO</button>
</form>

<br style="clear:both" />

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


<div style="clear:both; padding-top:20px;line-height:26px">
<h2>Kategorije:</h2>
<a href="#salate">SALATE</a> * 
<a href="#prelivi za salate">PRELIVI ZA SALATE</a> * 
<a href="#predjela">PREDJELA</a> * 
<a href="#dodaci za supe i čorbe">DODACI ZA SUPE I ČORBE</a> * 
<a href="#supe i čorbe">SUPE I ČORBE</a> * 
<a href="#prilozi">PRILOZI</a> * 
<a href="#jela od mesa">JELA OD MESA</a> * 
<a href="#jela bez mesa">JELA BEZ MESA</a> * 
<a href="#jela od ribe">JELA OD RIBE</a> * 
<a href="#jela od jaja">JELA OD JAJA</a> * 
<a href="#sosovi">SOSOVI</a> * 
<a href="#hlebovi i pogače">HLEBOVI I POGAČE</a> * 
<a href="#proje">PROJE</a> * 
<a href="#peciva">PECIVA</a> * 
<a href="#testenine">TESTENINE</a> * 
<a href="#slane pite">SLANE PITE</a> * 
<a href="#slatke pite">SLATKE PITE</a> * 
<a href="#kolači">KOLAČI</a> * 
<a href="#posni kolači">POSNI KOLAČI</a> * 
<a href="#slatkiši">SLATKIŠI</a> * 
<a href="#torte">TORTE</a> * 
<a href="#rolati">ROLATI</a> * 
<a href="#sladoledi">SLADOLEDI</a> * 
<a href="#slana zimnica">SLANA ZIMNICA</a> * 
<a href="#slatka zimnica">SLATKA ZIMNICA</a> * 
<a href="#čvarci">ČVARCI</a> * 
<a href="#napici">NAPICI</a>  
</div>

---


{% for category in site.categories %}
 
  <h3 id="{{ category[0] }}">{{ category[0] | upcase }} ({{ category[1].size }})</h3>
  
  <ul class="cat">
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

---

<a href="/poslovi-u-kuhinji/">POSLOVI U KUHINjI</a>
