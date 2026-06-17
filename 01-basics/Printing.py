#Printing in different ways
name= "Sars_cov_2"
disease= "COVID-19"
print("Name of the virus is:",name)

print("The name of the virus is {}".format(name))

#printing multiple variables
print("{} is the virus responsible for {} disease".format(name,disease))

#f-string python 3.6 and above
print(f"The name of virus is {name} and it is responsible for {disease} disease")

# concatenation of string
print("The name of virus is " + name + " and it is responsible for " + disease + " disease")
