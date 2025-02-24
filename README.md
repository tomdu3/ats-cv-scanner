# ats-cv-scanner
Python | ML Project | An ATS CV scanner

The code is written in Jupyter Notebook. In order to use it, it is necessary to:
1. make virtual environment and activate it
2. install dependencies from `requirements.txt` file
3. run Jupyter Notebook

I was using `uv` for virtual environment, but the dependencies can be install with `pip install requirements.txt`.

## Run the test `main.py`

The app can be tested with main.py:
- activate virtual environment and install dependencies
- change the file path/name (see the comments)
- run `python main.py`.

It will give you the output similar to this one:

```
[Your CV]

[Job Description]
---------------------------------------------
              Keywords matching              

****Matched keywords:****
environment | team | improve | structures | london | clients | science | problemsolving | ensure | projects | tools | algorithms | ability | python | data | implement | enhance | options | strong | global | agile | developer | development | communication | design | 

***Unmatched keywords:***
mathematics | looking | imm | frontoffice | talented | solutions | helps | indemand | business | meet | applications | upstream | responsibilities | risk | trading | pricing | execution | sales | innovative | fastpaced | contributing | physics | platforms | cuttingedge | closely | partners | booking | ii | distributed | focuses | middleware | qualifications | plus | methodologies | teams | opportunity | support | based | key | derivatives | building | expand | patterns | highimpact | organisations | changes | similar | stakeholders | mthree | fpml | technology | collaborate | messaging | jobready | degree | understanding | succeed | excellent | supporting | familiarity | umr | banks | making | networking | delivering | brokers | fx | trade | market | meeting | gather | etrading | continuous | products | office | kanban | desk | electronic | deploy | systems | analytical | marketmaking | xp | engineering | financial | investment | collaborative | fix | liaise | legacy | scrum | needs | regulatory | leading | exciting | transitioning | computer | mifid | models | external | operations | largescale | integration | developing | join | simplification | toptier | protocol | tcpip | develop | offerings | highperformance | 

Match percentage: 64%
```