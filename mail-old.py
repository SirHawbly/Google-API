# # this file is for a Google
# # Mail Bridge

# # 
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
import base64

from apiclient import errors
from httplib2 import Http
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode('ascii'))}



def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message.decode('ascii'))
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  except errors.HttpError as error:
    print('An error occurred: %s' % error)



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


