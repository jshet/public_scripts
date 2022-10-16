from PIL import Image 

def make_thumbnail(im_or_path,max_dimension=1920, save_as="test_out.jpg"):
    original = Image.open(im_or_path)
    thumb = original.copy()
    thumb.thumbnail((max_dimension, max_dimension))
    return original, thumb

def main():
    im_path = "test.jpg"
    save_as = "test_out.jpg"
    thumb = make_thumbnail(im_path, save_as=save_as)
    thumb.save(save_as)

def merge_images(background, overlay):
    overlay_image = Image.open(overlay)
    background.paste(overlay_image,(0,0), overlay_image)
    return background

if __name__ == "__main__":
    main()
