# Binomial Distribution I 

#### Random Variable 
 
A _random variable_, X, is the real-val function X: S -> R in which there is an event for each interval I where I is a subset of R. 

#### Binomial Experiment 

A _binomial experiment_ (or _Bernoulli Trial_) is a statistical experiment with the following probabilities. 

* The experiment consists of n repeated trials. 
* The trials are independent. 
* The outcome of each trial is either _success_ (s) or_failure_ (f) 

#### Bernoulli Random Variable and Distribution 

The sample space (S) of a binomial experiment only contains two points, _s_ and _f_. 

Define a _Bernoulli random variable_ to be the random variable defined by 

```
	X(_s_) = 1 

	X(_f_) = 0 
```

If we consider the probability of success to be _p_ and the probability of failure to be _q_ (where _q_ = 1 - _p_), then the _probability mass function_ (PMF) of X is 

```
			1 - p ≡ q, if x = 0 
p(_x_) = 	p 		 , if x = 1 
			0 		 , otherwise. 
```

This can also be expressed as 

```
	f(_x_) = p<sup>x</sup>(1 -  p)<sup>1-x</sup>, for x ∈ {0, 1}
```