with open("firmware.bin", "rb") as f:
    with open("firmware_hex.bin", "w+") as g:
        lines = f.read()
        for item in lines:
            g.write(str(item) + '\n')