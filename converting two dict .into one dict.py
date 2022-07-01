# **using update
a={"name":"seminao","place":"banglore","age":122}
b={"salary":5000,"hobby":"singing","seminao":"ningshen"}
a.update(b)
print(a)

# **1:using unpak asstrict
a={"name":"seminao","place":"banglore","age":122}
b={"salary":5000,"hobby":"singing","seminao":"ningshen"}
j={**a,**b}
print(j)

# **:2
a={"name":"seminao","place":"banglore","age":122}
b={"salary":5000,"hobby":"singing","seminao":"ningshen"}
# j={**a,**b}
j=dict(a,**b)
print(j)



