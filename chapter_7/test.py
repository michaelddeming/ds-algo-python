

class Watch:

    def __init__(self, band_color: str, face_color: str):

        self.band_color = band_color
        self.face_color = face_color

        self.price = 100

    

watch_1 = Watch(band_color="Silver", face_color="Brown")

print(watch_1.band_color)

watch_1.band_color = "Purple"

print(watch_1.band_color)













