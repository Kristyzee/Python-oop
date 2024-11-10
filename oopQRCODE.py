import qrcode
from tkinter import Tk, filedialog, colorchooser
from tkinter import simpledialog


########################      Assigment 1: QR Code

class QRCodeGenerator:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def get_data(self):
        return simpledialog.askstring("Input", "Enter data to convert to QR code")

    def get_save_path(self):
        return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])

    def get_color(self, color_type):
        color = colorchooser.askcolor(title=f"Choose {color_type} color")
        return color[1]

    def generate_qr_code(self):
        data = self.get_data()
        save_path = self.get_save_path()
        name = save_path.split("/")[-1].split(".")[0]

        background_color = self.get_color("background")
        fill_color = self.get_color("fill color")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=background_color)

        img.save(save_path)

        print(f"Success! You can check your folder for {name}.png")

if __name__ == "__main__":
    generator = QRCodeGenerator()
    generator.generate_qr_code()





