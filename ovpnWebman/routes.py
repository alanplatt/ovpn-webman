from ovpnWebman import app
from flask import render_template, url_for, request
from ovpnWebman.helpers import check_password

@app.route('/', methods=['GET','POST'])
def submit():
  if request.method == 'POST':
    print (dir(request.form))
    print (request.form)

    if request.form['password1'] == request.form['password2']:
      if check_password(request.form['password1']):
        return request.form['password1']
      else:
        error='Password of insufficient complexity'
    else:
      error='password mismatch'
    return render_template('submit.html.j2', error=error)

  elif request.method == 'GET':
    return render_template('submit.html.j2')


#TODO download the ovpn cert
@app.route("/get-file")
def get_file():
    filedata = generate_file_data()

    return Response(filedata,
                       mimetype="text/plain",
                       headers={"Content-Disposition":
                                    "attachment;filename=test.txt"})
