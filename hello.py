import turtle

links = [1, 2, 3, 4, 5, 6, 7, 8]
sides = [1, 2, 3, 4, 5, 6]

weaver = turtle.Turtle()
weaver.width(2)
weaver.color('orange')

# Move back so the chain is centered.
weaver.penup()
weaver.back(80)
weaver.pendown()

#for link in links:
    # Draw a hexagon.
    
for side in sides:
    weaver.forward(10)
    weaver.right(60)
    
    for side in sides:
        weaver.forward(50)
        weaver.right(60)
        
        
        
#Move back so the chain is centered.
    weaver.penup()
    weaver.back(20)
    #weaver.left(60)
    
    weaver.pendown()

weaver.hideturtle()

