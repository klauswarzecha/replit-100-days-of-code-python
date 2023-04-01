from flask import Flask, render_template, url_for


app = Flask(__name__)

blogposts = {    
    '1':  {
            'title': 'Double, double...', 
            'subtitle':'Toil And Trouble...', 
            'date':'2023-01-03', 
            'text': [
                'fire burn and caldron bubble'
            ]
          }, 

    '19': {
            'title': 'Ignorance Is Strength', 
            'subtitle': 'double-plus-good', 
            'date': '2023-01-12', 
            'text': [
                'Sing to the faithful members of the party', 
                'Sing to the party policy', 
                'Sing to our country, mighty Oceania', 
                'Land of peace and victory',    
            ]
        }, 

    '20': {
            'title': 'Flask is Awesome', 
            'subtitle':'Once you know...', 
            'date':'2023-01-23', 
            'text': [
                'I am looking forward to the next lession.'
            ]
        }
}


@app.route('/blog/<number>')
def blog(number: str):
    if number > 20:
        blogpost = blogposts.get(number, '20')
    return render_template('blog.html', blogpost=blogpost)



if __name__ == '__main__':
    app.run('localhost', debug=True)










