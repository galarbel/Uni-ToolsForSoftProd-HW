#!/bin/bash

###################################
## Simple Example

# Show the checked properties
cbmc argv-out-of-bounds.c --show-properties --bounds-check --pointer-check

# Show the verification condition formulas
cbmc argv-out-of-bounds.c --show-vcc --bounds-check --pointer-check

# Check the verification condition
cbmc argv-out-of-bounds.c --bounds-check --pointer-check
# Expected bug: [main.pointer_dereference.6] dereference failure: object bounds in argv[(signed long int)2]: FAILURE

# Get a counterexample trace
cbmc argv-out-of-bounds.c --bounds-check --pointer-check --trace

# Fixed example
cbmc  argv-out-of-bounds-fixed.c --bounds-check --pointer-check --trace

##
###################################

###################################
## Modular Example

cbmc modular-bug.c --function sum --bounds-check
cbmc modular.c --function sum --bounds-check

##
###################################

###################################
## Loop Unwinding

cbmc binsearch.c --function binsearch --bounds-check
cbmc binsearch.c --function binsearch --unwind 6 --bounds-check --unwinding-assertions
cbmc binsearch.c --function binsearch --unwind 6 --bounds-check --unwinding-assertions --trace

##
###################################

###################################
## Unbounded Loop

cbmc lock-example.c --bounds-check
cbmc lock-example.c --unwind 6 --bounds-check --unwinding-assertions

##
###################################


###################################
## Verification Condition

cbmc --function foo array-access.c --show-properties --bounds-check

cbmc --function foo array-access.c --bounds-check --show-vcc

cbmc --function foo array-access.c --bounds-check --trace

##
###################################
