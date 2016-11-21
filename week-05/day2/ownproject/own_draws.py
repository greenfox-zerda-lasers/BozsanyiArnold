class Drawing:

    def draw_castle_body():
        width = 50
        print ('|' * width)

    def draw_castle_towers(num):
        space = num
        for i in range(0,num):
            i += 1
            space -= 1
            print((space*" ") + (i*'*') + ((i-1)*'*'))
Drawing.draw_castle_towers(5)
Drawing.draw_castle_body()
Drawing.draw_castle_body()
Drawing.draw_castle_body()
Drawing.draw_castle_body()
Drawing.draw_castle_body()
