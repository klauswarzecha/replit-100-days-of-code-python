def is_palindrome_simple(phrase: str) -> bool:
  """Determine if the lowercase letters in a phrase form a palindrome"""
  cleaned = ''.join(phrase.split()).lower()
  return cleaned == cleaned[::-1]

def chopchop(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  word = word[1:-1]
  return chopchop(word)

sentence = 'A Man A Plan A Canal Panama'

header = '🌟 Palindrome Checker 🌟'
print(header)
print()
word = input('\nPlease enter a word > ')
cleaned = ''.join(word.split()).lower()

result = chopchop(cleaned)
if result:
  print(f'{word} is a palindrome.')
else:
  print(f'{word} is not a palindrome.')


