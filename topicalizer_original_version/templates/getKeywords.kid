<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE analysis SYSTEM "/static/dtd/keywords.dtd">
<analysis xmlns:py="http://purl.org/kid/ns#" py:extends="'masterXML.kid'">
  <result py:if="error == 0">
    <tenMostFrequentWords>
      <word py:for="unigram, frequency in mostFrequentUnigrams">
	<token py:content="XML(unigram)">X</token>
	<frequency py:content="frequency">X</frequency>
      </word>
    </tenMostFrequentWords>
    <mostFrequentWordsAll>
      <word py:for="unigram, frequency in mostFrequentUnigramsAll">
	<token py:content="XML(unigram)">X</token>
	<frequency py:content="frequency">X</frequency>
      </word>
    </mostFrequentWordsAll>
    <keywords>
      <keyword py:for="keyword in keywords">
	<token py:content="XML(keyword)">X</token>
      </keyword>
    </keywords>
  </result>
  <error py:if="error == 1">
    <message py:content="errorMessage">X</message>
    <url>${url}</url>
  </error>
</analysis>
