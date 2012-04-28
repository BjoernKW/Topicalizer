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
<h2>API</h2>
<table align="center">
  <tr>
    <td width="600">
      Topicalizer cannot only be used via the main website, but by an API as well. There are currently five methods:<br /><br />
      1.) <b>http://www.topicalizer.com/getCompleteAnalysis/</b><br /><br />
      This method provides you with the complete analysis that is also rendered if using the main website, the only difference being that the results are not shown in XHTML, but as an XML data structure.<br /><br />
      2.) <b>http://www.topicalizer.com/getKeywords/</b><br /><br />
      This method returns just the keywords and single word frequencies for a site, again as an XML data structure.<br /><br />
      3.) <b>http://www.topicalizer.com/getAugmentedKeywords/</b><br /><br />
      This method returns the keywords of a sentence or phrase (you could possibly also enter longer texts, but the generated results would most probably be too large to make sense) and their hyponyms, hypernyms and synonyms as an XML data structure. Unlike method 1.) and 2.), this method is only available for English<br /><br />
      4.) <b>http://www.topicalizer.com/getCoOccurrences/</b><br /><br />
      This method returns the most likely co-occurrences for the keywords of a sentence or phrase (the same remark as for 3.) regarding larger texts applies here as well), this method also is only available for (American) English.<br /><br />
      5.) <b>http://www.topicalizer.com/getSemWeb/</b><br /><br />
      This method returns a web of related terms for a given term by making use of the Google API and Wikipedia. This feature currently is only available for English terms.<br /><br /><br />
      Method 1.) and 2.) both take two arguments, method 3.) only takes the <b>plainText</b> argument:<br /><br />
      1.) <b>url</b> or <b>plainText</b><br />
      You can either enter a URL or a plain text to be analysed, likewise as on the main website. However, you should make sure, that when using the plainText option you either access the method by POST (which is the preferred way anyway, since GET does only support arguments up to a length of 255 characters) or you URL-escape the text before sending it to this method.<br /><br />
      2.) <b>language</b><br />
      This should be the language of the document behind the URL or the text you gave as the first argument. The specification of the document / text language is used for appropriately selecting some language parameters like stop words and syllable structures.<br />
      You can also set this argument to 'automatic', which will invoke an automatic language recognition. However, you might run into trouble when using this feature, if either the text is too short or if it contains several languages in approximately equal shares.<br />
      This argument can have any of the following values:<br /><br />
      <span py:for="language in languages">
        &nbsp;&nbsp;&nbsp;&nbsp;<span py:content="language">X</span><br />
      </span><br /><br />
      Method 4.) takes the following two arguments:<br /><br />
      1.) <b>plainText</b><br />
      You can enter a plain text to be analysed here. However, you should make sure, that you either access the method by POST (which is the preferred way anyway, since GET does only support arguments up to a length of 255 characters) or you URL-escape the text before sending it to this method.<br /><br />
      2.) <b>textCategory</b><br />
      This should be the rough text category the text to be analysed belongs to.
      This argument can have any of the following values, the categories are taken from the Brown Corpus of Present-Day Edited American English, which is used to calculate the results for this method. The descriptions of the respective text category are given in brackets:<br /><br />
      <span py:for="textCategoryIndex, textCategoryTitle in textCategories">
        &nbsp;&nbsp;&nbsp;&nbsp;<span py:content="textCategoryIndex">X</span> (<span py:content="textCategoryTitle">X</span>)<br />
      </span><br /><br />
      Method 5.) takes one argument:<br /><br />
      1.) <b>term</b><br />
      This should be the term to create a web of related terms for.<br /><br /><br />
      <b>Usage examples:</b><br /><br />
      http://www.topicalizer.com/getCompleteAnalysis/?url=http://www.turbogears.org/&amp;language=english<br />
      http://www.topicalizer.com/getKeywords/?url=http://www.turbogears.org/&amp;language=automatic<br />
      http://www.topicalizer.com/getAugmentedKeywords/?plainText=This is is just a test<br />
      http://www.topicalizer.com/getCoOccurrences/?plainText=This is is just a test&amp;textCategory=a<br />
      http://www.topicalizer.com/getSemWeb/?term=Semantic Web<br />
    </td>
  </tr>
</table>
</body>
</html>
