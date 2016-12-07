#part 1
x=[4,6,1,3,5,7,25]
def draw_stars(some_list):
    for counter in some_list:
        output =""
        for counter in range(0,len(some_list)):
            output=output + "*"
        print output

print draw_stars(x)

#part 2
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars2(new_list):
    for counter in new_list:
        output =""
        if type(counter) is int:
            for x in range(counter):
                output=output +"*"



        elif type(counter) is str:
            for x in range(len(counter)):
                letter= counter[0].lower()
                output=letter+output
        print output


print draw_stars2(y)
