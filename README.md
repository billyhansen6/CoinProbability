### Installations and Requirments

This project requires no additional installations.

### Project Motivation

A python package that calculates probabilities of outcomes from a collection of weighted coins.


### File Descriptions

- Coins_Load_Data.py: a class that initializes a coin collection.
- Coins.py: a class that inherits the default coin collection from Coins_Load_Data, replaces
the collection with user defined coins, and then calculates the likelihood of various outcomes.
- init.py: initializes the Bayes_Coins class.
- test.py: unit tests to test if the classes are working as expected.

### How to Interact with this project

To install this package in python use: <pre><code>pip install Coin_Probability_Sauce
</code></pre>

Import the relevant module by using: <pre><code>from Coins_Probability_Sauce import Bayes_Coins
</code></pre>

You can then create a custom coin collection using the create_new_collection()
function, and experiment with various probabilities using
heads_from_both_coins()
calculate_random_flip_heads()
calculate_random_flip_tails()


### Licensing, Authors, Acknowledgments, etc.

Copyright 2020 Billy Hansen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.