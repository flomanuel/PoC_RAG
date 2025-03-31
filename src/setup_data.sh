#!/bin/bash

printf "========== Cleaning up directory...\n"
rm -rf ./data/*

printf "========== Downloading regulations as training data...\n"

curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006R1907-20241218" > ./data/reach1.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006R1907-20230528" > ./data/reach2.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006R1907-20211001" > ./data/reach3.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006R1907-20191030" > ./data/reach4.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02006R1907-20161011" > ./data/reach5.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02006R1907-20150101" > ./data/reach6.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02006R1907-20110306" > ./data/reach7.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014R0422&qid=1743269299985" > ./data/random-regulation1.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014R0423&qid=1743269299985" > ./data/random-regulation2.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32014R0539&qid=1743269299985" > ./data/random-regulation3.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32015R2120&qid=1743269299985" > ./data/random-regulation4.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32002D0620&qid=1743269299985" > ./data/random-regulation5.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32015R0756&qid=1743269299985" > ./data/random-regulation6.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32012R1217&qid=1743269299985" > ./data/random-regulation7.html
curl "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32015D0642&qid=1743269299985" > ./data/random-regulation8.html
