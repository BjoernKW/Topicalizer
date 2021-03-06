<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python import sitetemplate ?>
<html dir="ltr" lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="sitetemplate">
<head profile="http://dublincore.org/documents/dcq.html" py:match="item.tag=='{http://www.w3.org/1999/xhtml}head'" py:attrs="item.items()">
<title py:replace="''">Topicalizer - The tool for topic extraction, text analysis and abstract generation</title>
<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" py:replace="''" />
<meta py:replace="item[:]" />
<meta name="DC.title" content="Topicalizer - The tool for topic extraction, text analysis and automatic abstract generation" />
<meta name="DC.subject" content="Text analysis" />
<meta name="DC.description" content="Topicalizer is a tool for topic extraction, text analysis, abstract generation and search engine optimization" />
<meta name="DC.audience" content="Webmasters, bloggers, linguists, authors" />
<meta name="DC.creator" content="Bj&ouml;rn Wilmsmann" />
<meta name="DC.publisher" content="Topicalizer" />
<meta name="DC.contributor" content="Bj&ouml;rn Wilmsmann" />
<meta name="DC.date" content="2006-01-27" />
<meta name="DC.type" content="Text" />
<meta name="DC.format" content="text/xhtml" />
<meta name="DC.identifier" content="http://www.topicalizer.com/" />
<meta name="DC.source" content="none" />
<meta name="DC.language" content="en" />
<meta name="DC.relation" content="Index" />
<meta name="DC.coverage" content="Text analysis, semantic web, search engine optimization, topic recognition, tagging, tag, topic, text summary" />
<meta name="DC.rights" content="All rights reserved" />
<meta name="audience" xml:lang="en" content="Webmasters, bloggers" />
<meta name="audience" content="Webmasters, bloggers" lang="en" />
<meta name="keywords" xml:lang="en" content="Text analysis, semantic web, search engine optimization, topic recognition, tagging, tag, topic, text summary" />
<meta name="robots" content="index,follow" />
<meta name="revisit-after" content="1 month" />
<link rel="shortcut icon" href="/static/images/favicon.ico" />
<link rel="icon" href="/static/images/favicon.ico" />
<link rel="stylesheet" type="text/css" href="${tg.url('/static/css/style.css')}" />
<script src="${tg.url('/static/javascript/fat.js')}" type="text/javascript"></script>
</head>
<body py:match="item.tag=='{http://www.w3.org/1999/xhtml}body'" py:attrs="item.items()">
<div py:if="tg.config('identity.on') and not defined('logging_in')" id="pageLogin">
  <span py:if="tg.identity.anonymous">
    <a href="${tg.url('/login')}">Login</a>
  </span>
  <span py:if="not tg.identity.anonymous">
    Welcome ${tg.identity.user.display_name}.
    <a href="${tg.url('/logout')}">Logout</a>
  </span>
</div>
<br /><br /><br />
<table align="center">
  <tr>
    <td width="440" class="logo">
      <p id="logo" class="fade-129f12">
        <br />
        <img src="${tg.url('/static/images/topicalizer.png')}" width="400" height="50" alt="Topicalizer" border="0" />
        <br />
        <br />
      </p>
    </td>
  </tr>
</table>
<br /><br />
<div id="status_block" class="flash" py:if="value_of('tg_flash', None)" py:content="tg_flash"></div>
<div py:replace="[item.text]+item[:]"/>
<br /><br />
<a href="${tg.url('/')}">Home</a> | <a href="${tg.url('/about')}">About</a> | <a href="/serendipity/">Blog</a> | <a href="${tg.url('/faq')}">FAQ</a> | <a href="${tg.url('/api')}">API</a> | <a href="${tg.url('/tools')}">Tools</a> | <a href="${tg.url('/links')}">Links</a> | <a href="${tg.url('/terms')}">Terms of Use</a> | <a href="${tg.url('/contact')}">Contact</a> | <a href="${tg.url('/disclaimer')}">Disclaimer</a>
<br /><br />
&copy; 2006-2007 by <a href="http://topicalizer.com/bwilmsmann/english.html">Bj&ouml;rn Wilmsmann</a>
<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-571882-1";
urchinTracker();
</script>
</body>
</html>
