# NihilistPypher

NihilistPypher was made as a project for Data Security Course at [PUT Poznań](https://www.put.poznan.pl/). 
The application implements simple cypher originally used by [_Russian Nihilists_](https://en.wikipedia.org/wiki/Russian_nihilist_movement) in the 1880s used later by the [_KGB_](https://en.wikipedia.org/wiki/First_Chief_Directorate).
I've chosen to write substitution flavor of this cypher which execution is explained below.

### Explaining the cypher
-----

Suppose you want to cypher a message. To do it with this method you're going to need:
- Unciphered message (duh)
- Two keys

Let's say you want to send a message: **RED SQUARE TOMMOROW**. 
We're going to pick __TSAR__ as our first key and __RUSSIA__ as the second one.

First, we need to prepare our data.

##### Step 1. Preparing the matrix.

Let's take the alphabet and put it into matrix

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| a | b | c | d | e |   |
| f | g | h | i | j |   |
| k | l | m | n | o |   |
| p | q | r | s | t |   |
| u | v | w | x | y | z |

Well, something's definitely wrong. We have to substitute one of the letters so it would be an even matrix of 5x5. 
The usual substiution options are:
 - _w_ for _v_
 - _v_ for _w_
 - _i_ for _j_
 - _j_ for _i_
 - _c_ for _k_
 or
 - _k_ for _c_.

I'm going to substitue _j_ for _i_ for this presentation. Our matrix has to contain only unique symbols. Now our matrix looks like this

 | | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
__1__| a | b | c | d | e |
**2**| f | g | h | i | k |
**3**| l | m | n | o | p |
**4**| q | r | s | t | u |
**5**| v | w | x | y | z |

Now, let's take our first key __TSAR__, put it into our matrix and remove substitutes of the letters, so the matrix would still be 5x5.

 || 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
**1**| **_t_** | **_s_** | **_a_** | **_r_** | b |
**2**| c | d | e | f | g |
**3**| h | i | k | l | m |
**4**| n | o | p | q | u |
**5**| v | w | x | y | z |

Our matrix is now ready for coding.


##### Step 2. Cyphering the key.

Our key needs to be translated to the coordinates of the according letters from the matrix to continue. To do it, simply look for the letter from our key and write down it's coordinates from the grid where the first digit is the matrix row. (eg. "c" is 21)

Following this rule coded key looks like this:

|  	| R  	| U  	| S  	| S  	| I  	| A  	|
|-------	|----	|----	|----	|----	|----	|----	|
| coded: 	| 14 	| 45 	| 12 	| 12 	| 32 	| 13 	|


##### Step 3. Cyphering the word. (finally)

First, following the rule from step 2 code the actual word.
|        	| R  	| E  	| D  	| S  	| Q  	| U  	| A  	| R  	| E  	| T  	| O  	| M  	| M  	| O  	| R  	| O  	| W  	|
|--------	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|
| coded: 	| 14 	| 23 	| 22 	| 12 	| 44 	| 45 	| 13 	| 14 	| 23 	| 11 	| 42 	| 35 	| 35 	| 42 	| 14 	| 42 	| 52 	|

Lastly the last step would be to add key to our word in exact manner:

| message:          	| R  	| E  	| D  	| S  	| Q  	| U  	| A  	| R  	| E  	| T  	| O  	| M  	| M  	| O  	| R  	| O  	| W  	|
|-------------------	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|
| **key:**              	| **R**  	|**U**  	| **S**  	| **S**  	| **I**  	| **A**  	|**R**  	| **U**  	| **S**  	|**S**  	| **I**  	| **A**  	| **R** 	|**U**  	| **S**  	| **S** 	| **I**  	|
| coded message:    	| 14 	| 23 	| 22 	| 12 	| 44 	| 45 	| 13 	| 14 	| 23 	| 11 	| 42 	| 35 	| 35 	| 42 	| 14 	| 42 	| 52 	|
| coded key:        	| 14 	| 45 	| 12 	| 12 	| 32 	| 13 	| 14 	| 45 	| 12 	| 12 	| 32 	| 13 	| 14 	| 45 	| 12 	| 12 	| 32 	|
Which, by adding the digits gives us:

| cyphered message: 	| 28 	| 68 	| 34 	| 24 	| 76 	| 58 	| 27 	| 59 	| 35 	| 23 	| 74 	| 48 	| 49 	| 78 	| 26 	| 54 	| 84 	|
|-------------------	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	|----	

### About the application
---
![Application screenshot](https://i.ibb.co/9H9cycQ/Adnotacja-2019-10-27-121502.png)

Thanks to previous explanation of the cypher exact explanation is not needed. 
We can import a file with message to code or input it manually. 
I've added a "substitue letters" radio buttons to choose between all the available options for substitution. 
Decyphering with keys and substitutions different from the ones used in encoding will result with an error or just jibberish.
"Export to file" button is used to save the cyphered message to file, seems obvious.
"Generate grids" button shows all the info that's used to get the Output

### Tech talk
---
I know I should not put an `.exe` file into my repository, but it's just the fastest solution right now.

Obviously the application is written with ![Python](https://img.icons8.com/metro/26/000000/python.png) (why else would i insert "Py" in the name? 🤔) with the usage of:
- `Tkinter` (to wrap the code into a slick interface)
- [Unidecode](https://pypi.org/project/Unidecode/) (to remove all special symbols from the cyphered messages)
- [Pandas](https://pandas.pydata.org/) (to show a good looking grid of the alphabet)

Huge thanks to
- [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe),
- [Rubber duck](https://rubberduckdebugging.com/cyberduck/),
- and Caffeine
for making this code come true.
### Information reference
---
- [American Cryptogram Association - Nihilist Substitution](https://www.cryptogram.org/downloads/aca.info/ciphers/NihilistSubstitution.pdf)
- PUT Poznań inside pdf _szyfry-cd3.pdf_ (probably not allowed to link it)
- [Tkinter documentation](https://docs.python.org/3/library/tk.html)
- [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/)
