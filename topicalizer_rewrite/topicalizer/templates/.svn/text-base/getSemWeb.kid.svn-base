<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE analysis SYSTEM "/static/dtd/linkedTerms.dtd">
<analysis xmlns:py="http://purl.org/kid/ns#" py:extends="'masterXML.kid'">
  <result py:if="error == 0">
    <linkedTerms>
      <term py:for="term in linkedTerms">
	<text py:content="XML(term['text'])">X</text>
      </term>
    </linkedTerms>
  </result>
  <error py:if="error == 1">
    <message py:content="errorMessage">X</message>
  </error>
</analysis>
