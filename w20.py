# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
def farm():

    total_head=35
    total_legs=94
    rabbit=(total_legs-(2*total_head))/2
    chicken=total_head-rabbit
    print("no of rabbit : ",rabbit)
    print("no of chicken : ",chicken)
farm()
