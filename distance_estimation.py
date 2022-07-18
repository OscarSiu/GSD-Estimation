# GSD calculation created by Oscar SIU #
# Initiated on 31 Mar 2022 #
# Ref: https://www.propelleraero.com/blog/ground-sample-distance-gsd-calculate-drone-data/

from PIL import Image

# Find image dimension
def find_dim(path):
    image = Image.open(path)
    imW, imH = image.size
    print("Image Width = ", imW, "Image Height = ", imH)
    #image.show()

    return imW, imH


# GSD Calculation (cm/pixel)
# GSDh= flight height x sensor height / focal length x image height;
# GSDw= flight height x sensor width / focal length x image width 
def gsd_calculation(Fh, Fr, Sw, Sh, imW, imH):
    GSDw = (Fh * Sw * 100) / (Fr * imW)
    GSDh = (Fh * Sh * 100) / (Fr * imH)
    print("GSD width: ","{:.2f}".format(GSDw), "cm/pixel, GSD height: ", "{:.2f}".format(GSDh), "cm/pixel")

    # Dimension of single image footprint (m)
    DW = GSDw * imW / 100
    DH = GSDh * imH / 100
    print("DW: ", "{:.2f}".format(DW), "m, DH: ", "{:.2f}".format(DH), "m\n")

