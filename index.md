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


<a href="#salate">SALATE</a>
<a href="#Prelivi za salate">PRELIVI ZA SALATE</a>
<a href="#predjela">PREDJELA</a>
<a href="#Dodaci za supe i čorbe">DODACI ZA SUPE I ČORBE</a>
<a href="#supe i čorbe">SUPE I ČORBE</a>
<a href="#prilozi">PRILOZI</a>
<a href="#jela od mesa">JELA OD MESA</a>
<a href="#jela bez mesa">JELA BEZ MESA</a>
<a href="#Jela od ribe">JELA OD RIBE</a>
<a href="#Jela od jaja">JELA OD JAJA</a>
<a href="#hleb i pogače">HLEB I POGAČE</a>
<a href="#Sosovi">SOSOVI</a>
<a href="#Peciva">PECIVA</a>
<a href="#slatkiši">SLATKIŠI</a>
<a href="#Sladoled">SLADOLED</a>
<a href="#Testenine">TESTENINE</a>
<a href="#Rolati">ROLATI</a>
<a href="#Slana zimnica">SLANA ZIMNICA</a>
<a href="#peciva">PECIVA</a>
<a href="#torte">TORTE</a>
<a href="#slane pite">SLANE PITE</a>
<a href="#hlebovi i pogače">HLEBOVI I POGAČE</a>
<a href="#proje">PROJE</a>
<a href="#slatke pite">SLATKE PITE</a>
<a href="#Slatka zimnica">SLATKA ZIMNICA</a>
<a href="#testa">TESTA</a>
<a href="#kolači">KOLAČI</a>
<a href="#posni kolači">POSNI KOLAČI</a>
<a href="#čvarci">ČVARCI</a>
<a href="#napici">NAPICI</a>


{% for category in site.categories %}
<!-- 
  <h3 id="{{ category[0] }}">{{ category[0] | upcase }} ({{ category[1].size }})</h3>
 -->
{% endfor %}


{% for category in site.categories %}
 
  <h3 id="{{ category[0] }}">{{ category[0] | upcase }} ({{ category[1].size }})</h3>
  
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

