class Grid:
    def draw_line(self,pg,screen):
        for i in range(0,10):
            if (i%3==0):
                pg.draw.line(screen,(138, 154, 91),(50+50*i,50),(50+50*i,500),4)
                pg.draw.line(screen,(138, 154, 91),(50,50+50*i),(500,50+50*i),4)
            else:
                pg.draw.line(screen,(113, 121, 126),(50+50*i,50),(50+50*i,500),2)
                pg.draw.line(screen,(113, 121, 126),(50,50+50*i),(500,50+50*i),2)