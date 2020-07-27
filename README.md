### Installations and Requirments

This project requires no additional installations.

### Project Motivation

A python package that caclulates probabilities of outcomes from a collection of weighted coins.


### File Descriptions

- Coins_Load_Data.py: a class that initializes a coin collection.
- Coins.py: a class that inherits the default coin collection from Coins_Load_Data, and then can work 
- Binomialdistribution.py: a class that inherits the read data function from the
general distribution, and then contains various binomial distribution methods like calculating
the probability of a specific outcome, and plotting the probabilities of all possible outcomes.
- init.py: initializes the binomial and gaussian classes.
- numbers.txt: a sample dataset to test the gaussian distribution classes.
- numbers_binomial.txt: a sample data-set to test the binomial distribution classes. 
- test.py: unit tests to test if the classes are working as expected.

### How to Interact with this project

The primary scripts are the Generaldistribution.py, Gaussiandistribution.py and
Binomialdistribution.py. 

To Import this package in python use: <pre><code>pip install sauce_probability
</code></pre>

You can find this package on pypi at https://pypi.org/project/sauce-probability/0.1/

The sample text files can be used as sample data for the gaussian and binomial classes.

numbers.txt can be used for the Gaussian class, and numbers_binomial.txt for the binomial class.

### Licensing, Authors, Acknowledgments, etc.

Copyright 2020 Billy Hansen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.