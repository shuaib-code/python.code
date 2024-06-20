import pyfiglet

def print_large_text(text, font="standard"):
    ascii_banner = pyfiglet.figlet_format(text, font=font)
    print(ascii_banner)

if __name__ == "__main__":
    text = "43756"
    
    fonts = [
        "banner", "block","isometric1",
        "letters", "dotmatrix"
    ]
    
    for font in fonts:
        print(f"Font: {font}")
        print_large_text(text, font=font)
        print("\n" + "="*80 + "\n")
