state = {}
Camera = require "lib.camera" --hump cam
function clearLoveCallbacks()
    love.draw = nil
    love.keypressed = nil
    love.keyreleased = nil
    love.mousepressed = nil
    love.mousereleased = nil
    love.update = nil
end

function loadState(name)
    state = {}
    clearLoveCallbacks()
    local path = "states/" .. name
    require(path .. "/main") --moves into that file
    load()
end

function love.load()
    love.window.setMode(800,600,{resizable=true})
    height = love.graphics.getHeight()
    width = love.graphics.getWidth()
    loadState("menu") -- NAME OF FOLDER IN STATES FOLDER CONTAINING MAIN.LUA
end

function winResize()
    if ((love.graphics.getHeight() ~= height) or (love.graphics.getWidth() ~= width)) then
        love.event.push("resize")
        height = love.graphics.getHeight()
        width = love.graphics.getWidth()
    end
end

function load() end
function love.draw() end
function love.update(dt) end
function love.focus(bool) end
function love.keypressed(key, unicode) end
function love.keyreleased(key) end
function love.mousepressed(x,y,button) end
function love.mousereleased(x,y,button) end
function love.quit() end