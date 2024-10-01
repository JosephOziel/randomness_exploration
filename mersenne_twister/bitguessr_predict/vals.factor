USING: kernel math prettyprint random ;

! mersenne twister is the default (i think)
624 [ random-32 . ] times

25 [ random-32 2 mod . ] times