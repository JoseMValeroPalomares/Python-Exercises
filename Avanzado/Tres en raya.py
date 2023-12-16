import PySimpleGUI as sg

button_size = (7,3)
Player_One = "X"
Player_Two = "O"
Current_Player = Player_One

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0,]

winner_plays = [[0,1,2], [3,4,7], [6,7,8], [0,3,6], [1,5,8], [2,5,8],[1,4,7], [2,5,8], [0,4,8],[2,5,6]]


layout = [
          [
                sg.Button("",key="0", size=button_size),
                sg.Button("",key="1", size=button_size),
                sg.Button("",key="2", size=button_size)],

          [
                sg.Button("",key="3", size=button_size),
                sg.Button("",key="4", size=button_size),
                sg.Button("",key="5", size=button_size)
                ],

          [
                sg.Button("",key="6", size=button_size),
                sg.Button("",key="7", size=button_size),
                sg.Button("",key="8", size=button_size)
          ],
          [sg.Input("", key="-Nombre-")],
          [sg.Button("He terminado", key="-Ok-")],
          [sg.Text("", key="-Player_Win" ,text_color="Black")],
          [sg.Button("Restart",key="Restart")]
        ]

window = sg.Window("Demo", layout, margins=(100, 100))
game_end = False
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-Ok-":
        break

    if window.Element(event).ButtonText == "" and not game_end == True:
        index = int(event.replace("-", ""))
        deck[index] = Current_Player
        window.Element(event).Update(text=Current_Player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                if deck[winner_play[0]] == Player_One:
                    print("El jugador uno ha ganado")
                    window.Element("-Player_Win").Update("El jugador 1 Gano")
                else:
                    print("El jugador dos  ha ganado")
                    window.Element("-Player_Win").Update("El jugador 2 Gano")
                game_end = True
        if 0 not in deck:
            print("Juego Terminado")

        if Current_Player == Player_One:
            Current_Player = Player_Two
        else:
            Current_Player = Player_One
    if event == "Restart":
        game_end = False
        num_str = "0"
        result_string = "0"
        window.Element("-Player_Win").Update("")
        for i in range (9):
            window.Element(str(i)).Update(text="")
            deck = [0, 0, 0,
                0, 0, 0,
                0, 0, 0, ]




window.Close()

