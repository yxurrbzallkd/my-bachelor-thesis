import matplotlib.pyplot as plt


def plot_image(image,w=10,h=6):
    plt.figure(figsize=(w,h))
    plt.imshow(image)
    plt.axis("off")
    plt.show()
    

