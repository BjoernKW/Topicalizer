<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE analysis SYSTEM "/static/dtd/keywords.dtd">
<analysis xmlns:py="http://purl.org/kid/ns#" py:extends="'masterXML.kid'">
  <result py:if="error == 0">
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
