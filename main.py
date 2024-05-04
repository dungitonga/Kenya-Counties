import turtle
import pandas

screen = turtle.Screen()
screen.title("Kenya County Game")
image = "kenya.gif"
screen.addshape(image)
turtle.shape(image)


df = pandas.read_csv("47_counties.csv")
answer_list = df.county.to_list()
guess_list = []

while len(guess_list) < 47:
    answer_county = screen.textinput(title=f"{len(guess_list)}/47 Counties", prompt="Enter county name")
    name = answer_county.title()

    if name == "Exit":
        remaining_counties = [county for county in answer_list if county not in guess_list]

        county_dict = {"county": remaining_counties}
        info = pandas.DataFrame(county_dict)
        info.to_csv("counties_to_learn")
        break

    if name in answer_list:
        guess_list.append(name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county = df[df.county == name]
        t.goto(county.iloc[0]['x'], county.iloc[0]['y'])
        t.write(name)




