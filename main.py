from flask import Flask,render_template,request
import os
import json

PEOPLE_FOLDER = os.path.join('static', 'player_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER




@app.route('/')
def show_post():
  goalkeepers = []
  defenders = []
  midfielders = []
  attackers = []



  if request.args.get('defenders') is None:

    x1 = 3
    x2 = 5
    x3 = 2

  else:

    x1 = int(request.args.get('defenders'))
    x2 = int(request.args.get('midfilders'))
    x3 = int(request.args.get('attackers'))


  with open('goalkeepers.json') as json_file:
    data = json.load(json_file)
    
    goalkeepers.append(list(data.keys())[:1])

  with open('defenders.json') as json_file:
    data = json.load(json_file)
    defenders.append(list(data.keys())[:x1])

  with open('midfielders.json') as json_file:
    data = json.load(json_file)
    midfielders.append(list(data.keys())[:x2])



  with open('attackers.json') as json_file:
    data = json.load(json_file)
    attackers.append(list(data.keys())[:x3])



  images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
  hists = os.listdir('static/player_photo')
  hists = ['player_photo/' + file for file in hists]

  return render_template('index.html',goalkeepers=goalkeepers,defenders=defenders,midfielders=midfielders,attackers=attackers,images=images,hists=hists)




if __name__ == '__main__':
  app.run(debug = True)