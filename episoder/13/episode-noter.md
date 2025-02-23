## Links omtalt i episoden

- [TomatSource 11 test pypi pakken](https://test.pypi.org/project/tomatsource11/)
- [Claude ai, som jeg brugte til at skabe udgangspunktet for elpris koden](https://claude.ai/new)



## Installation af pakker fra [test.pypi.org](http://test.pypi.org)

I episoden prøver vi at installere tomatsource 11 pakken, som er lagt op på [test.pypi.org](http://test.pypi.org)

Det gjorde vi ved at afvikle denne kommando i en terminal.

```bash
uv add --index-url <https://test.pypi.org/simple/> --extra-index-url <https://pypi.org/simple/> tomatsource11
```

Princippet i kommandoen er at vi angiver et specifikt index-url som er [test.pypi.org](http://test.pypi.org), og samtidig fortæller vi UV at de øvrige afhængigheder som skal bruges men som ikke findes på [test.pypi.org](http://test.pypi.org) skal installeres fra —extra-index-url som jo så er produktions [pypi.org](http://pypi.org) siden.

## Den lille rant

I episoden laver jeg en mini rant, over elpris apps, der er gået fra at svare på spørgsmålet hvad koster strømmen nu på en simpel måde, til at være store apps med medlemsskab og energi budget osv osv.

Under el pris krisen startede jeg med at bruge en mobil ap, der vist nok hed noget med elpriser men siden hen har skiftet navn til elekt

Elekt finde både på iPhone og Android og den er nærmest umulig at komme i gang med for at finde ud af hvad elprisen er.

Til gengæld tog jeg også et kig på den højest ratede strømpris apps på mobil storen og den er faktisk udemærket. Den hedder elpris, og den løser opgaven som går på hvad koster strømmen lige nu.

Måske fortæller det meget godt hvad det er folk vil have når den der har højest rating kun fortælle hvad prisen er og viser en graf over elprisens udvikling.

## Python koden.

Python koden som [claude.ai](http://claude.ai) gav os, løste næsten opgaven, dog med lidt små bugs.

Dem ser vi på hvordan vi kan løse i afsnit 14 af tomatsource