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
<form method="post" action="/process/">
  <table align="center">
    <tr>
      <td>
        <input type="text" class="greentext" name="url" size="30" onclick="JavaScript:if (this.value == 'Enter URL') { this.value=''; }" onblur="JavaScript:if (this.value == '') { this.value='Enter URL'; }" value="Enter URL" /> or
      </td>
    </tr>
    <tr>
      <td>
	<textarea class="greentext" name="plainText" cols="30" rows="5">Enter plain text</textarea>
      </td>
    </tr>
    <tr>
      <td>
	language:
	<select name="language">
	  <option py:for="language in languages" value="${language}" py:content="language">X</option>
	</select>
      </td>
    </tr>
  </table><br />
  <input type="hidden" name="submit" value="topicalize it!" />
  <input type="submit" value="topicalize it!" />
</form>
<br /><br /><br />
<table py:if="error == 0" align="center">
  <tr>
    <td width="750">
      <h1>Analysis for <span py:if="url != 'text'">'<a href="${url}" target="_blank">${url}</a>'</span><span py:if="url == 'text'">${url}</span></h1><br />
      <h2>Language</h2><br />
      ${languageTitle}, character set: ${charset}<br /><br /><hr /><br />
      <span py:if="debug == 1">
        <h2>Stop words</h2><br />
        <table>
	  <tr py:for="stopword in stopWordList">
	    <td>/<span py:content="stopword">X</span>/</td>
	  </tr>
        </table>
        <h2>Corpus</h2><br />
        ${XML(corpus)}<br /><br /><hr /><br />
      </span>
      <h2>Lexical analysis</h2><br />
      <table width="100%">
	<tr>
	  <td class="maintext-bold" width="40%">
            Number of words (tokens):
	  </td>
	  <td class="maintext">
	    ${tokenCount}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Number of distinct words (types):
	  </td>
  	  <td class="maintext">
	    ${typeCount}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Average number of words per sentence:
	  </td>
	  <td class="maintext">
	    ${averageTokensPerSentence}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Average number of words per paragraph:
	  </td>
	  <td class="maintext">
	    ${averageTokensPerParagraph}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Lexical density:
	  </td>
	  <td class="maintext">
	    ${lexicalDensity}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Average number of characters per word:
	  </td>
	  <td class="maintext">
	    ${averageCharactersPerWord}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
           Average number of syllables per word:
	  </td>
	  <td class="maintext">
	    ${averageSyllablesPerWord}
	  </td>
	</tr>
	<tr>
          <td class="maintext-bold">
            Longest word:
	  </td>
	  <td class="maintext">
	    '${XML(maxToken)}' <span class="maintext-bold">(${maxTokenLength} character<span py:if="maxTokenLength != 1">s</span></span>)
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Shortest word:
	  </td>
	  <td class="maintext">
            '${XML(minToken)}' (${minTokenLength} <span class="maintext-bold">character<span py:if="minTokenLength != 1">s</span></span>)
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Ten most frequent words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="unigram, frequency in mostFrequentUnigrams">
		<td py:content="XML(unigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="unigram, frequency in mostFrequentUnigramsAll">
		<td py:content="XML(unigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
      </table>
      <br /><hr /><br />
      <h2>Phrasal analysis</h2><br />
      <table width="100%">
	<tr>
	  <td class="maintext-bold">
            Ten most frequent two-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="bigram, frequency in mostFrequentBigrams">
		<td py:content="XML(bigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Ten most frequent three-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="trigram, frequency in mostFrequentTrigrams">
		<td py:content="XML(trigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Ten most frequent two-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="bigram, frequency in mostFrequentBigramsWithStopWords">
		<td py:content="XML(bigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Ten most frequent three-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="trigram, frequency in mostFrequentTrigramsWithStopWords">
		<td py:content="XML(trigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent two-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="bigram, frequency in mostFrequentBigramsAll">
		<td py:content="XML(bigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent three-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="trigram, frequency in mostFrequentTrigramsAll">
		<td py:content="XML(trigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent four-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="tetragram, frequency in mostFrequentTetragramsAll">
		<td py:content="XML(tetragram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent five-word phrases:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="pentagram, frequency in mostFrequentPentagramsAll">
		<td py:content="XML(pentagram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent two-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="bigram, frequency in mostFrequentBigramsWithStopWordsAll">
		<td py:content="XML(bigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent three-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="trigram, frequency in mostFrequentTrigramsWithStopWordsAll">
		<td py:content="XML(trigram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent four-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="tetragram, frequency in mostFrequentTetragramsWithStopWordsAll">
		<td py:content="XML(tetragram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Most frequent five-word phrases, including stop words:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="pentagram, frequency in mostFrequentPentagramsWithStopWordsAll">
		<td py:content="XML(pentagram)">X</td>
		<td py:content="frequency">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
      </table>
      <br /><hr /><br />
      <h2>Textual analysis</h2><br />
      <table width="100%">
	<tr>
	  <td class="maintext-bold" width="40%">
            Number of paragraphs:
	  </td>
	  <td class="maintext">
	    ${paragraphCount}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Number of sentences:
	  </td>
	  <td class="maintext">
	    ${sentenceCount}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Average number of sentences per paragraph:
	  </td>
	  <td class="maintext">
	    ${averageSentencesPerParagraph}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Longest sentence:
	  </td>
	  <td class="maintext">
	    '${XML(maxSentence)}' <span class="maintext-bold">(${maxSentenceLength} word<span py:if="maxSentenceLength != 1">s</span></span>)
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Shortest sentence:
	  </td>
	  <td class="maintext">
	    '${XML(minSentence)}' <span class="maintext-bold">(${minSentenceLength} word<span py:if="minSentenceLength != 1">s</span></span>)
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Readability according to <a href="http://en.wikipedia.org/wiki/Gunning-Fog_Index" target="_blank">Gunning-Fog Index</a> (the higher, the harder to read):
	  </td>
	  <td class="maintext">
	    ${readabilityGF}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Readability according to <a href="http://en.wikipedia.org/wiki/Automated_Readability_Index" target="_blank">Automated Readability Index</a> (the higher, the harder to read):
	  </td>
	  <td class="maintext">
	    ${readabilityAR}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Readability according to <a href="http://en.wikipedia.org/wiki/Coleman-Liau_Index" target="_blank">Coleman-Liau Index</a> (the higher, the harder to read):
	  </td>
	  <td class="maintext">
	    ${readabilityCL}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Average readability (the higher, the harder to read):
	  </td>
	  <td class="maintext">
	    ${readabilityAverage}
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Suggested keywords:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="keyword in keywords">
		<td py:content="XML(keyword)">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
	<tr>
	  <td class="maintext-bold">
            Abstract:
	  </td>
	  <td class="maintext">
	    <table>
	      <tr py:for="sentence, occurences in abstract">
		<td py:content="XML(sentence)">X</td>
	      </tr>
	    </table>
	  </td>
	</tr>
      </table>
      <br /><span py:if="url != 'text'"><a href="/getSimilarDocuments/?url=${url}">Find similar documents</a></span><span py:if="url == 'text'"><a href="/getSimilarDocuments/?plainText=${query}">Find similar documents</a></span>
    </td>
    <td>
      <br />
      <script type="text/javascript"><!--
      google_ad_client = "pub-4897855422499261";
      google_ad_width = 160;
      google_ad_height = 600;
      google_ad_format = "160x600_as";
      google_ad_type = "text_image";
      google_ad_channel ="";
      google_color_border = "A8DDA0";
      google_color_bg = "EBFFED";
      google_color_link = "0000CC";
      google_color_url = "008000";
      google_color_text = "6F6F6F";
      //--></script>
      <script type="text/javascript"
      src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
      </script>
    </td>
  </tr>
</table>
<p py:if="error == 1" align="center">
  <span py:content="errorMessage">X</span>:<br />
  <a href="${url}" target="_blank">${url}</a>
</p>
</body>
</html>
