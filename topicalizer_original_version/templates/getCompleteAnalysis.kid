<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE analysis SYSTEM "/static/dtd/analysis.dtd">
<analysis xmlns:py="http://purl.org/kid/ns#" py:extends="'masterXML.kid'">
  <result py:if="error == 0">
    <charset>${charset}</charset>
    <language>${languageTitle}</language>
    <lexical>
      <tokenCount>${tokenCount}</tokenCount>
      <typeCount>${typeCount}</typeCount>
      <averageWordsPerSentence>${averageTokensPerSentence}</averageWordsPerSentence>
      <averageWordsPerParagraph>${averageTokensPerParagraph}</averageWordsPerParagraph>
      <lexicalDensity>${lexicalDensity}</lexicalDensity>
      <averageCharactersPerWord>${averageCharactersPerWord}</averageCharactersPerWord>
      <averageSyllablesPerWord>${averageSyllablesPerWord}</averageSyllablesPerWord>
      <longestWord length="${maxTokenLength}">${XML(maxToken)}</longestWord>
      <shortestWord length="${minTokenLength}">${XML(minToken)}</shortestWord>
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
    </lexical>
    <phrasal>
      <tenMostFrequentBigrams>
        <bigram py:for="bigram, frequency in mostFrequentBigrams">
          <token py:content="XML(bigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </bigram>
      </tenMostFrequentBigrams>
      <tenMostFrequentTrigrams>
        <trigram py:for="trigram, frequency in mostFrequentTrigrams">
          <token py:content="XML(trigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </trigram>
      </tenMostFrequentTrigrams>
      <tenMostFrequentBigramsWithStopWords>
        <bigram py:for="bigram, frequency in mostFrequentBigramsWithStopWords">
          <token py:content="XML(bigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </bigram>
      </tenMostFrequentBigramsWithStopWords>
      <tenMostFrequentTrigramsWithStopWords>
        <trigram py:for="trigram, frequency in mostFrequentTrigramsWithStopWords">
          <token py:content="XML(trigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </trigram>
      </tenMostFrequentTrigramsWithStopWords>
      <mostFrequentBigramsAll>
        <bigram py:for="bigram, frequency in mostFrequentBigramsAll">
          <token py:content="XML(bigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </bigram>
      </mostFrequentBigramsAll>
      <mostFrequentTrigramsAll>
        <trigram py:for="trigram, frequency in mostFrequentTrigramsAll">
          <token py:content="XML(trigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </trigram>
      </mostFrequentTrigramsAll>
      <mostFrequentTetragramsAll>
        <tetragram py:for="tetragram, frequency in mostFrequentTetragramsAll">
          <token py:content="XML(tetragram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </tetragram>
      </mostFrequentTetragramsAll>
      <mostFrequentPentagramsAll>
        <pentagram py:for="pentagram, frequency in mostFrequentPentagramsAll">
          <token py:content="XML(pentagram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </pentagram>
      </mostFrequentPentagramsAll>
      <mostFrequentBigramsWithStopWordsAll>
        <bigram py:for="bigram, frequency in mostFrequentBigramsWithStopWordsAll">
          <token py:content="XML(bigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </bigram>
      </mostFrequentBigramsWithStopWordsAll>
      <mostFrequentTrigramsWithStopWordsAll>
        <trigram py:for="trigram, frequency in mostFrequentTrigramsWithStopWordsAll">
          <token py:content="XML(trigram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </trigram>
      </mostFrequentTrigramsWithStopWordsAll>
      <mostFrequentTetragramsWithStopWordsAll>
        <tetragram py:for="tetragram, frequency in mostFrequentTetragramsWithStopWordsAll">
          <token py:content="XML(tetragram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </tetragram>
      </mostFrequentTetragramsWithStopWordsAll>
      <mostFrequentPentagramsWithStopWordsAll>
        <pentagram py:for="pentagram, frequency in mostFrequentPentagramsWithStopWordsAll">
          <token py:content="XML(pentagram)">X</token>
          <frequency py:content="frequency">X</frequency>
        </pentagram>
      </mostFrequentPentagramsWithStopWordsAll>
    </phrasal>
    <textual>
      <paragraphCount>${paragraphCount}</paragraphCount>
      <sentenceCount>${sentenceCount}</sentenceCount>
      <averageSentencesPerParagraph>${averageSentencesPerParagraph}</averageSentencesPerParagraph>
      <longestSentence length="${maxSentenceLength}">${XML(maxSentence)}</longestSentence>
      <shortestSentence length="${minSentenceLength}">${XML(minSentence)}</shortestSentence>
      <gunningFog>${readabilityGF}</gunningFog>
      <automatedReadability>${readabilityAR}</automatedReadability>
      <colemanLiau>${readabilityCL}</colemanLiau>
      <averageReadability>${readabilityAverage}</averageReadability>
      <keywords>
        <keyword py:for="keyword in keywords">
          <token py:content="XML(keyword)">X</token>
	</keyword>
      </keywords>
      <abstract>
        <sentence py:for="sentence, occurences in abstract">
          <token py:content="XML(sentence)">X</token>
	</sentence>
      </abstract>
    </textual>
  </result>
  <error py:if="error == 1">
    <message py:content="errorMessage">X</message>
    <url>${url}</url>
  </error>
</analysis>
