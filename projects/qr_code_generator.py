import qrcode

apple = qrcode.make("Apple 🍎")
type(apple)

apple.save("apple.png")
