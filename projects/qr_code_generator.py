import qrcode # type: ignore

apple = qrcode.make("Apple 🍎")
type(apple)

apple.save("apple.png")
