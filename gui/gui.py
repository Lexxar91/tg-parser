import asyncio
import tkinter as tk

from parser import tg_parser_channel


async def parse_telegram():
    await tg_parser_channel.parse_start()


def on_button_click():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(parse_telegram)
    loop.close()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Парсить Телеграм",
                   fg="red",
                   command=on_button_click)
button.pack(side=tk.LEFT)

root.mainloop()
