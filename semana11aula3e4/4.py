import random

class Enigma:
    def __init__(self):
        # Configuração inicial com três rotores e um refletor
        self.rotor1 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.rotor2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
        self.rotor3 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
        self.reflector = list("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    def rotate_rotor(self, rotor):
        return rotor[1:] + rotor[:1]

    def encrypt(self, char):
        # Simulação básica de uma rotação do Enigma (simplificada)
        output = char

        # Passa pelo primeiro rotor
        output = self.rotor1[ord(output) - ord('A')]

        # Passa pelo segundo rotor
        output = self.rotor2[ord(output) - ord('A')]

        # Passa pelo terceiro rotor
        output = self.rotor3[ord(output) - ord('A')]

        # Refletor
        output = self.reflector[ord(output) - ord('A')]

        # Retrocesso pelos rotores (simplificado)
        output = chr(self.rotor3.index(output) + ord('A'))
        output = chr(self.rotor2.index(output) + ord('A'))
        output = chr(self.rotor1.index(output) + ord('A'))

        return output

    def encrypt_message(self, message):
        encrypted_message = ""
        for char in message.upper():
            if char.isalpha():
                encrypted_message += self.encrypt(char)
            else:
                encrypted_message += char
        return encrypted_message

enigma = Enigma()
message = "HELLO"
encrypted_message = enigma.encrypt_message(message)

print(f"Mensagem original: {message}")
print(f"Mensagem criptografada: {encrypted_message}")
