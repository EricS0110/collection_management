from nicegui import ui

from settings import get_settings


book_columns = 1
book_cover_options = ["Paperback", "Hardcover"]
book_condition_options = ["New", "Good", "Worn", "Collapsing"]
comic_columns = 2
music_columns = 1
music_format_options = ["New Vinyl", "Old Vinyl", "CD"]
movie_columns = 1
movie_format_options = ["DVD", "Bluray", "4K"]
television_columns = 1
television_format_options = ["DVD", "Bluray", "4K"]

settings = get_settings()


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


# Create tabs for each collection, as well as an "About" tab for information
with ui.tabs() as tabs:
    home_tab = ui.tab(name="Home", icon="home")
    book_tab = ui.tab(name="Books", icon="import_contacts")
    comic_tab = ui.tab(name="Comics", icon="inventory")
    music_tab = ui.tab(name="Music", icon="album")
    movie_tab = ui.tab(name="Movies", icon="videocam")
    television_tab = ui.tab(name="Television", icon="monitor")
    about_tab = ui.tab(name="About", icon="info")

# Populate tabs with specified fields
with ui.tab_panels(tabs, value="Home"):
    with ui.tab_panel("About"):
        with open("configuration/about.md") as about_text:
            ui.markdown(about_text.read())
    with ui.tab_panel("Home"):
        with open("configuration/home_screen.md") as home_text:
            ui.markdown(home_text.read())
    with ui.tab_panel("Books"):
        with ui.grid(columns=book_columns).style(add="width: 400px"):
            book_title_input = ui.input(label="Title")
            book_author_input = ui.input(label="Author")
            book_series_input = ui.input(label="Series")
            book_series_number_input = ui.number(label="Series Number")
            book_year_input = ui.number(label="Year")
            book_edition_input = ui.number(label="Edition")
            book_isbn_input = ui.input(label="ISBN (or other identifier)")
            book_genre_input = ui.input(label="Genre")
            book_cover = ui.radio(book_cover_options).props("inline")
            book_condition = ui.radio(book_condition_options).props("inline")
            book_button = ui.button('Add Item', on_click=add_book_clicked, color='green')
    with ui.tab_panel("Comics"):
        with ui.grid(columns=comic_columns).style(add="width: 800px"):
            comic_title_input = ui.input(label="Title")
            comic_supertitle_input = ui.input(label="Super Title")
            comic_issue_input = ui.number(label="Issue")
            comic_issuemonth_input = ui.input(label="Issue Month")
            comic_issueyear_input = ui.input(label="Issue Year")
            comic_volume_input = ui.input(label="Volume")
            comic_upc_input = ui.input(label="UPC")
            comic_publisher_input = ui.input(label="Publisher")
            comic_variant_input = ui.input(label="Variant")
            comic_duplicates_input = ui.input(label="Duplicates")
            comic_owner_input = ui.input(label="Owner")
            comic_condition_input = ui.input(label="Condition")
            comic_value_input = ui.number(label="Value")
            comic_valueyear_input = ui.number(label="Value Year")
            comic_button = ui.button('Add Item', on_click=add_comic_clicked, color='green')
    with ui.tab_panel("Music"):
        with ui.grid(columns=music_columns).style(add="width: 400px"):
            music_album_input = ui.input(label="Album")
            music_artist_input = ui.input(label="Artist")
            music_year_input = ui.number(label="Year")
            music_discnumber_input = ui.number(label="Disc Number")
            music_disccount_input = ui.number(label="Disc Count")
            music_genre_input = ui.input(label="Genre")
            music_format_input = ui.radio(music_format_options).props("inline")
            music_button = ui.button('Add Item', on_click=add_music_clicked, color='green')
    with ui.tab_panel("Movies"):
        with ui.grid(columns=movie_columns).style(add="width: 400px"):
            movie_title_input = ui.input(label="Title")
            movie_series_input = ui.input(label="Series")
            movie_seriesnumber_input = ui.number(label="Series Number")
            movie_year_input = ui.number(label="Year")
            movie_genre_input = ui.input(label="Genre")
            movie_discnumber_input = ui.number(label="Disc Number")
            movie_disccount_input = ui.number(label="Disc Count")
            movie_format_input = ui.radio(movie_format_options).props("inline")
            movie_notes_input = ui.input(label="Notes")
            movie_button = ui.button('Add Item', on_click=add_movie_clicked, color='green')
    with ui.tab_panel("Television"):
        with ui.grid(columns=television_columns).style(add="width: 400px"):
            television_title_input = ui.input(label="Title")
            television_year_input = ui.number(label="Year")
            television_season_input = ui.number(label="Season")
            television_discnumber_input = ui.number(label="Disc Number")
            television_disccount_input = ui.number(label="Disc Count")
            television_genre_input = ui.input(label="Genre")
            television_format_input = ui.radio(television_format_options).props("inline")
            television_button = ui.button('Add Item', on_click=add_television_clicked, color='green')

ui.run(title="Collections App", )
