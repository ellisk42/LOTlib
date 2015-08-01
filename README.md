LOTlib
------

LOTlib is a Python 2 library for implementing "language of thought" models. A LOTlib model specifies a set of primitives and captures learning as inference over compositions of those primitives in order to express complex concepts. LOTlib permits lambda expressions, meaning that learners can come up with abstractions over compositions and define new primitives. Frequently, models use sampling in order to determine likely compositional hypotheses given some observed data. 

There are several sampling methods provided, including tree-regeneration Metropolis-Hastings (from the "rational rules" model of Goodman et al. 2008), and variants that include tempering, annealing, tempered transitions, and other search algorithms. 

The best way to use this library is to read and modify the examples. 

LOTlib also provides support for MPI through a wrapper for mpi4py (LOTlib.MPI), allowing sampling algorithms to run in parallel on a simple computer or cluster.

REQUIREMENTS
------------

- numpy
- scipy

The following are infrequently used (i.e., not required for most functionality):

- matplotlib (plotting)
- mpi4py (if using MPI)
- cachetools (for memoization)
- graphviz (for DOT images of trees)

INSTALLATION
------------

Put this library somewhere - e.g. ~/Libraries/LOTlib/
	
Set the PYTHONPATH environment variable to point to LOTlib/:
	
	$ export PYTHONPATH=$PYTHONPATH:~/Libraries/LOTlib
	
You can put this into your .bashrc file to make it loaded automatically when you open a terminal. On ubuntu and most linux, this is:
	
	$ echo 'export PYTHONPATH=\$PYTHONPATH:~/Libraries/LOTlib' >> ~/.bashrc

And you should be ready to use the library via:
	
	import LOTlib
	
EXAMPLES and TUTORIAL
---------------------

A good starting place is the FOL folder, which contains a simple example to generate first-order logical expressions. These have simple boolean functions as well as lambda expressions. 

The best reference for learning how to create/modify grammars is Tutorial/FunctionNodeDemo. It contains all of the syntax for various parts of grammars, including how to use primitives and lambdas. 

More examples are provided in the "Examples" folder. These include: simple symbolic regression, the recursive number learning model, a quantifier learning model. The "tests" folder may also be useful, as this runs some simple models to check for, e.g., correct sampling and inference. 

Citation:
---------

This software may be cited as:

	@misc{piantadosi2014lotlib,
	author={Steven T. Piantadosi},
	title={{LOTlib: Learning and Inference in the Language of Thought}},
	year={2014},
	howpublished={available from https://github.com/piantado/LOTlib}
	}