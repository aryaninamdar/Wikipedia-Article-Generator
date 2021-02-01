import requests
import Tkinter as tk

# Creating the GUI
window = tk.Tk()
window.title("Wikipedia Article Generator")
window.geometry("1500x900")
window.resizable(width=False, height=False)

# create label/input
canvas = tk.Canvas(window, width=1500, height=900)
canvas.create_line(0, 80, 1500, 80)
canvas.create_line(1100, 80, 1100, 900)
canvas.pack()

# label
prompt = tk.Label(canvas, text="Enter a topic to search in Wikipedia: ", font=('Calibri', 25))
prompt.place(x=10, y=20)

# input
topic_entry = tk.Entry(canvas, font=('Calibri', 25))
topic_entry.place(x=405, y=20)

# search button
search_btn = tk.Button(canvas, text="Search", font=('Calibri', 25), command=lambda: getArticle())
search_btn.place(x=1250, y=25)

# retrieve article/related media data from API's

def getArticle():
    # generate article
    topic = topic_entry.get()

    data = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            'action': 'query',
            'format': 'json',
            'titles': topic,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
        }).json()
    page = next(iter(data['query']['pages'].values()))
    article_title = tk.Label(canvas, text="Article: ", font=('Calibri', 25))
    article_title.place(x=10, y=90)
    article_area = tk.Label(canvas, text=page['extract'], font=('Calibri', 15), wraplength=1070)
    article_area.place(x=10, y=150)

    # show related media
    url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'sortBy=popularity&'
       'apiKey=4f52ee91c734419f8ab8ffeea5010742')

    related_media = requests.get(url)
    related_media = related_media.json()

    related_media_title = tk.Label(canvas, text="Top Headlines: ", font=('Calibri', 25))
    related_media_title.place(x=1110, y=90)

    related_media_area = tk.Label(canvas, text=related_media['articles'][0]['title'], font=('Calibri', 15), wraplength=380)
    related_media_area.place(x=1110, y=150)

    related_media_area2 = tk.Label(canvas, text=related_media['articles'][1]['title'], font=('Calibri', 15), wraplength=380)
    related_media_area2.place(x=1110, y=250)

    related_media_area3 = tk.Label(canvas, text=related_media['articles'][2]['title'], font=('Calibri', 15), wraplength=380)
    related_media_area3.place(x=1110, y=350)

    related_media_area4 = tk.Label(canvas, text=related_media['articles'][3]['title'], font=('Calibri', 15), wraplength=380)
    related_media_area4.place(x=1110, y=450)

    related_media_area5 = tk.Label(canvas, text=related_media['articles'][4]['title'], font=('Calibri', 15), wraplength=380)
    related_media_area5.place(x=1110, y=550)

window.mainloop()
