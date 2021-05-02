/submit/expense/
  POST, returns a jason
  input : date (optional), text, amount, token
  output: status:ok

/submit/income/
  POST, returns a jason
  input : date (optional), text,     amount, token
  output: status:ok



/accounts/register/
step1:
POST
input: username, email, password
output: #click on link with the code in hte email
GET
input: email, code
output: ok (shows the token)

/q/generalstat/
POST, returns a json input: fromdate (optional), todate(optional), token
output: json from some general stats related to this user