from threading import Timer
import webbrowser

import dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
port = 500

def open_browser():
    webbrowser.open_new("http://localhost:{}".format(port))


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=False, port=port)
