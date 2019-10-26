# NihilistPypher

NihilistPypher was made as a project for Data Security Course at [PUT Poznań](https://www.put.poznan.pl/). 
The application implements simple cypher originally used by [_Russian Nihilists_](https://en.wikipedia.org/wiki/Russian_nihilist_movement) in the 1880s used later by the [_KGB_](https://en.wikipedia.org/wiki/First_Chief_Directorate).
I've chosen to write substitution flavor of this cypher which execution is explained below.

### How it works

Suppose you want to cypher a message. To do it with this method you're going to need:
- Unciphered message (duh)
- Two keys

Let's say you want to send a message: **RED SQUARE TOMMOROW**. 
We're going to pick __TSAR__ as our first key and __RUSSIA__ as the second one.

First

Sources:
- [American Cryptogram Association - Nihilist Substitution](https://www.cryptogram.org/downloads/aca.info/ciphers/NihilistSubstitution.pdf "Here be thy pdf")
- PUT Poznań inside pdf _szyfry-cd3.pdf_ (probably not allowed to link it)
