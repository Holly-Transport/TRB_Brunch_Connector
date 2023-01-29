# TRB_Brunch_Connector

Every year I host a reunion brunch during the Transportation Research Board meetings. During the pandemic, the meetings were canceled, but to keep the spirit going, I wrote a  python script that will: (1) randomly match each guest with three other people on the invitation list and (2) send them an email with the other guests' names and addresses. After receiving the email, each guest could then reach out to these colleagues -- some familiar, some new -- and let them know what they've been up to this past year. Maybe the exchange would result in a new connection or a catch up coffee date. Just as if they had come to brunch!

I used the Sheety API to generate the random matches, and smtplib for sending the emails. 
