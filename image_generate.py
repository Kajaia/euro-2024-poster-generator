from PIL import Image, ImageDraw, ImageFont
from image_download import download_image
from slugify import slugify
import datetime

def generate_match_image(home_team, away_team, home_logo_url, away_logo_url):
    # Load the background image
    background_path = "./assets/img/euro-2024-bg.jpg"
    image = Image.open(background_path).convert("RGBA")

    # Initialize drawing context
    draw = ImageDraw.Draw(image)

    # Load fonts
    font_path = "./assets/fonts/montserrat-semibold.ttf"
    teams_name_font = ImageFont.truetype(font_path, 90)

    # Function to draw text with specified position
    def draw_text(draw, text, font, x, y):
        draw.text((x, y), text, fill='white', font=font)

    # Home team name
    home_team_x = 290
    home_team_y = 488
    draw_text(draw, home_team, teams_name_font, home_team_x, home_team_y)

    # Away team name
    away_team_x = 1410
    away_team_y = 488
    draw_text(draw, away_team, teams_name_font, away_team_x, away_team_y)

    # Download and resize team logos
    home_logo = download_image(home_logo_url).convert("RGBA")
    away_logo = download_image(away_logo_url).convert("RGBA")
    logo_size = (350, 350)
    home_logo = home_logo.resize(logo_size, Image.LANCZOS)
    away_logo = away_logo.resize(logo_size, Image.LANCZOS)

    # Calculate logo positions
    home_logo_x = 252
    home_logo_y = 122
    away_logo_x = 1339
    away_logo_y = 122

    # Paste logos onto the image
    image.paste(home_logo, (home_logo_x, home_logo_y), home_logo)
    image.paste(away_logo, (away_logo_x, away_logo_y), away_logo)

    # Save the image
    current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    image_path = f"./generated/{slugify(home_team)}-vs-{slugify(away_team)}-{current_date}.png"
    image.save(image_path)
    return image_path