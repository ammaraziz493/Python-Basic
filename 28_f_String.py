letter="My name is {}. I am from {}"
name="Ammar"
country="Pakistan"
print(letter.format(name,country))
letter="My name is {1}. I am from {0}"
name="Ammar"
country="Pakistan"
print(letter.format(country,name))
# f string
print(f"My name is {name}. I am from {country}")
sen="The price is {price:.2f}"
# price=2.009999
print(sen.format(price=2.4566))
price=2.009999
sen=f"The price is {price:.2f}"
print(sen)
print(f"{2*30}")
print(f"Hi i am print this f_string as it is.My name is {{name}}. I am from {{country}}")