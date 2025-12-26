#!/usr/bin/env kotlin
/*
The manager of a industrial plant is planning to buy a machine of either type A or type B.

For each day’s operation:
* The number of repairs X, that machine A needs is a Poisson random variable with mean 0.88
  The daily cost of operating A is 160 + 40 * X^2
* The number of repairs X, that machine B needs is a Poisson random variable with mean 1.55
  The daily cost of operating B is 128 + 40 * X^2

Assume that the repairs take a negligible amount of time and the machines are maintained
nightly to ensure that they operate like new at the start of each day.

Find and print the expected daily cost for each machine.
*/

import kotlin.math.pow

val aX2 = ll2(0.88)
val bX2 = ll2(1.55)
println("%.3f".format(160 + 40 * aX2))
println("%.3f".format(128 + 40 * bX2))

fun ll2(lx: Double): Double {
  return lx + lx.pow(2)
}
