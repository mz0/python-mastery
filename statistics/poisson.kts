#!/usr/bin/env kotlin

import kotlin.math.pow

val mean = 2.5
val sample = 5
println("%.3f".format(mean.pow(sample)))
println("%.3f".format(kotlin.math.E.pow(-mean)))
println(fact5())
println("%.3f".format(
  mean.pow(sample) * kotlin.math.E.pow(-mean) / fact5() )
)

fun fact5(): Int {
  return 2 * 3 * 4 * 5
}
