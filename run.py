#
# Jinja Example
#
# A small Flask app to test the Jinja templating language
#
# March 2015
#
#

# import from Flask and setup the app
from flask import Flask, render_template
app = Flask(__name__)

# setup up root view
@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!",
                           my_list=[0,1,2,3,4,5])

# define __main__ function so can call from command line
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
