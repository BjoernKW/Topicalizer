<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html dir="ltr" lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
<head profile="http://dublincore.org/documents/dcq.html">
<title>Topicalizer - The tool for topic extraction, text analysis and abstract generation</title>
<meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
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
<link rel="stylesheet" type="text/css" href="/static/css/standard.css" />
<script src="/static/javascript/fat.js" type="text/javascript"></script>
</head>
<body>
<h2>FAQ</h2>
<table align="center">
  <tr>
    <td width="600">
      <table>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    What does the name Topicalizer mean?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    In linguistics a topicalizer is a constituent that marks another constituent as the current topic. For example, in English there are topicalizers like 'regarding', 'given' and 'as for'. The idea behind this software is, amongst other aspects, about finding the topic (or rather topic framework) of a text, therefore this software can be seen as some kind of 'topic marker', too.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    Why did you create Topicalizer?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    This software was created as some kind of feasibility study in computational linguistics in the first place. Besides this, in my opinion a tool like this was still lacking on the web.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    Which programming language do you use for Topicalizer?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    Topicalizer was (and is being) built with <a href="http://www.python.org/" target="_blank">Python</a> and the <a href="http://www.turbogears.org/" target="_blank">Turbogears</a> web framework.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    Besides being interesting, what could be the purpose of this tool?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    The main purpose of this tool is providing webmasters, bloggers or any other kind of web author with a way of optimizing their websites regarding content structure, readability, topic coherence and last but not least search engine listings (for those into buzzword bingo: search engine optimization, SEO), since the latter is all about well-structured content and topic structure of a text.<br />
	    Moreover, this software can be used for automatically acquiring some useful semantic information about a document. The keyword method of the Topicalizer API could be used for automatically tagging a blog entry, just to give you an idea.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    When using Topicalizer with a specific URL as argument I receive a strange error message. Is there a way to avoid this?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    The reason for this might be that the HTML parser Topicalizer uses only understands well-formed HTML, so if a document should contain invalid HTML chances are that you receive a strange EXPAT parser error. One way to address this problem (apart from correcting the corresponding HTML code) is to use Topicalizer's plain text analysis option.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    When using Topicalizer with a specific URL one time and the plain text contained behind this URL another time I receive different results. How come?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    The account for this is very much like the one for the aforementioned problem: The HTML parser Topicalizer uses only understands well-formed HTML, so if a document should contain invalid HTML chances are that you either receive a strange EXPAT parser error or that some of the HTML code cannot filtered correctly (which sometimes is done on purpose by its creator, for instance as for ad server code), which in turn can lead to incorrect results. One way to address this problem (apart from correcting the corresponding HTML code) is to use Topicalizer's plain text analysis option.<br />
	    Furthemore, you will receive the best results with the plain text option anyway, because this way you can be sure that there is no additional (and undesired) text like html headers, titles and copyright information at all.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    Why is the document language important for the analysis?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    Topicalizer uses certain language-specific parameters like stop words and syllable structure, so choosing the appropriate language will significantly improve results.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    Why does Topicalizer still have the option for manually selecting a language, if there is a working automatic language recognition?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    The automatic language recognition works well enough for texts that are long enough and have been written in one language only. However, you might run into trouble when using this feature, if either the text is too short or if it contains several languages in approximately equal shares, so you still can select a language manually, if you do not trust Topicalizer's guess.<br /><br />
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>Q:</b>
	  </td>
	  <td>
	    How did you create this nifty fading effect on your logo?
	  </td>
	</tr>
	<tr>
	  <td>
	    <b>A:</b>
	  </td>
	  <td>
	    For this effect I used the 'Fade Anything Technique' developed by Adam Michela of <a href="http://www.axentric.com/" target="_blank">www.axentric.com</a>. Check out <a href="http://www.axentric.com/posts/default/7" target="_blanl">this page</a> for further details.<br /><br />
	  </td>
	</tr>
      </table>
    </td>
  </tr>
</table>
</body>
</html>
