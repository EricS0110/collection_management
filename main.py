import json
from nicegui import ui


def add_book_clicked():
    ui.notify("Add book clicked")
    return


def add_comic_clicked():
    ui.notify("Add comic clicked")
    return


def add_music_clicked():
    ui.notify("Add music clicked")
    return


def add_movie_clicked():
    ui.notify("Add movie clicked")
    return


def add_television_clicked():
    ui.notify("Add television_clicked")
    return


def build_panel_elements(fields_dict: dict, col_name: str):
    if len(fields_dict) > 10:
        num_columns = 2
    else:
        num_columns = 1

    with ui.grid(columns=num_columns):
        for key, value in fields_dict.items():
            if value == "text":
                ui.input(label=key)
            if value == "number":
                ui.number(label=key)
            if isinstance(value, list):
                ui.radio(value).props('inline')
        # I don't know of a way to do this automatically, hard coding the collections by manual control here
        match col_name:
            case "Books":
                ui.button('Add Item', on_click=add_book_clicked, color='green')
            case "Comics":
                ui.button('Add Item', on_click=add_comic_clicked, color='green')
            case "Music":
                ui.button('Add Item', on_click=add_music_clicked, color='green')
            case "Movies":
                ui.button('Add Item', on_click=add_movie_clicked, color='green')
            case "Television":
                ui.button('Add Item', on_click=add_television_clicked, color='green')


# Get collection configuration details
with open("configuration/collections.json") as collections_file:
    my_collection = json.load(collections_file)

# Create any required iterable lists in one loop through the json doc
collection_names = []
collection_dict = {}
for collection in my_collection:
    collection_names.append(collection['collection_name'])
    collection_dict[collection['collection_name']] = collection['collection_fields']

# Create tabs for each collection, as well as an "About" tab for information
with ui.tabs() as tabs:
    ui.tab(name="Home", icon="home")
    for collection in my_collection:
        ui.tab(name=collection['collection_name'], icon=collection['collection_icon'])
    ui.tab(name="About", icon="info")

# Populate tabs with specified fields
with ui.tab_panels(tabs, value="Home"):
    for tab_name in collection_names:
        with ui.tab_panel(tab_name) as panel:
            build_panel_elements(collection_dict[tab_name], tab_name)
    with ui.tab_panel("About"):
        with open("configuration/about.md") as about_text:
            ui.markdown(about_text.read())
    with ui.tab_panel("Home"):
        with open("configuration/home_screen.md") as home_text:
            ui.markdown(home_text.read())

ui.run(title="Collections App")
