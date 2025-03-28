from PIL import Image

# Load the scrambled image
scrambled_img = Image.open("scrambled_image.png")  # Change file name if needed

# Image dimensions and grid size
img_size = 500
grid_size = 5
piece_size = img_size // grid_size  # 100x100 per piece

# Mapping of (Original Row, Original Col) -> (Scrambled Row, Scrambled Col)
mapping = [
    (2, 1, 0, 0),
    (1, 1, 0, 1),
    (4, 1, 0, 2),
    (0, 3, 0, 3),
    (0, 1, 0, 4),
    (1, 4, 1, 0),
    (2, 0, 1, 1),
    (2, 4, 1, 2),
    (4, 2, 1, 3),
    (2, 2, 1, 4),
    (0, 0, 2, 0),
    (3, 2, 2, 1),
    (4, 3, 2, 2),
    (3, 0, 2, 3),
    (3, 4, 2, 4),
    (1, 0, 3, 0),
    (2, 3, 3, 1),
    (3, 3, 3, 2),
    (4, 4, 3, 3),
    (0, 2, 3, 4),
    (3, 1, 4, 0),
    (1, 2, 4, 1),
    (1, 3, 4, 2),
    (0, 4, 4, 3),
    (4, 0, 4, 4),
]

# Create a new blank image
reconstructed_img = Image.new("RGB", (img_size, img_size))

# Process each piece according to the mapping
for orig_row, orig_col, scram_row, scram_col in mapping:
    # Calculate pixel positions
    src_x = scram_col * piece_size
    src_y = scram_row * piece_size
    dst_x = orig_col * piece_size
    dst_y = orig_row * piece_size

    # Extract the piece from the scrambled image
    piece = scrambled_img.crop((src_x, src_y, src_x + piece_size, src_y + piece_size))

    # Paste it into the correct position in the reconstructed image
    reconstructed_img.paste(piece, (dst_x, dst_y))

# Save the reconstructed image
reconstructed_img.save("reconstructed_image.png")

# Show the final result
reconstructed_img.show()
