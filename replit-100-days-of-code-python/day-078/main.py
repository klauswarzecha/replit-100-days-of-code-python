from replit import db

from flask import Flask, render_template

def populate_db():
  db[77] = {
    'url': 'https://replit.com/@klauswarzecha/day77', 
    'ref': 'More work with Flask. Will there be someting about Jinja2 as well?'
    
  }
  db[76] = {
    'url': 'https://replit.com/@klauswarzecha/day76', 
    'ref': 'This is the lesson Flask was introduced. Pretty cool!'
  }
  db[75] = {
    'url': 'https://replit.com/@klauswarzecha/day75', 
    'ref': 'Created a Link Tree page with lots of links to scientific networks.'
  }

app = Flask(__name__)
"""
@app.route('/<pageNumber>')
def index(pageNumber):
  
  return f"This is page {pageNumber}"
"""


@app.route('/<pagenumber>')
def index(
  pagenumber,
  href=None, 
  reflection=None
):
  
    data = db[pagenumber]
    
    return render_template(
      'reflection.html', 
      pagenumber=pagenumber, 
      href=data.get('url'), 
      reflection=data.get('ref')
    )


populate_db()
app.run(host='0.0.0.0', port=81, debug=True)