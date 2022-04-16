import dash
from dash import html
import feffery_antd_components as fac

app=dash.Dash(__name__)
app.layout=html.Div([fac.AntdTitle('你好，dash',level=3),
                     fac.AntdText(f"dash version is {dash.__version__}"),
                     fac.AntdDivider(),
                     fac.AntdText(f'fac version is {fac.__version__}')])


if __name__=='__main__':
    app.run_server(debug=True)