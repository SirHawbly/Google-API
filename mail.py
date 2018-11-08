# # this file is for a Google
# # Mail Bridge

# # Pipeline
# 0. Get Email Type being Sent
# 1. Connect to Google API
# 2. Get and Information for Email
# 3. Pull Email Template
# 4. Fill in any Vars in Template
# 5. Create Message
# 6. Send Message

def fill_in_reminder (line, first, last, event, date, remdays):
	print(' ', end='')



def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  store = file.Storage('token.json')
  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
  service = build('gmail', 'v1', http=creds.authorize(Http()))

  # Call the Gmail API
  email_body = ''
  with open('temp-email.txt', 'r') as email_template:
    for email_line in email_template:
      print(str(email_line), end='')
      first = last = event = date = remdays = 'asdf'
      fill_in_reminder(email_line, first, last, event, date, remdays)
      email_body += email_line

  to_email = from_email = 'bartlett@pdx.edu'
  message = create_message(to_email,from_email,'sub', email_body)
  send_message(service, 'me', message)


if __name__ == '__main__':
    main()


