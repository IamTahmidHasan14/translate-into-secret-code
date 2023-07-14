import random
def encode(word):
  if len(word) < 3:
    return word[::-1]
  else:
    first_letter = word[0]
    new_word = word[1:] + first_letter
    random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    return random_chars + new_word + random_chars
def decode(word):
  if len(word) < 3:
    return word[::-1]
  else:
    random_chars = word[:3] + word[-3:]
    new_word = word[3:-3]
    last_letter = new_word[-1]
    return last_letter + new_word[:-1]
def main():
  message = input("Enter your message: ")
  choice = input("Do you want to code or decode? ")
  words = message.split()
  if choice == "code":
    result = [encode(word) for word in words]
  elif choice == "decode":
    result = [decode(word) for word in words]
  else:
    print("Invalid choice")
    return
  print(' '.join(result))
if __name__ == '__main__':
  main()