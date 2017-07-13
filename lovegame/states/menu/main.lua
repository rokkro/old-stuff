local frames = {}
local imageFile,posx,posy,butts,sprites
menu = 0
function load()
    imageFile = love.graphics.newImage("textures/button.png") --PLACEHOLDER IMG
    sprites = { --define location of sprites in image
        {x1=178,y1=200,w=364,h=178}, --blank, normal button
        {x1=564,y1=200,w=364,h=178}, --hover over button
        {x1=946,y1=200,w=364,h=178}, --clicked button
    }
    butts = { --properties of individual buttons
        start = {
            id = "start",
            posy = sprites[1].h/2,
            posx =  sprites[1].w/2 ,
            frame = 1, --current state (unclicked/hovered)
            yoffset=0,
        },
        other = {
            id = "other",
            posy = sprites[1].h/2 ,
            posx =  sprites[1].w/2 ,
            frame = 1,
            yoffset = -250, --offset from middle on y axis
        }
    }
    for i in pairs(sprites) do --create frame for each sprite (extracts buttons from sprite sheet)
        frames[i] = love.graphics.newQuad(sprites[i].x1, sprites[i].y1, sprites[i].w, sprites[i].h,imageFile:getDimensions())--image need to double # frames for it
    end
    cam = Camera(width/2,height/2,.5,0)
    cam.smoother = Camera.smooth.damped(10)
end

function love.draw()    --draws buttons. Takes in sprite sheet, the frame[state of sprite], and positioning,scaling, and offset
    cam:attach()
        love.graphics.draw(imageFile,frames[butts.start.frame], (width/2 - butts.start.posx),(height/2 - butts.start.posy),0)
        love.graphics.draw(imageFile,frames[butts.other.frame], (width/2 - butts.other.posx),(height/2 - butts.other.posy),0,nil,nil,nil, butts.other.yoffset)
    cam:detach()
end

function love.update(dt)
    cam:lockPosition(width/2,height/2,cam.smoother)
    winResize() --for window resizing

    for i in pairs(butts) do
        print(i.id)
        --mouseButts()
    end
end


function mouseButts(butts) --mouse interaction with buttons
    x, y = cam:mousePosition()--love.mouse.getPosition()
    if x > width/2 - butts.posx and x < width/2 + butts.posx
            and y > height/2 - butts.posy -butts.yoffset and y < height/2 + butts.posy - butts.yoffset then
        if love.mouse.isDown(1) then
            butts.frame = 3
            menu = butts.id
            --require("states.menu.menu2")
        else
            butts. frame = 2
        end
    else
        butts.frame = 1
    end
end


--NOTE: MUST PUT THE FILE PATH states/menu/FOLDER WHEN WORKING INSIDE
--NOTE 2: GIVEN THE STATE LOADING SET UP, YOU MUST USE function load() INSTEAD OF love.load
