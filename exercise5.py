def reverse_string(s):
  if len(s) <= 1:
    return s
  first_char = s[0]
  remaining_string = s[1:]
  reversed_remaining = reverse_string(remaining_string)
  return reversed_remaining + first_char
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Input: {input_string}, Reversed: {reversed_string}")