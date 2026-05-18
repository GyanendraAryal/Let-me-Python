class Bird:
    def speak(self):
        return f"Bird is speaking"


class Parrot(Bird):
    def speak(self):
        super().speak()
        return f"Parrot is speaking"
thisBird = Parrot()
print(thisBird.speak())