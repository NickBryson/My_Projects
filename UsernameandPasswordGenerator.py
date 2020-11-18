def username_generator(first_name, last_name):
  username = ''
  if len(first_name) < 3:
    username = first_name + last_name[:4]
  elif len(last_name) < 4:
    username = first_name[:3] + last_name
  elif len(first_name) < 3 and len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

print(username_generator('Nicholas', 'Bryson'))

def password_generator(username):
  password = ''
  for i in range(len(username)):
    password += username[i-1]
  return password

print(password_generator('NicBrys'))