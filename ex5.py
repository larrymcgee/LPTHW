my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
cm_to_inches = 0.39
inches_to_cm = 2.54
lbs_to_kg = 0.45359237
kg_to_lbs = 2.20462

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print ("%s lbs = %s kg") % (my_weight, my_weight * lbs_to_kg)
print ("%s inches = %s cm") % (my_height, my_height * inches_to_cm)
