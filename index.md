---
layout: default
---
<!-- <html>
<head></head>
<body>
{% include header.html %}
content
{% include sidebar.html %}
{% include footer.html %}
</body>
</html> -->

<form method="get" id="search-google" action="https://www.google.com/search" target="_blank"><input type="hidden" name="sitesearch" value="jekyllcodex.org" /><input type="text" name="q" maxlength="255" value="" placeholder="Search via Google" class="form-control" /></form>


{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}
{% assign vids = tag[1] | sort %}

{% if vids != empty %}

  <h2 id="{{tag[0] | uri_escape | downcase}}">{{tag[0]}}</H2>
     <p>
      {% for p in vids %}
     <a href="/{{p.type | downcase}}/"><img src="/assets/img/{{p.type | downcase}}.png" alt="{{p.type}}" title="{{p.type}}"/></a> <a href="{{ p.url }}">{{ p.title }}</a> ({{p.type}}/{{p.category}}) &raquo;  <span class="entry-date"><time datetime="{{ p.date | date_to_xmlschema }}" itemprop="datePublished">{{ p.date | date: "%B %d, %Y" }}</time></span>
     <br />
      {% endfor %}
    </p>
  
{% endif %}

{% endfor %}

<div class="home">

  <h1 class="page-heading">Posts</h1>

  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>