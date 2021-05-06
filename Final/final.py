
# Alanté "Alan" D. Powell
# Programming Language Concepts
# Spring 2021 - Final Exam - Question 6

# It depends. If you intend to right a 1-line return statement as I did, it is important
# to express symbols to enforce precedence. If you break each section up into different variables
# and call them in the correct order no.


# Constants
A = 51 
B = 7 
C = 11 
D = 13 
E = 2

def q1_func(a, b, c):
    return (((a * b)-1)+c)

print(q1_func(A, B, C))

def q2_func(a, b, c, d):
    return (((a * (b-1)) / c) % d)

print(q2_func(A, B, C, D))

def q3_func(a, b, c, d, e):
    return ((a - b) / c) & ((d * e) / a) - 3

print(q3_func(A, B, C, D, E))

def q4_func(a, b, c, d, e):
    return (((a + b) <= c) * (d > (b-e)))

print(q4_func(A, B, C, D, E))

def q5_func(a, c, d, e):
    return ((a * -1) or (( c == d) & e))

print(q5_func(A, C, D, E))

def q6_func(a, b, c, d):
    return (((a > b) or c) or (d <= 17))

print(q6_func(A, B, C, D))

def q7_func(a, b, c, d):
    return a + (b * c) + d

print(q7_func(A, B, C, D))

def q8_func(a):
    return (1 + a) + (a + 1)

print(q8_func(A))

# Spring 2021 - Final Exam - Question 7

###
# 
# EXPR --> EQUAL
# 
# EQUAL --> compare(('=' | '/=') compare())*;
# COMPARE --> not(('||' | '~|')not())*;
# NOT --> less_than_or_greater_than(('&&' | '/' | '!')less_than_or_greater_than())*;
# TERM --> factor(('-' | '+' | '<=' | '%')factor())*;
# FACTOR --> post(('*' | '>=' | '&')post())*;
# POST --> pre(('++' | '--')pre())*;
# 
# ###