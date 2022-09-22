def get_coords():
    """REEDS all Coords"""
    with open("coords.txt") as fobj:
         data = fobj.readlines()
    return data

def get_coords_in_dict():
    """Returns an DICT seperated by X coords and Y coords"""
    data = get_coords
    xdata=[]
    ydata=[]
    allcoords = {}
    for x in data():
        x = x.strip()
        # x.split(',')[0] == "X"
        if x.split(',')[0] != "X":
            xdata.append(x.split(', ')[0])
            ydata.append((x.split(', ')[1]))
        else:
            KeyX = x.split(', ')[0]
            KeyY = x.split(', ')[1]

    allcords = {KeyX: xdata, KeyY: ydata}
    return allcords

def sum_list(xdata, ydata):
    """Gibt die Summe der Coordinaten zurück"""
    summex = 0
    summey = 0
    for x in xdata:
        summex = summex + float(x)
    for y in ydata:
        summey = summey + float(y)
    Ergebnis = (summex, summey)
    return Ergebnis


def sum_dict(coords_dict):
    """Gibt die Summe der Coordinaten Zurück"""
    summex = 0
    summey = 0
    for x in coords_dict["X"]:
        summex = summex + float(x)
    for y in coords_dict["Y"]:
        summey = summey + float(y)
    Ergebnis = (summex, summey)
    return Ergebnis