#Individual Projects on lists, tupples, and if statements

def draw_shape(lst,count):
    i=0
    j=0
    x=1
    y=1
    space=1
    for i in lst:
        shape=i[0]
        height=i[1]
        if shape=="square":
            print("square")

            for ind in range(height):
                for index in range(height):
                    print("*", end=" ")
                print("\n")
                        
            

        elif shape=="triangle":
            print("triangle")

            for ind in range(height):
                for index in range(ind+1):
                    print("*", end=" ")
                print("\n")
            


        elif shape=="pyramid":
            print("pyramid")

            for ind in range(1 ,height+1):
                for space in range(1,(height-ind)+1):
                    print(end="  ")

                for index in range(2*ind-1):
                    print("* ", end="")
                
                print("\n")
           
                          

print("Welcome to \"DRAW A SHAPE!\" program ")
print("You can enter a square, a triangle, or a pyramid")
NumberOfShapes=int(input("what is the number of shapes you will add? :"))
i=0
list=[] 
while(i<NumberOfShapes):
    shape=input("the shape is: ")
    height=int(input("and the height is: "))
    list.append((shape,height))
    i+=1

list.sort(key=lambda i:i[1])
print(list)
draw_shape(list,NumberOfShapes)