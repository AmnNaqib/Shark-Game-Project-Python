# date: 16 APRIL 2023
# description: The code is for a game called "Shark Attack!" which has
#              a main menu with various options such as start, user manual,
#              who we are, and rules. The game involves controlling a shark
#              to eat fish and avoid jellyfish.

# import library
import turtle
import random
from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk

# to crete main menu
class MyFrame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(
            self,
            title="Shark Attack!",
            width=800,
            height=600,
            background="lightblue",
            resizable=False,
        )

        self.imageLabel = self.addLabel(text="", row=1, column=0, sticky="NSEW")
        self.startButton = self.addButton(
            text="       START       ",
            command=self.onStartButtonClick,
            row=2,
            column=0,
            columnspan=2,
        )

        self.userManualButton = self.addButton(
            text=" USER MANUAL",
            command=self.onUserManualButtonClick,
            row=3,
            column=0,
            columnspan=2,
        )
        self.wwaButton = self.addButton(
            text="  WHO WE ARE ", row=4, column=0, columnspan=2, command=self.wweWindow
        )
        self.rulesButton = self.addButton(
            text="       RULES       ",
            row=5,
            column=0,
            columnspan=2,
            command=self.onRules,
        )
        self.startButton["font"] = ("timesnewroman", 20, "bold")
        self.startButton["background"] = "skyblue"

        self.userManualButton["font"] = ("timesnewroman", 20, "bold")
        self.userManualButton["foreground"] = "skyblue"

        self.wwaButton["font"] = ("timesnewroman", 20, "bold")
        self.wwaButton["foreground"] = "skyblue"

        self.rulesButton["font"] = ("timesnewroman", 20, "bold")
        self.rulesButton["foreground"] = "skyblue"

        self.image = PhotoImage(file="gametitle.png")
        self.imageLabel["image"] = self.image
        self.imageLabel["background"] = "lightblue"

    # function if 'start' button clicked
    def onStartButtonClick(self):
        # shrink the main menu
        self.setSize(0, 0)
        try:
            sgame()
        except turtle.Terminator:
            exit()

    # function if 'How to play' button clicked
    def onUserManualButtonClick(self):
        self.destroy()
        newWindow = EasyFrame()
        newWindow.setTitle("HOW TO PLAY")
        newWindow.setResizable(False)
        newWindow.setSize(800, 600)
        imageLabel = newWindow.addLabel(text="", row=0, column=0)
        self.image = PhotoImage(file="htp.gif")
        imageLabel["image"] = self.image
        newWindow.wait_window()  # wait for the new window to close
        MyFrame().mainloop()  # reinstantiate MyFrame and call its mainloop function

    # function if 'Who we are' button clicked
    def wweWindow(self):
        self.destroy()
        newWindow1 = EasyFrame()
        newWindow1.setTitle("WHO WE ARE")
        newWindow1.setResizable(False)
        newWindow1.setSize(800, 600)
        imageLabel1 = newWindow1.addLabel(text="", row=0, column=0)
        self.image = PhotoImage(file="wwe.gif")  # import image
        imageLabel1["image"] = self.image
        newWindow1.wait_window()  # wait for the new window to close
        MyFrame().mainloop()  # reinstantiate MyFrame and call its mainloop function

    # function if 'Rules' button clicked
    def onRules(self):
        rules = {
            "score +1": "Eat 1 fish",
            "time  +5": "Eat 3 fish",
            "time  -3": "Hit the jellyfish",
        }
        sorted_rules = sorted(rules.items(), key=lambda x: x[1])
        message = "\n".join([f"{key}: {value}" for key, value in sorted_rules])
        self.messageBox(title="RULES", message=message)

# class for the game
class sgame:
    def __init__(self):
        # Set up the self.screen
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgpic("bg.gif")
        self.screen.title("Shark Attack!")
        self.screen.tracer(0)  # turn off animation
        # Load images for shark, fish, and jellyfish
        self.screen.addshape("shark.gif")
        self.screen.addshape("sharkright.gif")
        self.screen.addshape("fish.gif")
        self.screen.addshape("jelly.gif")
        # Create a sprite class for the fish
        class Fish(turtle.Turtle):
            def __init__(self):
                super().__init__(shape="fish.gif")
                self.penup()
                x = random.randrange(-340, 240)
                y = random.randrange(-265, 265)
                if x == 0 and y == 0:
                    random.randrange(
                        x + random.randrange(10, 15), y + random.randrange(10, 15)
                    )
                else:
                    self.setpos(x, y)

        # Create a sprite class for the jellyfish
        class Obstacle(turtle.Turtle):
            def __init__(self):
                super().__init__(shape=random.choice(["jelly.gif"]))
                self.penup()
                x = random.randrange(-340, 240)
                y = random.randrange(-265, 265)
                if x == 0 and y == 0:
                    random.randrange(
                        x + random.randrange(10, 15), y + random.randrange(10, 15)
                    )
                else:
                    self.setpos(x, y)

        # Create multiple fish sprites
        self.fish_sprites = []
        for i in range(10):
            fish_sprite = Fish()
            self.fish_sprites.append(fish_sprite)

        # Create multiple jellyfish sprites
        self.obstacle_sprites = []
        for i in range(5):
            obstacle_sprite = Obstacle()
            self.obstacle_sprites.append(obstacle_sprite)

        # Set up the score
        self.score = 0
        self.score_text = turtle.Turtle()
        self.score_text.penup()
        self.score_text.hideturtle()
        self.score_text.setpos(-380, 275)
        self.score_text.pencolor("green")
        self.score_text.write(
            f"Score: {self.score}", align="left", font=("anton", 16, "bold")
        )

        # Set up the timer
        self.time_left = 30
        self.timer_text = turtle.Turtle()
        self.timer_text.hideturtle()
        self.timer_text.penup()
        self.timer_text.setpos(-380, 255)
        self.timer_text.pencolor("red")
        self.timer_text.write(
            f"Time  : {self.time_left}", align="left", font=("anton", 16, "bold")
        )

        # Set up score notification
        self.popup = turtle.Turtle()
        self.popup.hideturtle()
        self.popup.pencolor("gold")

        # Set up time notification
        self.popup2 = turtle.Turtle()
        self.popup2.hideturtle()
        self.popup2.pencolor("red")

        # Function to update timer
        def update_timer():
            global time_left
            self.time_left -= 1
            self.timer_text.clear()
            if self.time_left > 0:
                # Call the update_timer function again after 1 second
                turtle.ontimer(update_timer, 700)
                self.timer_text.write(
                    f"Time  : {self.time_left}",
                    align="left",
                    font=("anton", 16, "bold"),
                )

        # Call the update_timer function to start the timer
        turtle.ontimer(update_timer, 1000)

        # Create a sprite for the shark
        self.shark_sprite = turtle.Turtle()
        self.shark_sprite.shape("shark.gif")
        self.shark_sprite.penup()
        self.shark_sprite.speed(6)
        self.shark_sprite.setpos(0, 0)

        # Set up keyboard controls for the shark
        def move_left():
            self.shark_sprite.shape("shark.gif")
            x = self.shark_sprite.xcor()
            x -= 10
            if x < -340:
                x = -340
            self.shark_sprite.setx(x)

        def move_right():
            self.shark_sprite.shape("sharkright.gif")
            x = self.shark_sprite.xcor()
            x += 10
            if x > 340:
                x = 340
            self.shark_sprite.setx(x)

        def move_up():
            y = self.shark_sprite.ycor()
            y += 10
            if y > 265:
                y = 265
            self.shark_sprite.sety(y)

        def move_down():
            y = self.shark_sprite.ycor()
            y -= 10
            if y < -265:
                y = -265
            self.shark_sprite.sety(y)

        def clear_popup():
            self.popup.clear()

        def clear_popup2():
            self.popup2.clear()

        def exit_window():
            turtle.bye()  # Close the turtle window
            exit()

        self.screen.listen()
        self.screen.onkeypress(move_left, "Left")
        self.screen.onkeypress(move_right, "Right")
        self.screen.onkeypress(move_up, "Up")
        self.screen.onkeypress(move_down, "Down")
        self.screen.onkeypress(exit_window, "Return")

        # Main game loop
        while True:
            # Move the fish sprites randomly
            for fish_sprite in self.fish_sprites:
                fish_sprite.setpos(
                    fish_sprite.xcor() + random.randint(-20, 20),
                    fish_sprite.ycor() + random.randint(-20, 20),
                )
                if fish_sprite.xcor() > 340:
                    fish_sprite.setpos(fish_sprite.xcor() - 10, fish_sprite.ycor())
                elif fish_sprite.xcor() < -340:
                    fish_sprite.setpos(fish_sprite.xcor() + 10, fish_sprite.ycor())
                if fish_sprite.ycor() > 265:
                    fish_sprite.setpos(fish_sprite.xcor(), fish_sprite.ycor() - 10)
                elif fish_sprite.ycor() < -265:
                    fish_sprite.setpos(fish_sprite.xcor(), fish_sprite.ycor() + 10)

            # Move the obstacles randomly
            for obstacle_sprite in self.obstacle_sprites:
                obstacle_sprite.setpos(
                    obstacle_sprite.xcor() + random.randint(-30, 30),
                    obstacle_sprite.ycor() + random.randint(-30, 30),
                )
                if obstacle_sprite.xcor() > 340:
                    obstacle_sprite.setpos(
                        obstacle_sprite.xcor() - 10, obstacle_sprite.ycor()
                    )
                elif obstacle_sprite.xcor() < -340:
                    obstacle_sprite.setpos(
                        obstacle_sprite.xcor() + 10, obstacle_sprite.ycor()
                    )
                if obstacle_sprite.ycor() > 265:
                    obstacle_sprite.setpos(
                        obstacle_sprite.xcor(), obstacle_sprite.ycor() - 10
                    )
                elif obstacle_sprite.ycor() < -265:
                    obstacle_sprite.setpos(
                        obstacle_sprite.xcor(), obstacle_sprite.ycor() + 10
                    )
            self.screen.tracer(1)  # Turn on the animation

            # Check for collision between shark and fish
            for fish_sprite in self.fish_sprites:
                if self.shark_sprite.distance(fish_sprite) < 70:
                    fish_sprite.hideturtle()
                    self.fish_sprites.remove(fish_sprite)
                    # Check if 3 fish eaten
                    if (
                        len(self.fish_sprites) == 7
                        or len(self.fish_sprites) == 4
                        or len(self.fish_sprites) == 1
                    ):
                        self.time_left += 5
                        self.popup2.penup()
                        self.popup2.goto(
                            self.shark_sprite.xcor() + 5, self.shark_sprite.ycor() + 5
                        )
                        self.popup2.pendown()
                        self.popup2.write(
                            "+5", align="left", font=("anton", 20, "bold")
                        )
                        turtle.ontimer(clear_popup2, 1000)
                    self.popup.penup()
                    self.popup.goto(self.shark_sprite.xcor(), self.shark_sprite.ycor())
                    self.popup.pendown()
                    self.popup.pencolor("gold")
                    self.popup.write("+1", align="left", font=("anton", 20, "bold"))
                    turtle.ontimer(
                        clear_popup, 1000
                    )  # Call the function after a second
                    self.score += 1
                    self.score_text.clear()
                    self.score_text.write(
                        f"Score: {self.score}", align="left", font=("anton", 16, "bold")
                    )

            # Check for collision between shark and obstacles(jellyfish)
            for obstacle_sprite in self.obstacle_sprites:
                if self.shark_sprite.distance(obstacle_sprite) < 70:
                    self.time_left -= 3
                    self.popup2.penup()
                    self.popup2.goto(
                        self.shark_sprite.xcor() + 5, self.shark_sprite.ycor()
                    )
                    self.popup2.pendown()
                    self.popup2.write("-3", align="left", font=("anton", 20, "bold"))
                    turtle.ontimer(clear_popup2, 1000)

            # Check if all fish have been eaten
            if not self.fish_sprites:
                self.screen.clear()
                self.time_left = 0
                turtle.bgcolor("steel blue")
                turtle.up()
                self.screen.addshape("youwon.gif")
                mg = turtle.Turtle()
                mg.up()
                mg.goto(0, 50)
                mg.shape("youwon.gif")
                self.screen.addshape("scores.gif")
                dk = turtle.Turtle()
                dk.up()
                dk.goto(-50, -150)
                dk.shape("scores.gif")
                turtle.goto(85, -180)
                turtle.color("white")
                turtle.write(
                    f"{self.score}", align="right", font=("anton", 40, "bold", "italic")
                )
                turtle.hideturtle()
                return

            # Check if times up
            if self.time_left <= 0 and len(self.fish_sprites) != 0:
                self.screen.clear()
                turtle.bgcolor("steel blue")
                turtle.up()
                self.screen.addshape("timeup.gif")
                mg = turtle.Turtle()
                mg.up()
                mg.goto(0, 50)
                mg.shape("timeup.gif")
                self.screen.addshape("scores.gif")
                dk = turtle.Turtle()
                dk.up()
                dk.goto(-50, -150)
                dk.shape("scores.gif")
                turtle.goto(80, -180)
                turtle.color("white")
                turtle.write(
                    f"{self.score}", align="right", font=("anton", 40, "bold", "italic")
                )
                turtle.hideturtle()
                return

            self.screen.update()  # Update the self.screen
        self.screen.mainloop()  # Keep window opened

# main function
def main():
    MyFrame().mainloop()  # Instantiate MyFrame and call its mainloop function

# Call the main function
if __name__ == "__main__":
    main()
