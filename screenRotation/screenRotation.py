from resource import *

click_element_in_right_click_mouse_menu("displaySettings.jpg")

click_element("2.jpg")

li = pageDown_until_element_is_visible(['Landscapel.jpg', "Portrait flippedl.jpg"])

# new_orientation = "Landscape.jpg" if li == "Portrait flippedl.jpg" else "Portrait flipped.jpg"

if li == "Portrait flippedl.jpg":
    new_orientation = "Landscape.jpg"
else:
    new_orientation = "Portrait flipped.jpg"

click_element(li)

click_element(new_orientation)